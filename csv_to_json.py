import pandas as pd

def convert(input_file, output_file):
    df = pd.read_csv(input_file)
    df.to_json(output_file, orient='records', indent=2)
