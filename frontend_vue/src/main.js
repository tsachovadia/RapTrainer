import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Import the router
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/aura-light-noir/theme.css'; // theme
import 'primevue/resources/primevue.min.css'; // core css
import 'primeicons/primeicons.css'; // icons

const app = createApp(App);
app.use(PrimeVue);
app.use(router); // Use the router

app.mount('#app') 