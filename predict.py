
%%writefile predict.py
import io
import joblib
import requests

MODEL_URL = "https://raw.githubusercontent.com/monaistree011-oss/reusable-ml-model/main/20newsgroups_model.joblib"

print("Fetching trained model directly from GitHub...")
try:
    response = requests.get(MODEL_URL)
    response.raise_for_status()

    model_bytes = io.BytesIO(response.content)
    model = joblib.load(model_bytes)
    print("Model loaded successfully into memory!\n")

    new_samples = [
        "The local team won the championship game in overtime last night.",
        "Scientists have discovered a new planet orbiting a distant star using the Hubble telescope.",
        "My computer's graphics card is overheating when I try to boot up the operating system."
    ]

    predictions = model.predict(new_samples)

    print("--- Prediction Results ---")
    for text, pred in zip(new_samples, predictions):
        print(f"Text: '{text}'")
        print(f"Predicted Category ID: {pred}\n")

except requests.exceptions.RequestException as e:
    print(f"Error fetching model from GitHub: {e}")
except Exception as e:
    print(f"An error occurred while loading or running the model: {e}")