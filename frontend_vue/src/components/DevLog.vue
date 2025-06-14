<script setup>
import { logs } from '@/services/logger';
import Panel from 'primevue/panel';
import ScrollPanel from 'primevue/scrollpanel';
</script>

<template>
  <Panel header="Development Log" toggleable collapsed>
    <ScrollPanel style="width: 100%; height: 200px">
      <div v-for="log in logs" :key="log.id" class="log-entry" :class="`log-${log.type}`">
        <strong>[{{ log.timestamp }}] [{{ log.type.toUpperCase() }}]</strong> {{ log.message }}
        <pre v-if="log.data">{{ log.data }}</pre>
      </div>
      <p v-if="!logs.length">No log entries yet.</p>
    </ScrollPanel>
  </Panel>
</template>

<style scoped>
.log-entry {
  padding: 4px;
  border-bottom: 1px solid #444;
  font-family: monospace;
  white-space: pre-wrap;
}
.log-info {
  color: #cdd6f4; /* Text */
}
.log-success {
  color: #a6e3a1; /* Green */
}
.log-error {
  color: #f38ba8; /* Red */
}
pre {
  margin-top: 5px;
  padding: 5px;
  background-color: #313244; /* Surface0 */
  border-radius: 4px;
}
</style> 