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
        <img src="starbuckslogo.png" alt="Logo" /><br/>
        <h1>Starbucks Drink Recommender</h1>
      </header>
      <form onSubmit={handleSubmit}>
        <label>
          Saturated Fat:
          <input
            type="range"
            min="0"
            max="3"
            value={saturatedFat * 10}
            onChange={e => setSaturatedFat(e.target.value / 10)}
          />
          <input
            type="number"
            value={saturatedFat}
            onChange={e => setSaturatedFat(e.target.value)}
          />
        </label>
        <br />
        <label>
          Dietary Fibre:
          <input
            type="range"
            min="0"
            max="8"
            value={dietaryFibre}
            onChange={e => setDietaryFibre(e.target.value)}
          />
          <input
            type="text"
            value={dietaryFibre}
            onChange={e => setDietaryFibre(e.target.value)}
          />
        </label>
        <br />
        <label>
          Sodium:
          <input
            type="range"
            min="0"
            max="40"
            value={sodium}
            onChange={e => setSodium(e.target.value)}
          />
          <input
            type="text"
            value={sodium}
            onChange={e => setSodium(e.target.value)}
          />
        </label>
        <br />
        <label>
          Calories:
          <input
            type="range"
            min="0"
            max="510"
            value={calories}
            onChange={e => setCalories(e.target.value)}
          />
          <input
            type="text"
            value={calories}
            onChange={e => setCalories(e.target.value)}
          />
        </label>
        <br />
        <label>
          Protein:
          <input
            type="range"
            min="0"
            max="20s"
            value={protein}
            onChange={e => setProtein(e.target.value)}
          />
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
