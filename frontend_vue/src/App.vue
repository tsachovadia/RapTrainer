<script setup>
// This is the main app component. It only holds the general layout and the router view.
</script>

<template>
  <div id="app-container">
    <header class="app-header">
      <h1>רישום חרוזים</h1>
    </header>

    <main class="main-content">
      <router-view />
    </main>

    <footer class="app-footer">
      <p>&copy; 2024 RapTrainer</p>
    </footer>
  </div>
</template>

<style>
/* Global styles remain here */
:root {
  --primary-bg: #121212;
  --secondary-bg: #1e1e1e;
  --primary-text: #e0e0e0;
  --accent-color: #bb86fc;
  --border-color: #333;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  background-color: var(--primary-bg);
  color: var(--primary-text);
  margin: 0;
  direction: rtl; /* Right-to-left for Hebrew */
}

#app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  padding: 2rem;
}

.app-header {
  text-align: center;
  margin-bottom: 2rem;
  color: var(--accent-color);
}

.main-content {
  flex-grow: 1;
}

.app-footer {
  text-align: center;
  margin-top: 2rem;
  color: #888;
  font-size: 0.9rem;
}
</style>