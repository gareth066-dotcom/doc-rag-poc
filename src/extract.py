from pypdf import PdfReader
from pathlib import Path

pdf = Path("data/Hydro-Bush-Datasheet.pdf")

reader = PdfReader(pdf)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"

Path("extracted/content.txt").write_text(
    text,
    encoding="utf-8"
)

print("Extraction complete")