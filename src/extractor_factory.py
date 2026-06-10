from extractors.pdf_extractor import PdfExtractor
from extractors.docx_extractor import DocxExtractor
from extractors.pptx_extractor import PptxExtractor
from extractors.csv_extractor import CsvExtractor
from extractors.xlsx_extractor import XlsxExtractor

class ExtractorFactory:

    @staticmethod
    def get(file_name):

        file_name = file_name.lower()

        if file_name.endswith(".pdf"):
            return PdfExtractor()

        if file_name.endswith(".docx"):
            return DocxExtractor()

        if file_name.endswith(".pptx"):
            return PptxExtractor()

        if file_name.endswith(".csv"):
            return CsvExtractor()

        if file_name.endswith(".xlsx"):
            return XlsxExtractor()

        raise Exception(
            f"Unsupported file type: {file_name}"
        )