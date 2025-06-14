// This file will contain the JavaScript logic for our application.
document.addEventListener('DOMContentLoaded', () => {
    const rhymeGroupsList = document.getElementById('rhyme-groups-list');
    const logOutput = document.getElementById('frontend-log');
    const addGroupForm = document.getElementById('add-group-form');
    const newGroupNameInput = document.getElementById('new-group-name');
    const groupTemplate = document.getElementById('group-template');

    function log(message) {
        const timestamp = new Date().toLocaleTimeString();
        logOutput.textContent += `[${timestamp}] ${message}\n`;
        // Scroll to the bottom of the log
        logOutput.parentElement.scrollTop = logOutput.parentElement.scrollHeight;
    }

    async function fetchRhymeGroups() {
        log('Fetching all rhyme groups...');
        try {
            const response = await fetch('/rhyme-groups');
            log(`Response status: ${response.status}`);
            if (!response.ok) throw new Error(`Server error: ${response.statusText}`);
            const groups = await response.json();
            log(`Found ${groups.length} groups.`);
            renderRhymeGroups(groups);
        } catch (error) {
            log(`Error fetching groups: ${error}`);
            console.error(error);
        }
    }

    async function fetchWordsForGroup(groupId) {
        log(`Fetching words for group ${groupId}...`);
        try {
            const response = await fetch(`/rhyme-groups/${groupId}`);
            log(`Response status: ${response.status}`);
            if (!response.ok) throw new Error(`Server error: ${response.statusText}`);
            const groupDetails = await response.json();
            log(`Found ${groupDetails.words.length} words for group ${groupId}.`);
            return groupDetails.words;
        } catch (error) {
            log(`Error fetching words: ${error}`);
            console.error(error);
            return [];
        }
    }

    function renderRhymeGroups(groups) {
        rhymeGroupsList.innerHTML = ''; // Clear previous list
        if (groups.length === 0) {
            rhymeGroupsList.textContent = 'No groups found.';
            return;
        }
        groups.forEach(group => {
            const groupClone = groupTemplate.content.cloneNode(true);
            const groupItem = groupClone.querySelector('.group-item');
            groupItem.dataset.id = group.id;
            const nameSpan = groupItem.querySelector('.group-name');
            nameSpan.textContent = `${group.name} (${group.word_count} words)`;
            
            // Store original name and word count for editing
            groupItem.dataset.name = group.name;
            groupItem.dataset.wordCount = group.word_count;

            rhymeGroupsList.appendChild(groupClone);
        });
        log('Finished rendering groups.');
    }
    
    function renderWords(wordsListElement, words) {
        wordsListElement.innerHTML = '';
        if (words.length === 0) {
            wordsListElement.innerHTML = '<li>No words in this group yet.</li>';
            return;
        }
        words.forEach(word => {
            const li = document.createElement('li');
            li.dataset.id = word.id;
            li.innerHTML = `
                <span class="word-text">${word.text}</span>
                <input type="text" class="edit-word-input" value="${word.text}" style="display:none;">
                <div class="actions">
                    <button class="edit-word-btn">Edit</button>
                    <button class="save-word-btn" style="display:none;">Save</button>
                    <button class="delete-word-btn">Delete</button>
                </div>
            `;
            wordsListElement.appendChild(li);
        });
    }

    rhymeGroupsList.addEventListener('click', async (event) => {
        const target = event.target;
        const groupItem = target.closest('.group-item');
        if (!groupItem) return;
        
        const groupId = groupItem.dataset.id;

        // View Words button
        if (target.classList.contains('view-words-btn')) {
            const wordsContainer = groupItem.querySelector('.words-container');
            const wordsList = groupItem.querySelector('.words-list');
            const isVisible = wordsContainer.style.display === 'block';

            if (!isVisible) {
                const words = await fetchWordsForGroup(groupId);
                renderWords(wordsList, words);
            }
            wordsContainer.style.display = isVisible ? 'none' : 'block';
            target.textContent = isVisible ? 'View Words' : 'Hide Words';
        }

        // Edit Group button
        if (target.classList.contains('edit-btn')) {
            const nameSpan = groupItem.querySelector('.group-name');
            const editInput = groupItem.querySelector('.edit-input');
            nameSpan.style.display = 'none';
            editInput.style.display = 'inline-block';
            editInput.value = groupItem.dataset.name; // Use stored name
            editInput.focus();
            target.style.display = 'none';
            groupItem.querySelector('.save-btn').style.display = 'inline-block';
        }

        // Save Group button
        if (target.classList.contains('save-btn')) {
            const newName = groupItem.querySelector('.edit-input').value;
            await updateRhymeGroup(groupId, newName);
        }

        // Delete Group button
        if (target.classList.contains('delete-btn')) {
            if (confirm(`Are you sure you want to delete the group "${groupItem.dataset.name}"?`)) {
                await deleteRhymeGroup(groupId);
            }
        }

        // Word-related buttons
        const wordItem = target.closest('li[data-id]');
        if (wordItem && groupItem.querySelector('.words-list').contains(wordItem)) {
            const wordId = wordItem.dataset.id;

            if (target.classList.contains('edit-word-btn')) {
                const textSpan = wordItem.querySelector('.word-text');
                const editInput = wordItem.querySelector('.edit-word-input');
                textSpan.style.display = 'none';
                editInput.style.display = 'inline-block';
                editInput.focus();
                target.style.display = 'none';
                wordItem.querySelector('.save-word-btn').style.display = 'inline-block';
            }

            if (target.classList.contains('save-word-btn')) {
                const newText = wordItem.querySelector('.edit-word-input').value;
                await updateWord(wordId, newText, groupItem.querySelector('.words-list'));
            }

            if (target.classList.contains('delete-word-btn')) {
                 if (confirm(`Are you sure you want to delete this word?`)) {
                    await deleteWord(wordId, groupItem.querySelector('.words-list'));
                }
            }
        }
    });

    // Event listener for the add form
    addGroupForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const name = newGroupNameInput.value.trim();
        if (!name) return;
        log(`Creating new group "${name}"...`);
        try {
            const response = await fetch('/rhyme-groups', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name })
            });
            if (!response.ok) throw new Error(`Server error: ${response.statusText}`);
            log('Group created successfully.');
            newGroupNameInput.value = '';
            await fetchRhymeGroups(); // Refresh the entire list
        } catch (error) {
            log(`Error creating group: ${error}`);
        }
    });

    // Word form submission
    rhymeGroupsList.addEventListener('submit', async (event) => {
        if (event.target.classList.contains('add-word-form')) {
            event.preventDefault();
            const groupItem = event.target.closest('.group-item');
            const groupId = groupItem.dataset.id;
            const input = event.target.querySelector('.new-word-input');
            const wordText = input.value.trim();

            if (wordText) {
                await addWordToGroup(wordText, groupId, groupItem.querySelector('.words-list'));
                input.value = '';
            }
        }
    });

    // --- API HELPER FUNCTIONS ---
    
    async function updateRhymeGroup(id, name) {
        log(`Updating group ${id} to name "${name}"...`);
        try {
            const response = await fetch(`/rhyme-groups/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name })
            });
            if (!response.ok) throw new Error(`Server error: ${response.statusText}`);
            log('Group updated successfully.');
            await fetchRhymeGroups();
        } catch (error) {
            log(`Error updating group: ${error}`);
        }
    }

    async function deleteRhymeGroup(id) {
        log(`Deleting group ${id}...`);
        try {
            const response = await fetch(`/rhyme-groups/${id}`, { method: 'DELETE' });
            if (!response.ok) throw new Error(`Server error: ${response.statusText}`);
            log('Group deleted successfully.');
            await fetchRhymeGroups();
        } catch (error) {
            log(`Error deleting group: ${error}`);
        }
    }

    async function addWordToGroup(text, groupId, wordsListElement) {
        log(`Adding word "${text}" to group ${groupId}...`);
        try {
            const response = await fetch(`/rhyme-groups/${groupId}/words`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });
            if (!response.ok) throw new Error(`Server error: ${response.statusText}`);
            log('Word added successfully.');
            const newWords = await fetchWordsForGroup(groupId);
            renderWords(wordsListElement, newWords); // Re-render only the words list
        } catch (error) {
            log(`Error adding word: ${error}`);
        }
    }

    async function updateWord(id, text, wordsListElement) {
        log(`Updating word ${id} to "${text}"...`);
        try {
            const response = await fetch(`/words/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });
            if (!response.ok) throw new Error(`Server error: ${response.statusText}`);
            log('Word updated successfully.');
            const groupId = wordsListElement.closest('.group-item').dataset.id;
            const newWords = await fetchWordsForGroup(groupId);
            renderWords(wordsListElement, newWords);
        } catch (error) {
            log(`Error updating word: ${error}`);
        }
    }

    async function deleteWord(id, wordsListElement) {
        log(`Deleting word ${id}...`);
        try {
            const response = await fetch(`/words/${id}`, { method: 'DELETE' });
            if (!response.ok) throw new Error(`Server error: ${response.statusText}`);
            log('Word deleted successfully.');
            const groupId = wordsListElement.closest('.group-item').dataset.id;
            const newWords = await fetchWordsForGroup(groupId);
            renderWords(wordsListElement, newWords);
        } catch (error) {
            log(`Error deleting word: ${error}`);
        }
    }

    // --- INITIALIZATION ---
    // Initial fetch when the page loads
    fetchRhymeGroups();
}); 