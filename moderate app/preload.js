const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    sendLoginSuccess: (token) => ipcRenderer.send('login-success', token),
    onAuthToken: (callback) => ipcRenderer.on('auth-token', (event, token) => callback(token))
});