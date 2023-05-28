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
# Create a blank page with size
page = PDFPage(Size(200, 200))

# Or create a blank page with format
page = PDFPage(Format(PageType.A4, Orientation.P))

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

# Get output as byte array
arr: bytearray = page.output()

# Or write pdf page
page.write("Output.pdf")
```

#### Create from JSON file

``` json
{
    "size": {
        "width": 100.22,
        "height": 150.22
    },
    "format": {
        "pagetype": "A4",
        "orientation": "L"
    },
    "content": {
        "text": [
            {
                "font": {
                    "family": "Times",
                    "size": 10
                },
                "position": {
                    "X": 10,
                    "Y": 9
                },
                "text": "Test"
            }
        ],
        "link": [
            {
                "link": "https://github.com/sunriax",
                "text": "Test",
                "position": {
                    "X": 10,
                    "Y": 10
                },
                "size": {
                    "width": 10,
                    "height": 10
                }
            }
        ],
        "image": [
            {
                "path": "./Test.png",
                "position": {
                    "X": 10,
                    "Y": 10
                },
                "size": {
                    "width": 50,
                    "height": 50
                }
            }
        ],
        "rectangle": [
            {
                "position": {
                    "X": 10,
                    "Y": 10
                },
                "size": {
                    "width": 50,
                    "height": 50
                },
                "style": {
                    "rendering": "D",
                    "corner": false,
                    "radius": 0
                }
            }
        ]
    }
}
```

> Use size or format

``` python
with open("data.json", "rb") as fp:
    config = json.loads(fp.read(), object_hook=lambda d: SimpleNamespace(**d)) 

    if(hasattr(config, f"{Size.__name__.lower()}")):
        size: Size = Size(config.size.width, config.size.height)
        page = PDFPage(size)
    elif(hasattr(config, f"{Format.__name__.lower()}")):
        format: Format = Format(config.format.pagetype, config.format.orientation)
        page = PDFPage(format)
    else:
        raise NameError(args.config)

    page.create(config.content)
    page.write("Test.pdf", False)
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
