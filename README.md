[![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1%20Beta-orange.svg)](https://github.com/0x007e) [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
# Small Python PDF creation/manipulation tool

This python scripts can be used with command line or as import from another script.

## PDFpage

Create a PDF from a JSON config file. For additional information call:

``` bash
python ./pdfpage.py -h
```

| Short | Expand    | Description           |
|-------|-----------|-----------------------|
| -h    | --help    | Help menu             |
| -v    | --verbose | Enable verbosity      |
| -c    | --config  | Configuration file    |
| -o    | --output  | Output PDF file       |
| -f    | --force   | Overwrite output file |

### CLI-Usage

``` bash
# Do not overwrite Test.pdf
python ./pdfpage.py -c ./pdf.page.json -o ./Test.pdf

# Overwrite Test.pdf
python ./pdfpage.py -c ./pdf.page.json -o ./Test.pdf -f
```
### Python usage

``` python
# Create a blank page
page = PDFPage(Size(200, 200))

# Add a text
text.position = Position(10, 10)
text.font = Font("Times", 10)
text.text = "Test"

# Add a link  
link.position = Position(10,20)
link.size = Size(10, 10)
link.link = "https://github.com/0x007e"
link.text = "0x007e GitHub account"

# Add an image
image.position = Position(10,20)
image.size = Size(10, 10)
image.path = "./Test.png"
image.text = "Test image"

# Add a rectangle
rectangle.style = RectangleStyle(Rendering.D)
rectangle.position = Position(10,20)
rectangle.size = Size(10, 10)

page.add_text(text)
```

## PDFoverlay

Overlay a PDF page in a PDF document

``` bash
python ./pdfoverlay.py -h
```

| Short | Expand    | Description           |
|-------|-----------|-----------------------|
| -h    | --help    | Help menu             |
| -v    | --verbose | Enable verbosity      |
| -i    | --input   | PDF document          |
| -l    | --overlay | Overlay PDF page      |
| -o    | --output  | Output PDF file       |
| -p    | --pages   | Pages where overlay page should be layed on empty or 0=all pages |

### CLI-Usage

``` bash
# Overlay page on all document pages
python ./pdfoverlay.py -i ./Document.pdf -l Overlay.pdf -o ./DO.pdf

# Overlay page on selected document pages
python ./pdfoverlay.py -i ./Document.pdf -l Overlay.pdf -o ./DO.pdf -p 1 3 4 8
```
### Python usage

``` python
pdf: PDFOverlay=PDFOverlay("Document.pdf")

# All pages
pdf.add_overlay("Overlay.pdf")
pdf.add_overlay("Overlay.pdf", [ 0 ])

# Selected pages
pdf.add_overlay("Overlay.pdf", [ 1, 3, 6, 8 ])

# Write to Document
pdf.write(args.output)
```

## PDFmerge

Merge PDF pages into one document

``` bash
python ./pdfmerge.py -h
```

| Short | Expand    | Description           |
|-------|-----------|-----------------------|
| -h    | --help    | Help menu             |
| -i    | --input   | PDF documents         |
| -o    | --output  | Output PDF file       |

### CLI-Usage

``` bash
python ./pdfmerge.py -i ./Document1.pdf ./Document2.pdf -o ./Document.pdf
```
### Python usage

``` python
pdf: PDFMerge=PDFMerge("Document.pdf")

pdf.add_document("Document1.pdf")
pdf.add_document("Document2.pdf")
# ...
pdf.add_document("Documentn.pdf")

pdf.write()
pdf.close()
```
