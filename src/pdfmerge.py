import sys
import argparse

from pathlib import Path
from typing import Union
from pypdf import PdfMerger, PdfReader

class PDFMerge:
    def __init__(self, filename: str):
        self.filename = filename
        self.merger = PdfMerger()

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.__filename = value

    @property
    def merger(self) -> PdfMerger:
        return self.__merger

    @merger.setter
    def merger(self, value) -> PdfMerger:
        self.__merger = value

    def add_document(self, document: Union[bytearray, PdfReader, str]) -> None:
        self.merger.append(document)

    def write(self) -> None:
        self.merger.write(self.filename)

    def close(self) -> None:
        self.merger.close()

def pdfmerge_main(argv):
    filename = Path(__file__).name

    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("-i", "--input", default=[], nargs='*', required=True, help="Input file(s)")
    argumentParser.add_argument("-o", "--output", required=True, help="PDF output filename")
    argumentParser.add_argument("-v", "--verbose", action="store_true", help="Show whats going on")

    args = argumentParser.parse_args()

    if(args.verbose):
        print(filename, "args=%s" % args)

    try:
        pdf: PDFMerge=PDFMerge(args.output)

        for f in args.input:
            pdf.add_document(f)

        pdf.write()
        pdf.close()
    
    except Exception as ex:
        print(f"{Exception.__name__}({ex.args})")

if __name__ == "__main__":
   pdfmerge_main(sys.argv[1:])