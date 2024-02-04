def insert_newline(file_path, words_per_line=20):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
        return
    except UnicodeDecodeError:
        print(f"Error decoding file at path {file_path}. Try specifying a different encoding.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    words = content.split()
    lines = [' '.join(words[i:i + words_per_line]) for i in range(0, len(words), words_per_line)]
    result = '\n'.join(lines)

   
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(result)

    return result


file_path = "business.txt"
insert_newline(file_path, words_per_line=10)
