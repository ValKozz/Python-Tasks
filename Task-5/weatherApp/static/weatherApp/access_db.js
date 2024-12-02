
async function getFromDB() {
try {
        const response = await fetch('getFromDB');
        if (!response.ok) throw new Error('Failed to fetch data');
        const raw_response = await response.json();
        updateCards(raw_response);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to fetch cards. Please try again later.');
    }
}

function updateCards(parsed_data) {
    console.log(parsed_data)
    const container = document.getElementById('his-card-container');
    container.innerHTML = ''; // delete the default
	let i = 0;
	while (i < parsed_data.length) {
   		card = createCard(parsed_data[i]);
   		container.appendChild(card);
		i++;
    }
}

function createCard(city) {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = ` 
  			<div class="card-body">
    			<h3> ${city.fields.name}, ${city.fields.country} </h3>
    			<p> Temperature: ${city.fields.temp} C </p>
    			<p> Humidity: ${city.fields.humidity}% </p>
    			<p> Weather: ${city.fields.clouds} </p>
                <p>${city.fields.clouds_percent}% of sky taken up by clouds</p>
    			<p> Description: ${city.fields.weather_desc} </p>
			</div>
    `;
    return card;
}

document.getElementById('RefreshDB').addEventListener('click', getFromDB);