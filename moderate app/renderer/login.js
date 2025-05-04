const form = document.getElementById('login-form');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://localhost:8000/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });
        if (response.ok) {
            const data = await response.json();
            const token = data.token;
            window.electronAPI.sendLoginSuccess(token);
        } else {
            const errorData = await response.json();
            errorMessage.textContent = errorData.detail || 'Login failed';
        }
    } catch (error) {
        errorMessage.textContent = 'Server not available';
    }
});