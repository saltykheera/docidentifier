import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import PyPDF2

nlp = spacy.load("en_core_web_sm")



# Reading content from "creative.txt" and creating DataFrame
with open("creative.txt", 'r', encoding="utf-8") as file:
    creative_content = file.read()

creative_lines = creative_content.split('\n')
df_creative = pd.DataFrame(creative_lines, columns=['Column_Name'])

# Reading content from "government.txt" and creating DataFrame
with open("government.txt", 'r', encoding="utf-8") as file:
    government_content = file.read()

government_lines = government_content.split('\n')
df_government = pd.DataFrame(government_lines, columns=['Column_Name'])

#legal document
with open("legal.txt", 'r', encoding="utf-8") as file:
    legal_content = file.read()

legal_lines = legal_content.split('\n')
df_legal = pd.DataFrame(legal_lines, columns=['Column_Name'])

#medical document 
with open("medical.txt", 'r', encoding="utf-8") as file:
    medical_content = file.read()

medical_lines = medical_content.split('\n')
df_medical = pd.DataFrame(medical_lines, columns=['Column_Name'])



# Business document
with open("business.txt", 'r', encoding="utf-8") as file:
    business_content = file.read()

business_lines = business_content.split('\n')
df_business = pd.DataFrame(business_lines, columns=['Column_Name'])

# News document
with open("news.txt", 'r', encoding="utf-8") as file:
    news_content = file.read()

news_lines = news_content.split('\n')
df_news = pd.DataFrame(news_lines, columns=['Column_Name'])

# Manuals document
with open("manuals.txt", 'r', encoding="utf-8") as file:
    manuals_content = file.read()

manuals_lines = manuals_content.split('\n')
df_manuals = pd.DataFrame(manuals_lines, columns=['Column_Name'])

# Research document
with open("research.txt", 'r', encoding="utf-8") as file:
    research_content = file.read()

research_lines = research_content.split('\n')
df_research = pd.DataFrame(research_lines, columns=['Column_Name'])






#TRAINING DATA
training_data = [
    (df_creative, "creative"),
    (df_news, "news"),
    (df_legal, "legal"),
    (df_business, "business"),
    (df_medical, "medical"),
    (df_manuals, "manuals"),
    (df_research, "research"),
    (df_government,"government")
]

# Tokenizing and lemmatizing the training data
X_train = [' '.join([token.lemma_ for token in nlp(sentence)]) for df, _ in training_data for sentence in df['Column_Name']]
y_train = [category for df, category in training_data for _ in df['Column_Name']]


# Create a text classification model pipeline
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X_train, y_train)


# creating the gui reading the data
def open_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("PDF files", "*.pdf")])
    current_directory = os.path.dirname(os.path.abspath(__file__))
    txt_file = os.path.join(current_directory, "output.txt")
    
    
    if file_path:
        prediction_file=None
        try:
            with open(file_path, 'rb') as file:
                pdf_reader= PyPDF2.PdfReader(file)
                with open(txt_file,"w",encoding="utf-8") as t_file:
                    for page in range(len(pdf_reader.pages)):
                        page=pdf_reader.pages[page]
                        text=page.extract_text()
                        t_file.write(text)
                    
                
            with open(txt_file,"r",encoding='utf-8') as r_file:
                content=r_file.read()       

            processed_sent = " ".join([token.lemma_ for token in nlp(content)])
            prediction_file = model.predict([processed_sent])[0]

            file_name = os.path.basename(file_path)
            file_name_label.config(text=f"Selected File: {file_name}\nCategory: {prediction_file}")

        except FileNotFoundError:
            print(f"File not found at path: {file_path}")
        except Exception as e:
            print(f"Error reading file: {e}")


root = tk.Tk()
root.title("PRINT")


root.geometry("400x200")  


file_name_label = tk.Label(root, text="Selected File: None")
file_name_label.pack(pady=10)


image = Image.open("printer.png")
image = image.resize((50, 50))  
image_with_padding = Image.new('RGBA', (60, 60), (255, 255, 255, 0))  
image_with_padding.paste(image, (5, 5))

photo = ImageTk.PhotoImage(image_with_padding)


open_button = tk.Button(root, image=photo, command=open_file, bd=1,relief="solid") 
open_button.image = photo  
open_button.pack(pady=10)


root.mainloop()
