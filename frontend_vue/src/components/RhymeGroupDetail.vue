<script setup>
import { ref, onMounted } from 'vue';

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
          <li v-for="word in groupDetails.words" :key="word.id">{{ word.text }}</li>
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
}

.detail-container {
  background-color: var(--secondary-bg);
  padding: 1.5rem 2rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
}

.group-title {
  color: var(--accent-color);
  margin-top: 0;
  border-bottom: 2px solid var(--accent-color);
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
}

.word-list h3 {
    margin-bottom: 1rem;
}

.word-list ul {
  list-style: none;
  padding: 0;
}

.word-list li {
  background-color: #2a2a2a;
  padding: 0.75rem 1rem;
  border-radius: 4px;
  margin-bottom: 0.5rem;
}

.add-word-form {
  display: flex;
  margin-bottom: 1.5rem;
}

.add-word-form input {
  flex-grow: 1;
  padding: 0.75rem;
  border: 1px solid var(--border-color);
  border-radius: 4px 0 0 4px;
  background-color: #2a2a2a;
  color: var(--text-color);
  font-family: 'Heebo', sans-serif;
}

.add-word-form button {
  padding: 0.75rem 1.5rem;
  border: 1px solid var(--accent-color);
  background-color: var(--accent-color);
  color: #121212;
  font-weight: bold;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
  transition: background-color 0.2s;
}

.add-word-form button:hover {
  background-color: #ffca6e;
}

.add-word-form button:disabled {
  background-color: #555;
  cursor: not-allowed;
}
</style> 