function getRecommendations() {
    const role = document.getElementById("role").value;
    const skills = document.getElementById("skills").value;

    fetch('http://localhost:5000/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ role, skills })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("output").innerHTML = data.recommendations.join("<br>");
        })
        .catch(error => {
            document.getElementById("output").innerHTML = "Error fetching recommendations.";
            console.error(error);
        });
}
