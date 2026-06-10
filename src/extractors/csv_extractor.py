import pandas as pd

class CsvExtractor:

    def extract(self, file_path):

        df = pd.read_csv(file_path)

        return df.to_string(index=False)