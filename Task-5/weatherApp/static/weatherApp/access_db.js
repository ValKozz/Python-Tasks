async function getFromDB() {
try {
        const response = await fetch('getFromDB');
        if (!response.ok) throw new Error('Failed to fetch data');
        const data = await response.json();
        const parsed_data = JSON.parse(data);
        updateCards(parsed_data);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to fetch cards. Please try again later.');
    }
}

function updateCards(parsed_data) {
    const container = document.getElementById('his-card-container');
    container.innerHTML = ''; // delete the default
	let i = 0;
	while (i < parsed_data[3].length) {
   		card = createCard(parsed_data[3][i]);
   		container.appendChild(card);
		i++;
    }
}

function createCard(city) {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = ` 
  			<div class="card-body">
    			<h3> ${city.name}, ${city.country} </h3>
    			<p> Temperature: ${city.temp} C </p>
    			<p> Humidity: ${city.humidity}% </p>
    			<p> Weather: ${city.clouds} </p>
                <p>${city.clouds_percent}% of sky taken up by clouds</p>
    			<p> Description: ${city.weather_desc} </p>
			</div>
    `;
    return card;
}

document.getElementById('RefreshDB').addEventListener('click', getFromDB);