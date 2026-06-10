import pandas as pd

class XlsxExtractor:

    def extract(self, file_path):

        excel = pd.ExcelFile(file_path)

        output = []

        for sheet in excel.sheet_names:

            df = pd.read_excel(
                file_path,
                sheet_name=sheet
            )

            output.append(f"Sheet: {sheet}")
            output.append(df.to_string(index=False))

        return "\n".join(output)