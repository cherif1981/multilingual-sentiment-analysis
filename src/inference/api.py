from fastapi import FastAPI
app = FastAPI()

@app.post("/predict")
def predict(text: str):
    return {"sentiment": "positive"}
