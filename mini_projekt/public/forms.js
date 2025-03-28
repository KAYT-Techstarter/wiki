// Dynamische Dropdowns für Bans, Skins, Elo
const bansOptions = ["Milio", "Warwick", "Lulu", "Diana", "Yummi", "Mordekaiser", "Viktor", "Tresh", "Diana", "Warwick"];
const skinsOptions = ["Coven Camille", "Warden Nautilus", "Default Lissandra", "Soul Fighter Samira", "Lunar Eclipse Leona", "Augmented Singed", "Arcade Viego", "Little Demon Tristana", "PROJECT: Lucian", "Prestige Splendid Staff Nami + Border"];
const eloOptions = ["Sovereign", "Challenger Master", "Master", "Diamond", "Platinum", "Gold", "Silver", "Bronze"];

function createEloDropdowns() {
   const container = document.getElementById("elo");
  container.innerHTML = ""; // Leeren, falls bereits Elemente existieren

    for (let i = 0; i < 3; i++) {  // Maximal 3 Dropdowns
        const div = document.createElement("div");
        div.style.display = "flex";
        div.style.alignItems = "center";
        div.style.gap = "10px"; // Abstand zwischen Dropdown & Bild

        const select = document.createElement("select");
        select.setAttribute("data-index", i);
        select.innerHTML = `<option value="">Bitte wählen...</option>` +
        eloOptions.map(option => `<option value="${option}">${option}</option>`).join("");

        const img = document.createElement("img");
        img.src = "images/default.png"; // Standardbild
        img.width = 80;
        img.height = 80;
        img.alt = "Rank Icon";

        select.addEventListener("change", function () {
          updateRankIcon(select, img);
        });

        div.appendChild(select);
        div.appendChild(img);
        container.appendChild(div);
    }
}

function updateRankIcon(selectElement, imgElement) {
    const rankImages = {
        "Sovereign": "images/Sovereign.png",
        "Challenger Master": "images/Challenger.png",
        "Master": "images/Master.png",
        "Diamond": "images/Diamond.png",
        "Platinum": "images/Platinum.png",
        "Gold": "images/Gold.png",
        "Silver": "images/Silver.png",
        "Bronze": "images/Bronze.png"
    };
    console.log(`Selected: "${selectElement.value}"`);
    imgElement.src = rankImages[selectElement.value] || "images/default.png";
}   

// Dropdowns beim Laden erstellen
createEloDropdowns();

// Funktion zur Erstellung der Dropdowns
function createDropdowns(containerId, options, count) {
    const container = document.getElementById(containerId);
    for (let i = 0; i < count; i++) {
        const select = document.createElement('select');
        select.id = `${containerId}Select${i + 1}`;
        const placeholderOption = document.createElement('option');
        placeholderOption.value = "";
        placeholderOption.textContent = "Bitte wählen...";
        select.appendChild(placeholderOption);

        options.forEach(optionValue => {
            const option = document.createElement('option');
            option.value = optionValue;
            option.textContent = optionValue;
            select.appendChild(option);
        });

        container.appendChild(select);
        container.appendChild(document.createElement('br'));
    }
}

createDropdowns('bans', bansOptions, 10);
createDropdowns('skins', skinsOptions, 10);

// Event Listener für Absenden
document.getElementById("submitBtn").addEventListener("click", function (event) {
    event.preventDefault();

    // Daten für Blue Team KDA
    const blueTeamTopKDA = `${document.getElementById("blueTeamTopKDA_Kills").value}/${document.getElementById("blueTeamTopKDA_Deaths").value}/${document.getElementById("blueTeamTopKDA_Assists").value}`;
    const blueTeamJungleKDA = `${document.getElementById("blueTeamJungleKDA_Kills").value}/${document.getElementById("blueTeamJungleKDA_Deaths").value}/${document.getElementById("blueTeamJungleKDA_Assists").value}`;
    const blueTeamMidKDA = `${document.getElementById("blueTeamMidKDA_Kills").value}/${document.getElementById("blueTeamMidKDA_Deaths").value}/${document.getElementById("blueTeamMidKDA_Assists").value}`;

    // Weitere Team-Daten und KDA
    const gamemode = document.getElementById("gamemode").value;
    const date = document.getElementById("date").value;
    const blueTeamTop = document.getElementById("blueTeamTop").value;
    const blueTeamJungle = document.getElementById("blueTeamJungle").value;
    const blueTeamMid = document.getElementById("blueTeamMid").value;
    const blueTeamADC = document.getElementById("blueTeamADC").value;
    const blueTeamSupport = document.getElementById("blueTeamSupport").value;
    const redTeamTop = document.getElementById("redTeamTop").value;
    const redTeamJungle = document.getElementById("redTeamJungle").value;
    const redTeamMid = document.getElementById("redTeamMid").value;
    const redTeamADC = document.getElementById("redTeamADC").value;
    const redTeamSupport = document.getElementById("redTeamSupport").value;


    // Bans, Skins, Elo, MVP und Winning Team
    const bans = Array.from(document.querySelectorAll('#bans select')).map(select => select.value);
    const skins = Array.from(document.querySelectorAll('#skins select')).map(select => select.value);
    const elo = Array.from(document.querySelectorAll('#elo select')).map(select => select.value);
    const mvp = document.getElementById("mvp").value;
    const smvp = document.getElementById("smvp").value;
    const winningTeam = document.getElementById("winningTeam").value;
    const roundTime = document.getElementById("roundTime").value;

    fetch("/save", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            gamemode: gamemode,
            date: date,
            bans: bans,
            blueTeam: {
                top: blueTeamTop,
                jungle: blueTeamJungle,
                mid: blueTeamMid,
                adc: blueTeamADC,
                support: blueTeamSupport
            },
            redTeam: {
                top: redTeamTop,
                jungle: redTeamJungle,
                mid: redTeamMid,
                adc: redTeamADC,
                support: redTeamSupport
            },
            elo: elo,
            skins: skins,
            mvp: mvp,
            smvp: smvp,
            winningTeam: winningTeam,
            roundTime: roundTime
        })
    }).then(response => response.json())
      .then(data => alert(data.message));
});