document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value || 'testeroot'; // Default para teste
    const password = document.getElementById('password').value || 'root123';   // Default para teste
    const messageDiv = document.getElementById('message');
    
    try {
        const response = await fetch('http://localhost:8000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });
        
        messageDiv.textContent = 'Credenciais enviadas para teste!';
        messageDiv.className = 'success';
        messageDiv.style.display = 'block';
        
    } catch (error) {
        messageDiv.textContent = 'Erro ao enviar: ' + error.message;
        messageDiv.className = 'error';
        messageDiv.style.display = 'block';
    }
});