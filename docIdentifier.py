import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd
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

# Reading user file data
file_path = input("Enter the path to the file: ")

try:
    with open(file_path, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
except Exception as e:
    print(f"Error reading file: {e}")

processed_sent=" ".join([token.lemma_ for token in nlp(content)])
prediction_file = model.predict([processed_sent])[0]
print(f"The document belongs to the category of: {prediction_file}")