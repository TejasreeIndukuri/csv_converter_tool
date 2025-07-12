import pandas as pd

def convert(input_file, output_file):
    df = pd.read_csv(input_file)
    df.to_excel(output_file, index=False)
