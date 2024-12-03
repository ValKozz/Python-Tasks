async function getFromDB() {
try {
        const response = await fetch('getFromDB');
        if (!response.ok) throw new Error('Failed to fetch data');
        const raw_response = await response.json();
        updateCardsDB(raw_response);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to fetch cards. Please try again later.');
    }
}

function updateCardsDB(parsed_data) {
    let average_temp = 0;
    var coldest_city = parsed_data[0].fields

    const container = document.getElementById('his-card-container');
    container.innerHTML = ''; // delete the default
	let i = 0;
	while (i < parsed_data.length) {
        let current_city = parsed_data[i].fields;

        if (coldest_city.temp > current_city.temp) {
            coldest_city = current_city
        }

        average_temp += current_city.temp;

        city_card = createCardDB(parsed_data[i]);
   		container.appendChild(city_card);
		i++;
    }
    const average_info = document.getElementById('avg-temp-history');
    const coldest_city_info = document.getElementById('coldest-history');
    average_info.innerHTML =Number(average_temp/10).toFixed(2) + " C";
    coldest_city_info.innerHTML = coldest_city.name;
}

function createCardDB(city) {
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