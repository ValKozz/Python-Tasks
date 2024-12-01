const slider = document.getElementById("bSlider");
const sliderValue = document.getElementById("sliderValue");

window.onload=function() {
	sliderValue.textContent = slider.value;
}

slider.addEventListener("input", () => {
    sliderValue.textContent = slider.value;
});

function createCard(title, description, imageUrl) {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
  			<div class="card-body">
    			This will be updated.
		</div>
    `;
    return card;
}

// Function to update cards dynamically
function updateCards(data) {
    const container = document.getElementById('card_container');
    container.innerHTML = ''; // delete the default
    console.log(data);
    
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
