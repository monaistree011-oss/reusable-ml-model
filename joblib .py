import joblib
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# 1. Load the 20 Newsgroups dataset (train and test sets)
print('Loading 20 Newsgroups dataset...')
train = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'))
test = fetch_20newsgroups(subset='test', remove=('headers', 'footers', 'quotes'))

# 2. Build the model pipeline
print('Building the Multinomial Naive Bayes model pipeline...')
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# 3. Train the model
print('Training the model...')
model.fit(train.data, train.target)

# 4. Evaluate performance
predicted = model.predict(test.data)
acc = accuracy_score(test.target, predicted)
print(f'Test Accuracy: {acc * 100:.2f}%\n')
print(classification_report(test.target, predicted, target_names=test.target_names))

# 5. Save the trained model to disk
model_filename = '20newsgroups_model.joblib'
joblib.dump(model, model_filename)
print(f'Model saved successfully as {model_filename}')