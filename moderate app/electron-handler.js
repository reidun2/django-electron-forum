const { ipcMain } = require('electron');
const axios = require('axios').default;
const { wrapper } = require('axios-cookiejar-support');
const tough = require('tough-cookie');

ipcMain.handle('login', async (event, { username, password }) => {
    try {
        const cookieJar = new tough.CookieJar();
        const client = wrapper(axios.create({ jar: cookieJar, withCredentials: true }));

        await client.get('http://localhost:8000/login/');

        const csrfToken = cookieJar.getCookiesSync('http://localhost:8000')
            .find(cookie => cookie.key === 'csrftoken')?.value;

        const response = await client.post('http://localhost:8000/login/', {
            username,
            password
        }, {
            headers: {
                'X-CSRFToken': csrfToken
            }
        });

        return response.data;
    } catch (error) {
        return { error: error.message };
    }
});
