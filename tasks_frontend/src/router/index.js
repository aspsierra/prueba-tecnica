import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TasksList from '@/views/TasksList.vue'
import FamilyList from '@/views/FamilyList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: TasksList,
    },
    {
      path: '/families',
      name: 'Familias',
      component: FamilyList,
    },
  ],
})

export default router
