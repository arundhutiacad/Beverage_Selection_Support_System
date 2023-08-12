from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained random forest model from disk
with open('random_forest_model.pkl', 'rb') as f:
    classifier = pickle.load(f)


class Item(BaseModel):
    Calories: float
    Saturated_Fat: float
    Sodium: float
    Dietary_Fibre: float
    Protein: float


@app.post("/predict")
async def predict(item: Item):
    # Extract the features from the request body
    data = [[item.Calories, item.Saturated_Fat, item.Sodium, item.Dietary_Fibre, item.Protein]]

    # Make a prediction using the trained random forest model
    prediction = classifier.predict(data)

    # Return the result as a JSON response
    return {"prediction": prediction[0]}
