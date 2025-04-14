const buttonShowAnimals = document.getElementById("button_show_animals")
const showAnimals = document.getElementById("show_animals")
const buttonAddNewAnimal = document.getElementById("addnew_animals");

// buttonShowAnimals.addEventListener("click", () => {
//     fetch("http://127.0.0.1:3000/tiere", )
//     .then(res => res.json())
//     .then(data => displayData(data))

//     function displayData(data) {
//         console.log(data)
//     }
// });

buttonShowAnimals.addEventListener("click", async () => {
    const res = await fetch("http://127.0.0.1:3000/tiere")
    displayData(await res.json())

    function displayData(data) {
        console.log(data)
        showAnimals.innerHTML = "";
        data.forEach(tier => {
            console.log(tier)
            const li = document.createElement("li");
            li.textContent = tier.name;
            showAnimals.appendChild(li);
        });
    }
});

buttonAddNewAnimal.addEventListener("click", async () => {
    const tierart = document.getElementById("tierart").value;
    const name = document.getElementById("animalName").value;
    const krankheit = document.getElementById("krankheit").value;
    const alter = document.getElementById("animalAlter").value;
    const gewicht = document.getElementById("gewicht").value;

    const neuesTier = {
        art: tierart,
        name: name,
        krankheit: krankheit,
        alter: alter,
        gewicht: gewicht
    };


    const res = await fetch("http://127.0.0.1:3000/tiere", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(neuesTier)
    });;

});

