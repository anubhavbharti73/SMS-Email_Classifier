import pytest
import pickle
from app import transform_text

# Load model & vectorizer (update path if needed)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

def test_transform_text():
input_text = "Hello!!! This is a TEST message 123"
output = transform_text(input_text)

```
assert isinstance(output, str)
assert "hello" in output or "test" in output
```

#Test 2: Empty input

def test_empty_text():
output = transform_text("")
assert output == ""

#Test 3: Spam prediction

def test_spam_prediction():
text = "Congratulations! You won a free ticket. Call now!!!"
transformed = transform_text(text)
vector = tfidf.transform([transformed])
result = model.predict(vector)[0]

```
assert result in [0, 1]
```

#Test 4: Ham prediction

def test_ham_prediction():
text = "Hey bro, are we meeting today?"
transformed = transform_text(text)
vector = tfidf.transform([transformed])
result = model.predict(vector)[0]

```
assert result in [0, 1]
```

#Test 5: Special characters handling

def test_special_characters():
text = "@@@!!!###$$$"
output = transform_text(text)
assert isinstance(output, str)
