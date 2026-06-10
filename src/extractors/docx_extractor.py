from docx import Document

class DocxExtractor:

    def extract(self, file_path):

        doc = Document(file_path)

        text = []

        for p in doc.paragraphs:

            if p.text.strip():
                text.append(p.text)

        return "\n".join(text)