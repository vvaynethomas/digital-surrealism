# digital-surrealism

Python experiments in found-text poetry, image collage, and hybrid forms.

What happens when a document becomes a supply of phrases, or a page becomes
material for a collage? These scripts explore that question through chance and
recombination: sampling word chunks, shuffling lines across documents, building
corpus-based verse, and rearranging images into grids, strips, and blends.
NLTK vocabulary filters and part-of-speech tags add constraints to the text
experiments; image processing and OCR connect the visual and verbal work.

This is a collection of creative working scripts, not a packaged application,
pretrained generative model, or ready-to-run gallery. You can explore the
methods by reading the source without installing anything. Running them takes
local adaptation; the original source materials and generated works are not
included.

## Explore the experiments

| Follow an idea | Start here | What to look for |
| --- | --- | --- |
| Build a poem from fragments | [fragment_generator.py](fragment_generator.py) | `fragment_writer` samples DOCX chunks, filters words, and arranges fragments in a new Word document. |
| Turn a corpus into verse | [generate_texts.py](generate_texts.py) | `create_corpus`, `generate_bigrams_cfd`, and `generate_lines_from_corpus` connect source vocabulary, word-pair statistics, and seed selection; `write_lines_in_strophes` arranges lines. |
| Shuffle voices across documents | [multidocumentmultitypewriter.py](multidocumentmultitypewriter.py) | `construct_global_shuffle`, `trade_props`, and `write_vignettes` explore line recombination, proper-noun exchange, and short prose forms. |
| Cut and reassemble images | [image_processing_functions.py](image_processing_functions.py) | `grid_image`, `create_cubomanic`, and `create_stripomanic` work with square crops or strips; `merge_images` blends images. |
| Move between text and image | [image_processing_functions.py](image_processing_functions.py) | PDF rendering, `get_text_from_image`, and `create_altered_text_images` explore page images, OCR, and visual transformations. |

These are source-reading routes through the experiments, not independently
verified runnable recipes.

### A first reading: document fragments

Start with `fragment_writer` in
[fragment_generator.py](fragment_generator.py). Follow its calls to
`get_filepaths`, `extract_from_document`, and `extract_from_docx`:

1. Discover documents in an input directory. The writer currently selects DOCX
   sources even though the file also contains PDF helpers.
2. Sample chunks of 4-14 words, tokenize them, and filter against NLTK's English
   vocabulary.
3. Recombine chunks into fragments with line breaks, then save a DOCX with a
   title drawn from the source material.

The final call, `fragment_writer(alt_directory, 4)`, requests four fragments.
It also runs immediately when the file is imported or executed, using embedded
local paths. **Read the script before running it.**

### More paths through the collection

| File | Focus and important boundary |
| --- | --- |
| [text_generating_progs.py](text_generating_progs.py) | A larger workshop of extraction, vignettes, shuffles, fragments, corpus text, and stanza forms, plus HTML processing. Its final block runs stanza experiments. |
| [poems_from_fragments.py](poems_from_fragments.py) | PDF/DOCX extraction, keyword-selected lines, phrase assembly, and DOCX poems. Sets up output at module scope; `poem_writer` can move source files, so use copies. |
| [anaphoric writing.py](anaphoric%20writing.py) | Chunk gathering and part-of-speech experiments with console output. Executes at module scope; the document-saving experiment is commented out. |
| [essay_generator.py](essay_generator.py) | Early DOCX/essay and n-gram experiment. Incomplete, including `randint(28-32)` and undefined names such as `articles` and `NgramModel`. |
| [essay generator 2.py](essay%20generator%202.py) | Sentence extraction and essay assembly. `generate_essay` is nested inside `extract_sentence`, not a module-level entry point. |
| [robopoetry_functions.py](robopoetry_functions.py) | PDF image/text extraction, verse/vignette helpers, and page shuffling. A comment-only `except` block prevents the file from parsing. |
| [graphic_text_scratch.py](graphic_text_scratch.py) | Scratch driver for image arrangements and blends. Imports the side-effecting image module and references undefined names, including `final_directory` and `text_image_pages`. |

## Working with your own material

There is no command-line interface, dependency manifest, locked environment,
or verified one-command demo. For an adapted experiment, the intended flow is
**your source copies -> extraction or cropping -> randomized recombination ->
DOCX or image output -> manual selection and editing**.

1. Choose one method and read its full call chain, including the final
   experiment block. Many files create directories, change the working
   directory, or write files at module scope; importing is not a safe preview.
2. Prepare a small, disposable copy of material you have permission to process.
   Text methods use DOCX or readable PDF text; scanned PDFs need a separate OCR
   path. Image discovery in `get_imlist` recognizes lowercase `.jpg` paths and
   expects directory strings ending in a separator.
3. Use an isolated Python environment and select dependencies for that method
   from the inventory below. Resolve legacy API compatibility before attempting
   generation; installing the latest packages is not a verified setup.
4. Replace all relevant input, output, and executable paths, including paths
   inside helper functions. Restrict discovery to the copied input folder, not
   an entire home directory, and choose a writable output folder.
5. Review the output and its sources before sharing. Some routines record
   filenames or sections, but source attribution is not comprehensive or
   verified. Check reuse rights, private text, and exposed local paths yourself.

### Dependency inventory

The imports identify these distributions; this is not a known-good version set.
Even a text-only method may live in a file importing additional packages.

| Python import | Distribution | Role |
| --- | --- | --- |
| `docx` | `python-docx` | Read and write Word documents. |
| `nltk` | `nltk` | Vocabulary, tokenization, tagging, and corpus statistics. |
| `PyPDF2` | `PyPDF2` | Legacy PDF extraction. |
| `PIL` | `Pillow` | Read, transform, and save images. |
| `numpy`, `scipy` | `numpy`, `scipy` | Numerical and image/grid helpers. |
| `pdf2image` | `pdf2image` | Render PDF pages; also requires external Poppler tools such as `pdftoppm` and `pdfinfo`. |
| `pytesseract` | `pytesseract` | OCR wrapper; also requires Tesseract and its language data. |
| `requests`, `bs4` | `requests`, `beautifulsoup4` | Network image scraping and HTML parsing. |
| `matplotlib.pyplot` | `matplotlib` | Optional plotting paths in the poem and multi-document scripts. |

NLTK needs data beyond the Python package: the `words` corpus, Punkt
tokenization data (`punkt`, or `punkt_tab` in newer versions), and English
tagger data (`averaged_perceptron_tagger`, or
`averaged_perceptron_tagger_eng` in newer versions). Some files load the
vocabulary at import time. Use your chosen NLTK version's downloader and
resource lookup errors to identify the required data.

### Current boundaries

The original absolute Windows paths must be adapted, including the image
module's Tesseract executable/data settings (the data-folder path contains a
spelling error). Some helpers concatenate path strings or call `os.chdir`;
generated filenames can collide or be invalid on another system.

The PDF helpers use older `PdfFileReader`, `getPage`, and `extractText` APIs
that are incompatible with PyPDF2 3.x. Image code includes older APIs such as
`np.product`; current dependency compatibility is unverified. The image
module's original environment note mentions Anaconda 3.x, but supplies no
exact environment.

Empty, short, or unsuitable inputs can cause exceptions or unbounded retry
loops. Random choices are not seeded consistently, so exact reproduction is
not promised. Network helpers fetch external content; a downloaded image is
not automatically cleared for reuse. The incomplete scripts noted above need
repair before use. Full extraction, generation, image processing, OCR, and
scraping workflows have not been verified end to end.

## Focused regression tests

[tests/test_document_dispatch.py](tests/test_document_dispatch.py) checks the
PDF/DOCX dispatchers in `fragment_generator.py` and `anaphoric writing.py`.
Run from the repository root with Python's standard library:

```powershell
python -m unittest discover -s tests -v
```

The tests extract the dispatcher functions through their syntax trees and mock
the extractors, avoiding module-level experiments and external dependencies.
They cover return values, option forwarding, DOCX behavior, missing-file
diagnostics, and other exception propagation. They do **not** exercise real
PDF extraction or establish that a creative workflow runs successfully.

## Reuse and collaboration

Please contact me if you'd like to collaborate or use these tools in a public or commercial way.

No license file is currently provided. Licensing and permissions for both code
and source/output material need a maintainer decision; this documentation does
not grant new reuse rights or choose a license.
