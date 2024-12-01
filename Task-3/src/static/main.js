const slider = document.getElementById("bSlider");
const sliderValue = document.getElementById("sliderValue");

window.onload=function() {
	sliderValue.textContent = slider.value;
}

slider.addEventListener("input", () => {
    sliderValue.textContent = slider.value;
});

function createCard(city) {
    const card = document.createElement('div');
    card.className = 'card';
    // TODO
    card.innerHTML = ` 
  			<div class="card-body">
    			<h4> ${city.name}, ${city.country} </h4>
    			<p> Temperature: ${city.temp} </p>
    			<p> Humidity: ${city.humidity} </p>
    			<p> Clouds: ${city.clouds}, ${city.clouds_percent} </p>
    			<p> Description ${city.weather_desc} </p>
		</div>
    `;
    return card;
}

// Function to update cards dynamically
function updateCards(data) {
    const container = document.getElementById('card_container');
    container.innerHTML = ''; // delete the default
    const parsed_data = JSON.parse(data);
    console.log(parsed_data)
    console.log(parsed_data.length)
    if (parsed_data.length > 1) {
    	let i = 0;
    	while (i < parsed_data[0].length) {
 	   		card = createCard(parsed_data[0][i]);
 	   		container.appendChild(card);
    		i++;
		}
    }
}

// Fetch data from the backend and update cards
async function fetchData() {
    try {
        const response = await fetch('/getFive');
        if (!response.ok) throw new Error('Failed to fetch data');
        const data = await response.json();
        updateCards(data);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to fetch cards. Please try again later.');
    }
}

document.getElementById('getFive').addEventListener('click', fetchData);
