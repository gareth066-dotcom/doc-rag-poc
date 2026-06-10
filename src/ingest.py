from pathlib import Path
from extractor_factory import ExtractorFactory

DATA_FOLDER = Path("data")
OUTPUT_FILE = Path("extracted/content.txt")

all_content = []

for file in DATA_FOLDER.iterdir():

    if file.is_file():

        try:

            extractor = ExtractorFactory.get(
                file.name
            )

            content = extractor.extract(file)

            all_content.append(
                f"\n\n===== {file.name} =====\n\n"
            )

            all_content.append(content)

            print(f"Processed {file.name}")

        except Exception as e:

            print(
                f"Failed {file.name}: {e}"
            )

OUTPUT_FILE.write_text(
    "\n".join(all_content),
    encoding="utf-8"
)

print("Done")