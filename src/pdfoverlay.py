import os, sys
import argparse

from pathlib import Path
from typing import Union
from pypdf import PdfReader, PdfWriter, Transformation

class PDFOverlay:
    def __init__(self, filename: str):
        self.filename = filename
        self.reader = PdfReader(filename)

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        if(os.path.exists(value)):
            self.__filename = value
        else:
            raise FileNotFoundError(value)

    @property
    def reader(self) -> PdfReader:
        return self.__reader

    @reader.setter
    def reader(self, value) -> PdfReader:
        self.__reader = value

    def add_overlay(self, overlayorpath: Union[bytearray, str], pagenumber: int=[ 0 ]) -> None:
        page_overlay = PdfReader(overlayorpath).pages[0]

        if(0 in pagenumber):
            for page in self.reader.pages:
                page.merge_page(page2=page_overlay)
        else:
            i: int=0

            for page in self.reader.pages:

                i += 1

                if(i in pagenumber):
                    page.merge_page(page2=page_overlay)

    def add_watermark(self, watermarkorpath: Union[bytearray, str], pagenumber: int=[ 0 ], over=False):
        page_watermark = PdfReader(watermarkorpath).pages[0]

        if(0 in pagenumber):
            for page in self.reader.pages:
                page.merge_transformed_page(page_watermark, Transformation(), over)
        else:
            i: int=0

            for page in self.reader.pages:

                i += 1

                if(i in pagenumber):
                    page.merge_transformed_page(page_watermark, Transformation(), over)


    def write(self, filename: str) -> None:
        writer = PdfWriter()
        writer.append_pages_from_reader(self.reader)

        with open(filename, "wb",) as fp:
            writer.write(fp)
        
        writer.close()

def pdfoverlay_main(argv):
    filename = Path(__file__).name

    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("-i", "--input", required=True, help="PDF file")
    argumentParser.add_argument("-p", "--page", required=True, help="Overlay PDF file")
    argumentParser.add_argument("-n", "--numbers", default=[], nargs='+', type=int, required=False, help="Overlay Pages")
    argumentParser.add_argument("-o", "--output", required=True, help="PDF output filename")
    argumentParser.add_argument("-v", "--verbose", action="store_true", help="Show whats going on")
    argumentParser.add_argument("-w", "--watermark", action="store_true", help="Add as watermark")

    args = argumentParser.parse_args()

    if(args.verbose):
        print(filename, "args=%s" % args)

    try:
        if(not args.numbers):
            args.numbers = [ 0 ]

        pdf: PDFOverlay=PDFOverlay(args.input)

        if(args.watermark):
            pdf.add_watermark(args.page, args.numbers)
        else:
            pdf.add_overlay(args.page, args.numbers)
        pdf.write(args.output)

    except FileNotFoundError as ex:
        print(f"{Exception.__name__}({ex.filename})")

    except Exception as ex:
        print(f"{Exception.__name__}({ex.args})")
        

if __name__ == "__main__":
   pdfoverlay_main(sys.argv[1:])