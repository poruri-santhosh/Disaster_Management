// ---------------- MAP SETUP ----------------
const map = L.map('map').setView([20.5937, 78.9629], 5); // India center

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// ---------------- LOAD PREDICTIONS.JSON ----------------
fetch("predictions.json")
  .then(res => res.json())
  .then(data => {
      if (!data.records || data.records.length === 0) {
          document.getElementById("list").innerHTML =
              "<p style='color:red;'>Error: No records found in predictions.json</p>";
          return;
      }

      displayList(data.records);
      addMarkers(data.records);
  })
  .catch(err => {
      console.error(err);
      document.getElementById("list").innerHTML =
          "<p style='color:red;'>Error loading JSON file</p>";
  });


// ---------------- SHOW LIST OF LOCATIONS ----------------
function displayList(records) {
    const list = document.getElementById("list");
    list.innerHTML = ""; // clear old items

    records.forEach(rec => {
        const div = document.createElement("div");
        div.className = "item";
        div.innerHTML = `
            <p><b>Location ID:</b> ${rec.id}</p>
            <p><b>City:</b> ${rec.location}</p>
            <p><b>Risk:</b> ${(rec.prediction * 100).toFixed(2)}%</p>
            <p><b>Rainfall:</b> ${rec.rainfall_mm} mm</p>
            <p><b>Action:</b> ${rec.action}</p>
        `;
        list.appendChild(div);
    });
}


// ---------------- MAP MARKERS ----------------
function addMarkers(records) {

    // Predefined coordinates for cities
    const cityCoords = {
        "Hyderabad": [17.3850, 78.4867],
        "Vijayawada": [16.5062, 80.6480],
        "Chennai": [13.0827, 80.2707],
        "Mumbai": [19.0760, 72.8777],
        "Bangalore": [12.9716, 77.5946]
    };

    records.forEach(rec => {
        if (cityCoords[rec.location]) {
            const marker = L.marker(cityCoords[rec.location]).addTo(map);
            marker.bindPopup(`
                <b>${rec.location}</b><br>
                Risk: ${(rec.prediction * 100).toFixed(2)}%<br>
                Rainfall: ${rec.rainfall_mm} mm
            `);
        }
    });
}
