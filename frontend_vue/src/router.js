import { createRouter, createWebHistory } from 'vue-router';
import RhymeGroupList from './components/RhymeGroupList.vue';
import RhymeGroupDetail from './components/RhymeGroupDetail.vue';

const routes = [
  {
    path: '/',
    name: 'RhymeGroupList',
    component: RhymeGroupList,
  },
  {
    path: '/rhyme-groups/:id',
    name: 'RhymeGroupDetail',
    component: RhymeGroupDetail,
    props: true, // This allows the :id to be passed as a prop
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 