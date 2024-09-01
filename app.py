import streamlit as st
import pickle

tfidf = pickle.load(open('/content/drive/MyDrive/Colab Notebooks/vectorizer.pkl','rb'))
model = pickle.load(open('/content/drive/MyDrive/Colab Notebooks/model.pkl', 'rb'))

from nltk.corpus import stopwords
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
#stemming
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def transform_text(text):
  #lowering case
  text = text.lower()
  #tokenization
  text = nltk.word_tokenize(text)

  #removing special characters
  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)

  text = y[:]   #cloning 
  y.clear()

  #removing stopword and punctuation
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))


  return " ".join(y)


st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message brother")
# input_sms = "Enter the message brother"

if st.button("Predict"):
  #1. Preprocess the msge

  transform_sms = transform_text(input_sms)

  # print("thisa is tsms",transform_sms)
  #2. Vectorize

  vector_input = tfidf.transform([transform_sms])
  # print("this is vct: ", vector_input)

  #3. Predict

  result = model.predict(vector_input)[0]

  #4. Display

  if result ==1:
    st.header("Spam")

  else:
    st.header("Not Spam")
  
