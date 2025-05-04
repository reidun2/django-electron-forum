let authToken = null;

async function fetchAds() {
    try {
        const response = await fetch('http://localhost:8000/apil/ads/', {
            headers: {
                'Authorization': `Token ${authToken}`
            }
        });
        const ads = await response.json();

        const adsList = document.getElementById('ads-list');
        adsList.innerHTML = '';

        ads.forEach(ad => {
            const adItem = document.createElement('li');
            adItem.id = `ad-${ad.id}`;
            adItem.innerHTML = `
                ${ad.link ? `<a href="${ad.link}" target="_blank">` : ''}
                ${ad.image ? `<img src="${ad.image}" alt="Ad Image" style="max-width: 150px; display: block; margin-top: 5px;">` : ''}
                ${ad.link ? `</a><span style="display:block;"><a href="${ad.link}" target="_blank">${ad.link}</a></span>` : ''}
                <button onclick="deleteAd(${ad.id})" class="btn btn-danger" style="margin-top: 5px;">Delete</button>`;
            adsList.appendChild(adItem);
        });
    } catch (error) {
        console.error('Error fetching ads:', error);
        alert('Server error');
    }
};     

async function deleteAd(adId) {
    const confirmDelete = confirm('Are you sure you want to delete this ad?');
    if (!confirmDelete) return;

    try {
        const response = await fetch(`http://localhost:8000/apil/ads/${adId}/`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Token ${authToken}`,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            alert('Ad deleted successfully');
            await fetchAds();
        } else {
            console.error('Error deleting ad:', error);
            alert('Failed to delete ad');
        }
    } catch (error) {
        console.error('Error deleting ad:', error);
        alert('Server error');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('upload-ad-form');
    uploadForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const fileInput = document.getElementById('ad-image');
        const linkInput = document.getElementById('ad-link');
        const file = fileInput.files[0];
        const link = linkInput.value;

        if (!file || !link) return;

        const formData = new FormData();
        formData.append('image', file);
        formData.append('link', link);

        try {
            const response = await fetch('http://localhost:8000/apil/ads/', {
                method: 'POST',
                headers: {
                    'Authorization': `Token ${authToken}`
                },
                body: formData
            });

            if (response.ok) {
                alert('Ad uploaded successfully');
                fileInput.value = '';
                linkInput.value = '';
                await fetchAds();
            } else {
                alert('Failed to upload ad');
            }
        } catch (error) {
            console.error('Upload error:', error);
            alert('Server error');
        }
    });
});

window.electronAPI.onAuthToken(async (token) => {
    authToken = token;
    await fetchAds();
});