import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. LOAD DATASET (Using a sample dictionary for demonstration)
# In a real scenario, you would use: data = pd.read_csv('phishing_emails.csv')
data_dict = {
    'text': [
        "Urgent: Your account is locked. Click here to verify",
        "Free gift card inside! Claim your prize now",
        "Meeting scheduled for tomorrow at 10 AM",
        "Update your payment details immediately",
        "The project report is attached for your review",
        "Win a million dollars in our lottery!"
    ],
    'label': [1, 1, 0, 1, 0, 1]  # 1 = Phishing, 0 = Safe
}
df = pd.DataFrame(data_dict)

# 2. FEATURE EXTRACTION (Text to Numbers)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# 3. SPLIT DATA (Training and Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. TRAIN THE MODEL
model = MultinomialNB()
model.fit(X_train, y_train)

# 5. EVALUATE
y_pred = model.predict(X_test)
print("--- Phishing Detection Results ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100}%")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 6. TEST WITH NEW EMAIL
def test_email(email_text):
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)
    return "PHISHING" if prediction[0] == 1 else "SAFE"

print("\n--- Live Test ---")
sample_mail = input("Enter an email subject/body to check: ")
print(f"Result: {test_email(sample_mail)}")

input("\nPress Enter to exit...")