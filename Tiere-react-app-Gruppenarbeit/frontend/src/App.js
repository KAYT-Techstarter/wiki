import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from "react";

// 2. Tiere-Liste im Frontend:
// Holt euch alle Tiere vom Backend (GET /tiere)
// Zeigt sie im Frontend an – z.B. nur Tierart und Name

function App() {
  const [animals, setAnimals] = useState([]);

  useEffect(() => {
    const urlListe = [];
    async function getAnimals() {
      const res = await fetch(
        "http://localhost:5005/tiere"
      );
      const data = await res.json();

      setAnimals(data)
    }

    getAnimals()
  }, []);

  return (
    <div>
      {animals.map((animal) => (
        <h1>{animal.name}-{animal.tierart}</h1>
      ))}
    </div>
  );
}

export default App;
