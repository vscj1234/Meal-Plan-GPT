document.getElementById('preferenceForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        const recommendationDiv = document.getElementById('recommendation');
        const output = document.getElementById('recommendationOutput');
        output.textContent = data.recommendation;
        recommendationDiv.classList.remove('hidden');
    });
}); 