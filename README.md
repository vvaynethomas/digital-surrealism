# digital-surrealism
modules for generating texts, images, and hybrid forms

An experimental collection of Python scripts for recombining source documents
and images: word chunks, shuffled lines and paragraphs, corpus-based text,
image grids and blends, and OCR-based text/image experiments. The methods use
sampling, shuffling, NLTK tokenization and tagging, and document/image processing.
This is not a packaged application or a pretrained generative model.

## Where to start

Start by **reading `fragment_generator.py`**, especially `fragment_writer` and its
final call, `fragment_writer(alt_directory, 4)`. It is a compact entry point to
the document-fragment method: sample chunks from source documents, filter words,
and arrange the chunks in a Word document. Although it contains PDF helpers,
the writer currently filters its source list to DOCX files.

There is no command-line interface or verified one-command demo. Do not import
these scripts just to inspect their functions: many execute experiments, create
directories, change the working directory, or write files at module scope.
`graphic_text_scratch.py` also imports an image module that executes work itself.

Replace local paths with your own or it just won't work, unsurprisingly. Changing
only the input path is not enough: inspect output paths inside functions as well
as the final experiment block. Work on copies of source material in a disposable
workspace, not an entire home directory.

## Script map

These descriptions are based on source inspection, not end-to-end execution.
Names describe the experiments in the files, not a guarantee that each path works.

| Script | Methods and intended input/output | Current caveat |
| --- | --- | --- |
| `fragment_generator.py` | DOCX chunks assembled into fragments in a new DOCX; also contains PDF extraction helpers. | Final call runs immediately; output location is embedded in `fragment_writer`. |
| `generate_texts.py` | DOCX sentence/paragraph sampling and bigram conditional-frequency text, arranged in DOCX strophes. | Final block generates noun-seeded lines using local folders. |
| `text_generating_progs.py` | Larger collection: document extraction, vignettes, shuffles, fragments, corpus text, and stanza forms. | Final block runs stanza experiments; also includes HTML processing. |
| `poems_from_fragments.py` | PDF/DOCX extraction, keyword-selected lines, phrase assembly, and poem writing to DOCX. | Sets up local output at module scope; `poem_writer` can move source files. Use copies. |
| `multidocumentmultitypewriter.py` | Multi-document line shuffling, refrains, proper-noun exchange, and vignettes; DOCX output and optional plots. | Final block calls `construct_global_shuffle` on local folders. |
| `anaphoric writing.py` | PDF/DOCX chunk gathering and part-of-speech experiments, with console output. | Executes at module scope; document-saving experiment is commented out. |
| `essay_generator.py` | Early DOCX/essay and n-gram experiment. | Incomplete: includes `randint(28-32)` and references to undefined names such as `articles` and `NgramModel`. |
| `essay generator 2.py` | DOCX sentence extraction and an essay-assembly experiment. | `generate_essay` is nested inside `extract_sentence`, not exposed as a module-level entry point. |
| `robopoetry_functions.py` | PDF image/text extraction, verse/vignette helpers, and page shuffling. | Cannot parse: an `except` block has only comments (see verification below). |
| `image_processing_functions.py` | JPEG grids/tiling, cubomanic and stripomanic arrangements, blends, PDF conversion, image scraping, and OCR; image/DOCX output. | Includes local Tesseract settings and module-level image experiments; network helpers fetch external content. |
| `graphic_text_scratch.py` | Scratch driver for repeated image arrangements and blends. | Imports the side-effecting image module; also references undefined names such as `final_directory` and `text_image_pages`. |

## Inputs, outputs, and local assumptions

No source corpus, sample PDF/DOCX, sample images, or generated works are tracked
in this checkout. Supply your own material that you have permission to process.
Text extraction expects readable text in DOCX or PDF; scanned PDFs need a
separate OCR path, and several PDF routines skip or fail on unsuitable files.
The fragment writer needs enough usable DOCX text for repeated chunk sampling.
Empty, short, or unsuitable inputs can cause exceptions or unbounded retry loops.

The scripts contain absolute Windows paths to the original working folders.
Those folders are not distributed. Some helpers depend on trailing separators,
concatenate path strings, or derive output names from source text. Several use
`os.chdir`, so later relative paths depend on earlier calls. Output folders must
be writable; generated names may collide or be invalid on a different system.
Image discovery in `get_imlist` is limited to lowercase `.jpg` paths and expects
directory strings ending in a separator.

Before running a selected experiment, inspect its full call chain, replace all
relevant input/output and executable paths, and restrict it to a small copied
corpus. Review generated work manually: source names/sections may be recorded by
some routines, but attribution and provenance are not comprehensive or verified.
Do not publish private source text, local paths, or outputs without reviewing
privacy and reuse rights. Random choices are not seeded consistently, so exact
output reproduction is not promised.

## Dependencies

Imports establish the following package names. There is no dependency lockfile,
known-good version set, or verified installation recipe; this is an inventory,
not a claim that installing the latest releases makes the scripts work.

| Python import | Distribution | Used for |
| --- | --- | --- |
| `docx` | `python-docx` | Reading and writing Word documents across text/image experiments. |
| `nltk` | `nltk` | Vocabulary filtering, tokenization, tagging, and corpus statistics. |
| `PyPDF2` | `PyPDF2` | Legacy PDF extraction in document/image helpers. |
| `PIL` | `Pillow` | Image reading, manipulation, and saving. |
| `numpy`, `scipy` | `numpy`, `scipy` | Image/grid numerical helpers, including a SciPy wildcard import. |
| `pdf2image` | `pdf2image` | PDF rendering for image experiments. |
| `pytesseract` | `pytesseract` | OCR wrapper; also requires the external Tesseract executable and language data. |
| `requests`, `bs4` | `requests`, `beautifulsoup4` | Network image scraping and HTML parsing. |
| `matplotlib.pyplot` | `matplotlib` | Plotting in `poems_from_fragments.py` and `multidocumentmultitypewriter.py`. |

`pdf2image` also needs Poppler tools such as `pdftoppm`/`pdfinfo`.
The image module hardcodes Tesseract executable/data locations; check both,
including the spelling of the data-folder setting. PDF code uses older
`PdfFileReader`, `getPage`, and `extractText` APIs that are incompatible with
PyPDF2 3.x. Image code also contains older APIs such as `np.product`; current
dependency compatibility is untested. The image module's original comment
mentions Anaconda 3.x, but no exact historical environment is supplied.

### NLTK data

Installing NLTK alone does not supply its corpora/models. Source inspection
establishes use of `corpus.words.words()` (including at import time),
`word_tokenize`/`sent_tokenize`, and English `pos_tag`.

| Operation | Data to check for the chosen NLTK version |
| --- | --- |
| English vocabulary | `words` corpus |
| Word/sentence tokenization | Punkt data: `punkt` in older versions; newer versions may require `punkt_tab` |
| English part-of-speech tagging | `averaged_perceptron_tagger` in older versions; newer versions may require `averaged_perceptron_tagger_eng` |

Use the chosen version's NLTK downloader and its resource lookup errors to
resolve those names. No NLTK downloads, resource availability checks, or tagging
runs were performed for this pass because NLTK was not installed.

## Existing method example

`partition_word_list` in `fragment_generator.py` groups a list into successive
chunks without rearranging it. Its body was checked in isolation, with an
explicit chunk length:

```python
partition_word_list(["one", "two", "three", "four", "five"], chunk_length=2)
# [['one', 'two'], ['three', 'four'], ['five']]
```

This is a helper example with synthetic input, not a generated poem or a claim
that importing/running the whole script works. The check extracted only that
function's syntax tree, provided its existing `randint` default dependency,
and executed the function without the module's imports or final writer call.
No publication-ready generated text or artwork was found in the tracked files;
none has been invented for this README.

## Recorded checks and remaining work

Checks on 2026-10-24 used Python 3.14.2 on Windows:

| Check | Observed result |
| --- | --- |
| Parse all 11 `.py` files with `ast.parse` (no script imports/execution) | 10 parse; `robopoetry_functions.py` fails at line 580 because the `except` at line 564 has no executable body. Existing invalid-escape sequences also produce syntax warnings. Parsing does not establish runtime correctness. |
| Isolated `partition_word_list` check above | Returned the displayed list; exact result asserted. |
| Dependency metadata and module discovery | `python-docx` 1.2.0 present; all other distributions listed above absent. No application dependency imports were tested. |
| Executable discovery on `PATH` | `tesseract`, `pdftoppm`, and `pdfinfo` not found; hardcoded executable locations were not checked. |
| Tracked-file inventory | No sample corpora, generated examples, dependency manifest, test suite, or license file found. No verified generated clutter needed removal. |

Full script execution, PDF/DOCX extraction, text generation, image processing,
OCR, network scraping, and output provenance remain **untested**. This pass
does not modify algorithms or repair the historical experiments. Follow-up work
could select a single portable demo, resolve its dependencies and existing
runtime errors, provide rights-cleared sample input, configure paths, and add
a smoke test. A complete gallery or package is not required to read the project.

## Reuse and collaboration

Please contact me if you'd like to collaborate or use these tools in a public or commercial way.

No license file is currently provided. Licensing and permissions for both code
and source/output material need a maintainer decision; this documentation does
not grant new reuse rights or choose a license.
