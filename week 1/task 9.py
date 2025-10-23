import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


np.random.seed(42)

data = {
    'math_score': np.random.randint(40, 100, 100),
    'reading_score': np.random.randint(40, 100, 100),
    'writing_score': np.random.randint(40, 100, 100),
    'hours_studied': np.random.uniform(1, 10, 100),
    'attendance': np.random.randint(60, 100, 100)
}

df = pd.DataFrame(data)
df['passed'] = np.where((df['math_score'] > 50) & (df['attendance'] > 70), 1, 0)

print("Dataset Created Successfully!\n")
print(df.head())

print("\n Basic Statistics:")
print(df.describe())

print("\n Correlation Matrix:")
print(df.corr())

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['math_score'], bins=10, kde=True, color='skyblue')
plt.title('Math Score Distribution')
plt.subplot(1, 2, 2)
sns.scatterplot(x='hours_studied', y='math_score', data=df, hue='passed', palette='coolwarm')
plt.title('Study Hours vs Math Score')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(), annot=True, cmap='viridis')
plt.title('Correlation Heatmap')
plt.show()

X = df[['hours_studied', 'attendance']]
y = df['passed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

print("\nLogistic Regression Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))