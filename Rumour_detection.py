from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
CORS(app)

# Load the true and fake news datasets
true_data = pd.read_csv('../data/Book2.csv', encoding='latin1')
fake_data = pd.read_csv('../data/Book1.csv', encoding='latin1')

# Remove NaN values from the 'title' column
true_data = true_data.dropna(subset=['title'])
fake_data = fake_data.dropna(subset=['title'])

# Lowercase the title columns
true_data['title'] = true_data['title'].str.lower()
fake_data['title'] = fake_data['title'].str.lower()

# Concatenate the true and fake news titles
all_titles = pd.concat([true_data['title'], fake_data['title']])

# Initialize and fit the vectorizer
vectorizer = TfidfVectorizer()
vectorizer.fit(all_titles)

# Transform the titles into feature vectors
X_true = vectorizer.transform(true_data['title'])
X_fake = vectorizer.transform(fake_data['title'])

# Create target labels
y_true = pd.Series([1] * X_true.shape[0])  # True news is labeled as 1
y_fake = pd.Series([0] * X_fake.shape[0])  # Fake news is labeled as 0

# Concatenate the true and fake news feature vectors and labels
X = pd.concat([pd.DataFrame(X_true.toarray()), pd.DataFrame(X_fake.toarray())], ignore_index=True)
y = pd.concat([y_true, y_fake], ignore_index=True)

# Initialize and train the classifiers
RFC = RandomForestClassifier(random_state=0)
RFC.fit(X, y)

GBC = GradientBoostingClassifier(random_state=0)
GBC.fit(X, y)

DT = DecisionTreeClassifier(random_state=0)
DT.fit(X, y)

LR = LogisticRegression(random_state=0)
LR.fit(X, y)

def classify_news(news):
    news = news.lower()
    news_vector = vectorizer.transform([news])

    pred_RFC = RFC.predict(news_vector)[0]
    pred_GBC = GBC.predict(news_vector)[0]
    pred_DT = DT.predict(news_vector)[0]
    pred_LR = LR.predict(news_vector)[0]

    if (pred_RFC == 0) and (pred_GBC == 0) and (pred_DT == 0) and (pred_LR == 0):
        return {"result": "It is a Fake News!", "text": fake_data.loc[fake_data['title'].str.lower() == news]['text'].iloc[0], "date": fake_data.loc[fake_data['title'].str.lower() == news]['date'].iloc[0]}
    elif (pred_RFC == 1) and (pred_GBC == 1) and (pred_DT == 1) and (pred_LR == 1):
        return {"result": "True News", "text": true_data.loc[true_data['title'].str.lower() == news]['text'].iloc[0], "date": true_data.loc[true_data['title'].str.lower() == news]['date'].iloc[0]}
    else:
        return {"result": "This news does not exist in the dataset."}

@app.route('/check_news', methods=['POST'])
def check_news():
    news = request.json.get('news')
    result = classify_news(news)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)  # Run Flask app on port 5000

