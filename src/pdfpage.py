import io, os, sys
import argparse
from types import SimpleNamespace
from typing import Union, cast
from pypdf import PdfReader, PdfWriter
import json

from pathlib import Path
from fpdf import FPDF

from data.size import Size
from data.format import Format
from data.text import Text
from data.link import Link
from data.image import Image
from data.rectangle import Rectangle
from data.circle import Circle

class PDFPage:
    def __init__(self, format: Union[Size, Format]):
        self.pdf = FPDF()
        if isinstance(format, Size):
            self.size = format
            self.pdf.add_page(format=(format.width, format.height))
        elif isinstance(format, Format):
            self.pdf.add_page(format=format.pagetype, orientation=format.orientation)
            self.size = Size(self.pdf.w, self.pdf.h)
        else:
            raise Exception(f"Invalid type or value ({Size.__name__} or {Format.__name__} required)")

    @property
    def pdf(self) -> FPDF:
        return self.__pdf
    
    @pdf.setter
    def pdf(self, value) -> FPDF:
        self.__pdf = value

    @property
    def size(self) -> Size:
        return self.__size

    @size.setter
    def size(self, value) -> Size:
        self.__size = value

    def add_text(self, text: Text) -> None:
        self.pdf.set_font(family=text.font.family, size=text.font.size)
        self.pdf.text(text.position.X, text.position.Y, text.text)

    def add_link(self, link: Link) -> None:
        self.pdf.link(link.position.X, link.position.Y, link.size.width, link.size.height, link.link, link.text)

    def add_image(self, image: Image) -> None:
        self.pdf.image(image.path, image.position.X, image.position.Y, image.size.width, image.size.height)

    def add_rectangle(self, rectangle: Rectangle) -> None:
        self.pdf.rect(rectangle.position.X, rectangle.position.Y, rectangle.size.width, rectangle.size.height, rectangle.style.rendering, rectangle.style.corner, rectangle.style.radius)

    def add_circle(self, circle: Circle) -> None:
        self.pdf.circle(circle.position.X, circle.position.Y, circle.radius, circle.style.rendering)

    def create(self, content: object):
        text: Text
        for text in content.text:
            self.add_text(text)
        
        link: Link
        for link in content.link:
            self.add_link(link)

        image: Image
        for image in content.image:
            self.add_image(image)
        
        rectangle: Rectangle
        for rectangle in content.rectangle:
            self.add_rectangle(rectangle)     

        circle: Circle
        for circle in content.circle:
            self.add_circle(circle)    

    def output(self) -> bytearray:
        return self.pdf.output()

    def write(self, filename: str, force: bool=False):
        reader = PdfReader(io.BytesIO(self.output()))
        writer = PdfWriter()
        writer.append_pages_from_reader(reader)

        if(os.path.exists(filename)):
            if(not force):
                raise FileExistsError(filename)

        with open(filename, "wb") as fp:
            writer.write(fp)
        
        writer.close()

def pdfpage_main(argv):
    filename = Path(__file__).name

    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("-c", "--config", required=True, help="JSON configuration file")
    argumentParser.add_argument("-o", "--output", required=True, help="PDF output filename")
    argumentParser.add_argument("-f", "--force", action="store_true", help="Overwrite existing output")
    argumentParser.add_argument("-v", "--verbose", action="store_true", help="Show whats going on")

    args = argumentParser.parse_args()

    if(args.verbose):
        print(filename, "args=%s" % args)

    try:
        if(os.path.exists(args.config)):
            with open(args.config, "rb") as fp:
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
                page.write(args.output, args.force)

        else:
            raise FileNotFoundError(args.config)
        
    except FileNotFoundError as ex:
        print(f"{FileNotFoundError.__name__}({ex.filename})")

    except FileExistsError as ex:
        print(f"{FileExistsError.__name__}({ex.filename}), use -f to force an overwrite")

    except Exception as ex:
        print(f"{Exception.__name__}:{ex.args}")
    
if __name__ == "__main__":
   pdfpage_main(sys.argv[1:])