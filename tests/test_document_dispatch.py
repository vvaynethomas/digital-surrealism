import ast
import contextlib
import io
from pathlib import Path
from random import randint
import unittest
from unittest.mock import Mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ("fragment_generator.py", "anaphoric writing.py")


def load_dispatcher(script, pdf, docx):
    # Avoid importing dependencies or running the scripts' local experiments.
    source = ROOT / script
    tree = ast.parse(source.read_text(encoding="utf-8-sig"), filename=script)
    function = next(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "extract_from_document"
    )
    namespace = {
        "randint": randint,
        "extract_from_pdf": pdf,
        "extract_from_docx": docx,
    }
    exec(compile(ast.Module(body=[function], type_ignores=[]), script, "exec"),
         namespace)
    return namespace["extract_from_document"]


class DocumentDispatchTests(unittest.TestCase):
    def test_pdf_returns_result_and_forwards_options(self):
        for script in SCRIPTS:
            for result in ("sample text", ["sample", "runs"], None):
                with self.subTest(script=script, result=result):
                    pdf, docx = Mock(return_value=result), Mock()
                    dispatch = load_dispatcher(script, pdf, docx)
                    self.assertIs(
                        dispatch("input.pdf", output_type="all", output_size=7),
                        result,
                    )
                    pdf.assert_called_once_with(
                        "input.pdf", type="page", output_type="all", output_size=7
                    )
                    docx.assert_not_called()

    def test_docx_behavior_is_unchanged(self):
        for script in SCRIPTS:
            with self.subTest(script=script):
                result = ["existing DOCX result"]
                pdf, docx = Mock(), Mock(return_value=result)
                dispatch = load_dispatcher(script, pdf, docx)
                self.assertIs(dispatch("input.docx", "runs", 9), result)
                docx.assert_called_once_with("input.docx", "runs", 9)
                pdf.assert_not_called()

    def test_missing_pdf_keeps_existing_diagnostic(self):
        for script in SCRIPTS:
            with self.subTest(script=script):
                dispatch = load_dispatcher(
                    script, Mock(side_effect=FileNotFoundError), Mock()
                )
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    self.assertIsNone(dispatch("missing.pdf"))
                self.assertEqual(output.getvalue(), "couldn't scrape pdf\n")

    def test_other_pdf_errors_are_not_swallowed(self):
        for script in SCRIPTS:
            with self.subTest(script=script):
                dispatch = load_dispatcher(
                    script, Mock(side_effect=ValueError("invalid PDF")), Mock()
                )
                with self.assertRaisesRegex(ValueError, "invalid PDF"):
                    dispatch("input.pdf")


if __name__ == "__main__":
    unittest.main()
