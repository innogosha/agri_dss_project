document.getElementById('recommendationForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const region = document.getElementById('region').value;
    const soilType = document.getElementById('soil_type').value;

    fetch('/api/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            location: region,
            soil_type: soilType,
        }),
    })
    .then(response => response.json())
    .then(data => {
        const recommendationsDiv = document.getElementById('recommendations');
        recommendationsDiv.innerHTML = `
            <h3>Recommended Crops:</h3>
            <ul>
                ${data.recommended_crops.map(crop => `<li>${crop}</li>`).join('')}
            </ul>
            <h3>Irrigation Advice:</h3>
            <p>${data.irrigation}</p>
            <h3>Fertilization Advice:</h3>
            <p>${data.fertilization}</p>
        `;
    })
    .catch(error => console.error('Error:', error));
});
