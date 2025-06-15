<script setup>
import { ref, onMounted, nextTick } from 'vue';

// The component will receive the group ID as a prop from the router
const props = defineProps({
  id: {
    type: String,
    required: true,
  },
});

const groupDetails = ref(null);
const error = ref(null);
const isLoading = ref(true);
const newWord = ref('');
const isSubmitting = ref(false);

// State for inline editing
const editingWordId = ref(null);
const editingWordText = ref('');

async function fetchGroupDetails() {
  try {
    isLoading.value = true;
    error.value = null;
    const response = await fetch(`http://127.0.0.1:5000/api/rhyme-groups/${props.id}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    groupDetails.value = data;
  } catch (e) {
    console.error(`Failed to fetch details for group ${props.id}:`, e);
    error.value = 'Failed to load group details.';
  } finally {
    isLoading.value = false;
  }
}

async function addWord() {
  if (!newWord.value.trim()) {
    return; // Don't add empty words
  }

  isSubmitting.value = true;
  error.value = null;

  try {
    const response = await fetch(`http://127.0.0.1:5000/api/rhyme-groups/${props.id}/words`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: newWord.value }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
    }

    // Clear the input and refresh the list
    newWord.value = '';
    await fetchGroupDetails();

  } catch (e) {
    console.error('Failed to add word:', e);
    error.value = `Failed to add word: ${e.message}`;
  } finally {
    isSubmitting.value = false;
  }
}

function editWord(word) {
  editingWordId.value = word.id;
  editingWordText.value = word.text;
  nextTick(() => {
    // Focus the input element after it becomes visible
    document.querySelector('.edit-input').focus();
  });
}

function cancelEdit() {
  editingWordId.value = null;
  editingWordText.value = '';
}

async function updateWord() {
  if (!editingWordText.value.trim() || !editingWordId.value) return;
  
  isSubmitting.value = true;
  try {
    const response = await fetch(`http://127.0.0.1:5000/api/words/${editingWordId.value}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: editingWordText.value }),
    });
    if (!response.ok) throw new Error('Failed to update word');
    
    // Optimistically update the UI
    const wordIndex = groupDetails.value.words.findIndex(w => w.id === editingWordId.value);
    if (wordIndex !== -1) {
      groupDetails.value.words[wordIndex].text = editingWordText.value;
    }

    cancelEdit(); // Exit editing mode
  } catch (e) {
    error.value = e.message;
    console.error(e);
  } finally {
    isSubmitting.value = false;
  }
}

async function deleteWord(wordId) {
    if (!confirm('האם אתה בטוח שברצונך למחוק מילה זו?')) {
        return;
    }
    isSubmitting.value = true;
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/words/${wordId}`, {
            method: 'DELETE',
        });
        if (!response.ok) throw new Error('Failed to delete word');
        
        // Refresh list after deleting
        await fetchGroupDetails();
    } catch (e) {
        error.value = e.message;
        console.error(e);
    } finally {
        isSubmitting.value = false;
    }
}

onMounted(() => {
  fetchGroupDetails();
});
</script>

<template>
  <div>
    <div v-if="isLoading" class="loading">טוען...</div>
    <div v-if="error" class="error-message">{{ error }}</div>
    
    <div v-if="groupDetails" class="detail-container">
      <h2 class="group-title">{{ groupDetails.name }}</h2>
      
      <!-- Add Word Form -->
      <form @submit.prevent="addWord" class="add-word-form">
        <input 
          type="text"
          v-model="newWord"
          placeholder="הוסף מילה חדשה..."
          :disabled="isSubmitting"
        />
        <button type="submit" :disabled="isSubmitting">
          {{ isSubmitting ? 'מוסיף...' : 'הוסף' }}
        </button>
      </form>

      <div v-if="groupDetails.words && groupDetails.words.length > 0" class="word-list">
        <h3>מילים בקבוצה:</h3>
        <ul>
          <li v-for="word in groupDetails.words" :key="word.id" class="word-item">
            <div v-if="editingWordId === word.id" class="edit-mode">
              <input 
                v-model="editingWordText"
                class="edit-input"
                @keyup.enter="updateWord" 
                @keyup.esc="cancelEdit"
              />
              <button @click="updateWord" class="save-btn">שמור</button>
              <button @click="cancelEdit" class="cancel-btn">בטל</button>
            </div>
            <div v-else class="view-mode">
              <span @click="editWord(word)" class="word-text">{{ word.text }}</span>
              <button @click="deleteWord(word.id)" class="delete-btn">מחק</button>
            </div>
          </li>
        </ul>
      </div>
      <div v-else>
        <p>אין עדיין מילים בקבוצה זו.</p>
      </div>

      <!-- We can add the list of related bars here later -->

    </div>
  </div>
</template>

<style scoped>
.loading {
  text-align: center;
  padding: 2rem;
  font-style: italic;
}

.error-message {
  color: #cf6679;
  background-color: #3c1f24;
  border: 1px solid #cf6679;
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
  margin-bottom: 1rem;
}

.detail-container {
  background-color: #2c2c2c;
  padding: 1.5rem 2rem;
  border-radius: 8px;
  border: 1px solid #444;
}

.group-title {
  color: #bb86fc;
  margin-top: 0;
  border-bottom: 2px solid #bb86fc;
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
}

/* Form for adding a new word */
.add-word-form {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

.add-word-form input {
  flex-grow: 1;
}

.add-word-form button {
  white-space: nowrap;
}

.word-list h3 {
  margin-bottom: 1rem;
  color: #e0e0e0;
}

.word-list ul {
  list-style: none;
  padding: 0;
}

.word-item {
  background-color: #3a3a3a;
  padding: 0.75rem 1rem;
  border-radius: 4px;
  margin-bottom: 0.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background-color 0.2s;
}

.word-item:hover {
    background-color: #4a4a4a;
}

.word-item .view-mode, .word-item .edit-mode {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  gap: 0.75rem;
}

.word-text {
  cursor: pointer;
  flex-grow: 1;
  color: #e0e0e0;
}

/* Shared input style */
.add-word-form input,
.edit-input {
  background-color: #252525;
  color: #e0e0e0; /* CORRECTED COLOR */
  border: 1px solid #555;
  padding: 0.5rem;
  border-radius: 4px;
}

.edit-input {
    flex-grow: 1;
}

/* Shared button styles */
button {
  background-color: #bb86fc;
  color: #121212;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.2s;
}

button:disabled {
  background-color: #555;
  cursor: not-allowed;
}

button:not(:disabled):hover {
  background-color: #a06cd5;
}

/* Specific button styles */
.delete-btn {
  background-color: #cf6679;
}
.delete-btn:hover {
  background-color: #b05261;
}

.cancel-btn {
  background-color: #777;
}
.cancel-btn:hover {
  background-color: #666;
}

.save-btn {
    background-color: #03dac6;
}
.save-btn:hover {
    background-color: #01b8a3;
}
</style> 