import os

current_directory = os.path.dirname(os.path.abspath(__file__))
txt_file = os.path.join(current_directory, "output.txt")

print(txt_file)