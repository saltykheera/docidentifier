import pandas as pd


df = pd.read_csv("news.csv")  


column_name = "Heading"  


content_string = '\n'.join(df[column_name].astype(str))


output_file_path = "news.txt" 
with open(output_file_path, 'a', encoding='utf-8') as output_file:
    output_file.write(content_string)
