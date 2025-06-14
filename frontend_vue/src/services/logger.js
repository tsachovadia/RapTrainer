import { ref } from 'vue';

export const logs = ref([]);

export function log(message, type = 'info', data = null) {
  logs.value.unshift({
    id: Date.now() + Math.random(),
    timestamp: new Date().toLocaleTimeString(),
    type, // 'info', 'success', 'error'
    message,
    data: data ? JSON.stringify(data, null, 2) : null,
  });
} 