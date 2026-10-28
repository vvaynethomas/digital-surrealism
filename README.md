# digital-surrealism

A Python workshop for found-text poetry, image collage, and hybrid forms.

Documents become supplies of phrases; images become pieces to cut, shuffle, and
layer. These experiments use chance and recombination to find new relationships
inside existing material: a line meeting an unfamiliar voice, a poem assembled
from fragments, a page rearranged into a visual composition.

The collection brings together word sampling, corpus-based verse, line shuffling,
square and strip collages, image blending, and OCR. NLTK vocabulary filters and
part-of-speech tags give the text experiments constraints to play against.

## Find a starting point

Browse the source by the kind of transformation that interests you:

| Explore | Start here |
| --- | --- |
| **Found-text fragments** | [fragment_generator.py](fragment_generator.py): follow `fragment_writer` from sampled DOCX passages to filtered word chunks and a new Word document. |
| **Corpus-based verse** | [generate_texts.py](generate_texts.py): explore word-pair statistics, seed words, and lines arranged into strophes. |
| **Many voices in one text** | [multidocumentmultitypewriter.py](multidocumentmultitypewriter.py): line shuffling, refrains, proper-noun exchange, and vignettes. |
| **Visual collage** | [image_processing_functions.py](image_processing_functions.py): square crops, strips, tiling, and blends through `create_cubomanic`, `create_stripomanic`, and `merge_images`. |
| **Text as image, image as text** | The same image module connects PDF page rendering, visual transformations, and OCR through helpers such as `get_text_from_image`. |

For a wider wander, [text_generating_progs.py](text_generating_progs.py) gathers
stanza and prose experiments, while [poems_from_fragments.py](poems_from_fragments.py)
explores keyword-selected lines and phrase assembly.
[anaphoric writing.py](anaphoric%20writing.py), the essay sketches
([one](essay_generator.py), [two](essay%20generator%202.py)),
[robopoetry_functions.py](robopoetry_functions.py), and
[graphic_text_scratch.py](graphic_text_scratch.py) offer further working notes
and experiments.

## Work with your own material

Think of the scripts as a workshop to adapt: **gather -> extract or crop ->
recombine -> select and edit**.

Start with `fragment_writer` for a compact example. It gathers chunks of 4-14
words from DOCX sources, filters them against an English vocabulary, and
reassembles them into fragments with line breaks. Other routes work with
readable PDF text or JPEG images. Bring a small selection of your own material
and choose the transformation you want to explore.

Before execution, read the chosen script and its helpers, adapt their input,
output, and executable paths, and prepare compatible dependencies in an isolated
Python environment. Imports show what each script uses: text work centers on
`python-docx`, NLTK and its language data, and PyPDF2; visual work adds Pillow,
NumPy/SciPy, with Poppler for PDF rendering and Tesseract for OCR.
**Work on copies in a dedicated folder: some routines move or write files, and
some experiments run when imported.**

Keep track of your source material as you work, then review and credit it when
sharing a composition. The creative choices include the input collection,
constraints, and what you keep from the resulting recombinations.

## Reuse and collaboration

Please contact me if you'd like to collaborate or use these tools in a public or commercial way.

Arrange permission for the code and source material before reuse; this repository
does not include a license granting reuse rights.
