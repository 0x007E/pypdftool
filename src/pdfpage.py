import io
import os, sys
import argparse
from types import SimpleNamespace
from pypdf import PdfReader, PdfWriter
import json

from pathlib import Path
from fpdf import FPDF

from drawing.position import Position
from drawing.size import Size
from data.text import Text
from data.link import Link
from data.image import Image
from data.rectangle import Rectangle

class PDFPage:
    def __init__(self, size: Size):
        self.size = size
        self.pdf = FPDF()
        self.pdf.add_page(format=(size.width, size.height))

    @property
    def pdf(self) -> FPDF:
        return self.__pdf
    
    @pdf.setter
    def pdf(self, value):
        self.__pdf = value

    @property
    def size(self) -> Size:
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def add_text(self, text: Text):
        self.pdf.set_font(family=text.font.family, size=text.font.size)
        self.pdf.text(text.position.X, text.position.Y, text.text)

    def add_link(self, link: Link):
        self.pdf.link(link.position.X, link.position.Y, link.size.width, link.size.height, link.link, link.text)

    def add_image(self, image: Image):
        self.pdf.image(image.path, image.position.X, image.position.Y, image.size.width, image.size.height)

    def add_rectangle(self, rectangle: Rectangle):
        self.pdf.rect(rectangle.position.X, rectangle.position.Y, rectangle.size.width, rectangle.size.height, rectangle.style.rendering, rectangle.style.corner, rectangle.style.radius)

    def create(self):
        return self.pdf.output()

def pdfpage_main(argv):
    filename = Path(__file__).name

    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("-c", "--config", required=True, help="JSON configuration file")
    argumentParser.add_argument("-o", "--output", required=True, help="PDF output filename")
    argumentParser.add_argument("-f", "--force", action="store_true", help="Overwrite existing output")
    
    args = argumentParser.parse_args()
    print(filename, "args=%s" % args)

    try:
        if(os.path.exists(args.config)):
            with open(args.config, "rb")as fp:
                config = json.loads(fp.read(), object_hook=lambda d: SimpleNamespace(**d)) 
                
                page = PDFPage(Size(config.width, config.height))

                text: Text
                for text in config.content.text:
                    page.add_text(text)

                link: Link
                for link in config.content.link:
                    page.add_link(link)

                image: Image
                for image in config.content.image:
                    page.add_image(image)

                rectangle: Rectangle
                for rectangle in config.content.rectangle:
                    page.add_rectangle(rectangle)

                reader = PdfReader(io.BytesIO(page.create()))
                writer = PdfWriter()
                writer.append_pages_from_reader(reader)

                if(os.path.exists(args.output)):
                    if(not args.force):
                        raise FileExistsError(args.output)

                with open(args.output, "wb") as fp:
                    writer.write(fp)
                
                writer.close()

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