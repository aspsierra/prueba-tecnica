import { createRouter, createWebHistory } from 'vue-router'
import TasksList from '@/views/TasksList.vue'
import FamilyList from '@/views/FamilyList.vue'
import TaskDetails from '@/components/TaskDetails.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'tareas',
      component: TasksList,
      children: [
        {
          path: '/task/:id',
          name: 'Tarea',
          component: TaskDetails,
          props: true
        },
      ]
    },
    {
      path: '/families',
      name: 'Familias',
      component: FamilyList,
    },
  ],
})

export default router
