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

function attachTrailingCard(text, data) {
	const card = document.createElement('div');
	card.className = 'card'
	card.innerHTML = `
  			<div class="card-body">
  				<h4> ${text} : ${data} </h4>
  			</div>
	`
	return card
}

function updateCards(data) {
    const container = document.getElementById('card_container');
    container.innerHTML = ''; // delete the default
    const parsed_data = JSON.parse(data);
    // Debug, remove
    // console.log(parsed_data);
    // console.log(parsed_data.length);
    if (parsed_data.length > 1) {
    	let i = 0;
    	while (i < parsed_data[0].length) {
 	   		card = createCard(parsed_data[0][i]);
 	   		container.appendChild(card);
    		i++;
		}
		// Attach remaining lowest temp and average, TODO, horrible fix
		let avg_temp = attachTrailingCard("Average Temperature", parsed_data[1]);
   		container.appendChild(avg_temp);
		let coldes_city = attachTrailingCard("Coldest city", parsed_data[2]);
   		container.appendChild(coldes_city);

    } else {
        card = createCard(parsed_data)
        container.appendChild(card);
    }
}

async function fetchFive() {
    try {
        const response = await fetch('/getFive', 
            {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(slider.value),
                cache: "no-cache",
                headers: new Headers({"content-type": "application/json"}) 
            }
                );
        if (!response.ok) throw new Error('Failed to fetch data');
        const data = await response.json();
        updateCards(data);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to fetch cards. Please try again later.');
    }
}

async function fetchSingle() {
	const cityField = document.getElementById("cityField");
	if (cityField.value == ""){
		return alert("Empty field, please enter a name of the city.");
	} else {
		try {
        	const response = await fetch('/getSingle', 
            {
    			method: "POST",
    			credentials: "include",
    			body: JSON.stringify(cityField.value),
    			cache: "no-cache",
    			headers: new Headers({"content-type": "application/json"})
			});

        	if (!response.ok) throw new Error('Failed to fetch data');

        	const data = await response.json();
        	updateCards(data);
        	
    	} catch (error) {
        	console.error('Error:', error);
        	alert('Failed to fetch cards. Please try again later.');
    	}
	}
}

document.getElementById('getNamed').addEventListener('click', fetchSingle);
document.getElementById('getFive').addEventListener('click', fetchFive);
