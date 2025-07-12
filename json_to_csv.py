import pandas as pd

def convert(input_file, output_file):
    df = pd.read_json(input_file)
    df.to_csv(output_file, index=False)
