document.getElementById('bmiForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    
    const response = await fetch('http://localhost:5000/api/bmi', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ weight, height })
    });
    
    const data = await response.json();
    document.getElementById('result').innerText = `IMC: ${data.bmi.toFixed(2)} (${data.category})`;
    
    loadHistory();
});

async function loadHistory() {
    const response = await fetch('http://localhost:5000/api/bmi/history');
    const history = await response.json();
    const historyList = document.getElementById('history');
    historyList.innerHTML = '';
    history.forEach(record => {
        const li = document.createElement('li');
        li.textContent = `Poids: ${record.weight}kg, Taille: ${record.height}m, IMC: ${record.bmi.toFixed(2)} (${record.category})`;
        historyList.appendChild(li);
    });
}

loadHistory();