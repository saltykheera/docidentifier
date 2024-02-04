file_path = "medical.txt"  


with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()


unique_words = set()
result = []
for line in lines:
    words = line.strip().split()
    unique_line = ' '.join(word for word in words if word not in unique_words)
    result.append(unique_line)
    unique_words.update(words)


with open(file_path, 'w', encoding='utf-8') as file:
    file.write('\n'.join(result))


# Read content from the file
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Remove blank spaces and write the cleaned content back to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write('\n'.join(line.strip() for line in lines if line.strip()))
