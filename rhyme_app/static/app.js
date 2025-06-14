// This file will contain the JavaScript logic for our application.
document.addEventListener('DOMContentLoaded', () => {
    console.log('Rap Trainer App Loaded');

    const saveIdeaBtn = document.getElementById('save-idea-btn');
    if (saveIdeaBtn) {
        saveIdeaBtn.addEventListener('click', () => {
            const ideaText = document.getElementById('idea-textarea').value;
            if (ideaText) {
                // We will implement the API call here later
                console.log('Saving idea:', ideaText);
                alert('Idea saved (not really, this is a placeholder)!');
            } else {
                alert('Please enter an idea.');
            }
        });
    }
}); 