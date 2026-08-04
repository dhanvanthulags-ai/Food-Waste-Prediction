import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load Dataset
df = pd.read_csv("dataset/foodwastes.csv")
df.columns = df.columns.str.strip()

print("Dataset Loaded Successfully!")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Encode Categorical Columns
label_encoders = {}

categorical_columns = [
    "DAY",
    "MEAL",
    "MENU",
    "WEATHER",
    "SPECIAL EVENT",
    "EXAM"
]

for column in categorical_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

print("\nCategorical columns encoded successfully!")
print(df.head())

# Features and Target
X = df.drop("FOOD WASTED(kg)", axis=1)
y = df["FOOD WASTED(kg)"]

print(X.columns.tolist())

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

# Split Dataset into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\nDataset Split Successfully!")
print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# Create Random Forest Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the Model
model.fit(X_train, y_train)

print("\nRandom Forest Model Trained Successfully!")

# Predict on Test Data
y_pred = model.predict(X_test)

# Evaluate the Model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("------------------------")
print(f"Mean Absolute Error (MAE): {mae:.2f} kg")
print(f"R2 Score: {r2:.2f}")

# Save the trained model
joblib.dump(model, "model/food_waste_model.pkl")

print("\nModel saved successfully!")
print("Location: model/food_waste_model.pkl")

# Save Label Encoders
joblib.dump(label_encoders, "model/label_encoders.pkl")

print("Label Encoders saved successfully!")