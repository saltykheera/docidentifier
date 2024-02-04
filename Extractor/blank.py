file_path = "business.txt"  


with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()


with open(file_path, 'w', encoding='utf-8') as file:
    file.write('\n'.join(line.strip() for line in lines if line.strip()))
