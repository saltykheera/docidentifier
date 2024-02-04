import json

file_path = "your_json_file.json" 
output_file_path = "headlines.txt"  


with open(file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)


headlines = [entry['headline'] for entry in data]
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(headlines))
