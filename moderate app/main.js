const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const axios = require('axios');
const { wrapper } = require('axios-cookiejar-support');
const tough = require('tough-cookie');
const cookieJar = new tough.CookieJar();
const client = wrapper(axios.create({
    jar: cookieJar,
    withCredentials: true,
}));

let loginWindow;
let forumsWindow;
let adsWindow;

function createLoginWindow() {
    loginWindow = new BrowserWindow({
        width: 400,
        height: 300,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: false,
            contextIsolation: true
        }
    });

    loginWindow.loadFile('./views/login.html');
}

function createForumsWindow(token) {
    forumsWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: false,
            contextIsolation: true
        }
    });

    adsWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: false,
            contextIsolation: true
        }
    });

    forumsWindow.loadFile('./views/forums.html');
    adsWindow.loadFile('./views/ads.html');
    
    forumsWindow.webContents.once('did-finish-load', () => {
        forumsWindow.webContents.send('auth-token', token);
    });

    adsWindow.webContents.once('did-finish-load', () => {
        adsWindow.webContents.send('auth-token', token);
    });

    loginWindow.close();
}

app.whenReady().then(() => {
    createLoginWindow();

    ipcMain.on('login-success', (event, token) => {
        createForumsWindow(token);
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});