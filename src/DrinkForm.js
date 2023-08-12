import React, { useState } from 'react';
import './DrinkForm.css';

function DrinkForm() {
  const [saturatedFat, setSaturatedFat] = useState(0);
  const [dietaryFibre, setDietaryFibre] = useState(0);
  const [sodium, setSodium] = useState(0);
  const [calories, setCalories] = useState(0);
  const [protein, setProtein] = useState(0);
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch('http://127.0.0.1:8000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        Saturated_Fat: saturatedFat,
        Dietary_Fibre: dietaryFibre,
        Sodium: sodium,
        Calories: calories,
        Protein: protein
      })
    });
    const data = await response.json();
    setPrediction(data.prediction);
  }

  return (
    <div className="container">
      <header>
        <h1>Beverage Recommender</h1>
      </header><br/>
      <form onSubmit={handleSubmit}>
        <label>
          Fat (g):
          <div className="slider-container">
            <span className="min-label">{0}</span>
            <input
              type="range"
              min="0"
              max="0.3" // Set the maximum value to 0.3
              step="0.01" // Set the step to 0.01 for more accurate increments
              value={saturatedFat}
              onChange={e => setSaturatedFat(e.target.value)}
            />
            <span className="max-label">{0.3}</span>
          </div>
          <br />
          <input
            type="text"
            value={saturatedFat}
            onChange={e => setSaturatedFat(e.target.value)}
          />
        </label>
        <label>
          Dietary Fibre (g):
          <div className="slider-container">
            <span className="min-label">{0}</span>
            <input
              type="range"
              min="0"
              max="8"
              value={dietaryFibre}
              onChange={e => setDietaryFibre(e.target.value)}
            />
            <span className="max-label">{8}</span>
          </div>
          <br />
          <input
            type="text"
            value={dietaryFibre}
            onChange={e => setDietaryFibre(e.target.value)}
          />
        </label>
        <label>
          Sodium (mg):
          <div className="slider-container">
            <span className="min-label">{0}</span>
            <input
              type="range"
              min="0"
              max="40"
              value={sodium}
              onChange={e => setSodium(e.target.value)}
            />
            <span className="max-label">{40}</span>
          </div>
          <br />
          <input
            type="text"
            value={sodium}
            onChange={e => setSodium(e.target.value)}
          />
        </label>
        <label>
          Calories:
          <div className="slider-container">
            <span className="min-label">{0}</span>
            <input
              type="range"
              min="0"
              max="510"
              value={calories}
              onChange={e => setCalories(e.target.value)}
            />
            <span className="max-label">{510}</span>
          </div>
          <br />
          <input
            type="text"
            value={calories}
            onChange={e => setCalories(e.target.value)}
          />
        </label>
        <label>
          Protein (g):
          <div className="slider-container">
            <span className="min-label">{0}</span>
            <input
              type="range"
              min="0"
              max="20s"
              value={protein}
              onChange={e => setProtein(e.target.value)}
            />
            <span className="max-label">{100}</span>
          </div>
          <br />
          <input
            type="text"
            value={protein}
            onChange={e => setProtein(e.target.value)}
          />
        </label>
        <br />
        <input type="submit" value="Submit" />
      </form>
      {prediction && (
        <div className="result-box">
          Recommendation: {prediction}
        </div>
      )}
    </div>
  );
}

export default DrinkForm;
