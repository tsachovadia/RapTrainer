<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink } from 'vue-router';

const rhymeGroups = ref([]);
const error = ref(null);

async function fetchRhymeGroups() {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/rhyme-groups');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    rhymeGroups.value = data;
  } catch (e) {
    console.error("Failed to fetch rhyme groups:", e);
    error.value = 'Failed to load rhyme groups. Is the backend server running?';
  }
}

onMounted(() => {
  fetchRhymeGroups();
});
</script>

<template>
    <div v-if="error" class="error-message">
    <p>{{ error }}</p>
    </div>

    <div v-else class="rhyme-groups-container">
    <h2>קבוצות חרוזים</h2>
    <ul>
        <li v-for="group in rhymeGroups" :key="group.id" class="rhyme-group-item">
        <RouterLink :to="{ name: 'RhymeGroupDetail', params: { id: group.id } }" class="group-link">
            <span class="group-name">{{ group.name }}</span>
            <span class="word-count">({{ group.word_count }} מילים)</span>
        </RouterLink>
        </li>
    </ul>
    </div>
</template>

<style scoped>
/* Scoped styles will only apply to this component */
.error-message {
  color: #cf6679;
  background-color: #3c1f24;
  border: 1px solid #cf6679;
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
}

.rhyme-groups-container {
  background-color: var(--secondary-bg);
  padding: 1.5rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
}

.rhyme-group-item {
  list-style: none;
  padding: 1rem 0;
  border-bottom: 1px solid var(--border-color);
}

.rhyme-group-item:last-child {
  border-bottom: none;
}

.group-link {
  text-decoration: none;
  color: var(--primary-text);
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background-color 0.3s;
  padding: 0.5rem;
  border-radius: 4px;
}

.group-link:hover {
  background-color: #2a2a2a;
  color: var(--accent-color);
}

.group-name {
  font-weight: 500;
  font-size: 1.2rem;
}

.word-count {
  font-style: italic;
  color: #888;
}
</style> 