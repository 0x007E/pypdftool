import unittest

from fpdf import FPDF

from pdfpage import PDFPage
from data.size import Size
from data.format import Format, Orientation, PageType

class TestPdfPage(unittest.TestCase):
    SIZE_W: float = 100
    SIZE_H: float = 100

    def test_init_format_passing(self):
        page: PDFPage = PDFPage(Size(self.SIZE_W, self.SIZE_H))

        self.assertEqual(page.size.width, self.SIZE_W)
        self.assertEqual(page.size.height, self.SIZE_H)

    def test_init_orientation_passing(self):
        for o in Orientation:
            for e in PageType:
                page: PDFPage = PDFPage(Format(PageType(e.value), Orientation(o.value)))
                
                page_size_w: float = page.pdf.w
                page_size_h: float = page.pdf.h

                self.assertEqual(page.size.width, page_size_w)
                self.assertEqual(page.size.height, page_size_h)

    def test_init_failing(self):
        with self.assertRaises(Exception) as ex:
            page: PDFPage = PDFPage(None)
            self.assertTrue(f"Invalid type or value ({Size.__name__} or {Format.__name__} required)" in ex.exception)
            self.assertIsNone(page)

    def test_property_read_pdf_passing(self):
        page: PDFPage = PDFPage(Size(self.SIZE_W, self.SIZE_H))

        self.assertIsNotNone(page.pdf)
        self.assertIsInstance(page.pdf, FPDF)

if __name__ == '__main__':
    unittest.main()
