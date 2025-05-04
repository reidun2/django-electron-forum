let authToken = null;

async function fetchForums() {
    try {
        const response = await fetch('http://localhost:8000/apil/categories/', {
            headers: {
                'Authorization': `Token ${authToken}`
            }
        });
        const categories = await response.json();

        const forumsList = document.getElementById('forums-list');
        forumsList.innerHTML = '';

        categories.forEach(category => {

            const categoryItem = document.createElement('li');
            categoryItem.innerHTML = `<strong>Category: ${category.name}</strong>`;

            const forumsUl = document.createElement('ul');
            
            const sortedForums = category.forums.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));

            sortedForums.forEach(forum => {
                const forumItem = document.createElement('li');
                forumItem.innerHTML = `
                    <h3>Forum: ${forum.name}</h3>
                    <p>${forum.description}</p>
                    ${forum.image ? `<img src="${forum.image}" alt="Forum Image" style="max-width: 150px; display: block; margin-top: 5px;">` : ''}
                `;

                const messagesUl = document.createElement('ul');

                const sortedMessages = forum.messages.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));

                sortedMessages.forEach(message => {
                    const messageItem = document.createElement('li');
                    messageItem.innerHTML = `
                        <p>Message: ${message.content}</p>
                        <small>Created: ${new Date(message.created_at).toLocaleString()}</small>
                        ${message.image ? `<img src="${message.image}" alt="Message Image" style="max-width: 120px; display: block; margin-top: 5px;">` : ''}
                        <button onclick="deleteMessage(${message.id})" class="btn btn-danger" style="margin-top: 5px;">Delete</button>`;
                    messagesUl.appendChild(messageItem);
                });

                forumItem.appendChild(messagesUl);
                forumsUl.appendChild(forumItem);
            });

            categoryItem.appendChild(forumsUl);
            forumsList.appendChild(categoryItem);
        });
    } catch (error) {
        console.error('Error fetching forums:', error);
    }
};

async function deleteMessage(messageId) {
    const confirmDelete = confirm('Are you sure you want to delete this message?');
    if (!confirmDelete) return;

    try {
        const response = await fetch(`http://localhost:8000/apil/messages/${messageId}/`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Token ${authToken}`,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            alert('Message deleted successfully');
            await fetchForums();
        } else {
            alert('Failed to delete message');
        }
    } catch (error) {
        console.error('Error deleting message:', error);
        alert('Server error');
    }
}

window.electronAPI.onAuthToken(async (token) => {
    authToken = token;
    await fetchForums();
});