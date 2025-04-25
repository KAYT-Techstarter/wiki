import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

function Tierliste() {
  const { id } = useParams();
  const [tier, setTier] = useState();

  useEffect(() => {
    async function getTierDetails() {
      const res = await fetch(`http://localhost:5005/Tiere/${id}`);
      const data = await res.json();
      setTier(data);
    }

    getTierDetails();
  }, []);

  if (!tier) {
    return <p>Lade Tierdaten...</p>;
  }

  return (
    <div>
      <h1>{tier.name}</h1>
      <h2>Art: {tier.tierart}</h2>
      <h2>Alter: {tier.geburtstag}</h2>
      <h2>Gewicht: {tier.gewicht}</h2>
      <h2>Krankheit: {tier.krankheit}</h2>
    </div>
  );
}

export default Tierliste;

