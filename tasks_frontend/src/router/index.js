import { createRouter, createWebHistory } from 'vue-router'
import TasksList from '@/views/TasksList.vue'
import FamilyList from '@/views/FamilyList.vue'
import TaskDetails from '@/components/TaskDetails.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'taskList',
      component: TasksList,
      children: [
        {
          path: '/task/:id',
          name: 'task',
          component: TaskDetails,
          props: true
        },
        {
          path: '/task/new',
          name: 'newTask',
          component: TaskDetails,
        },
      ]
    },
    {
      path: '/families',
      name: 'familyList',
      component: FamilyList,
    },
  ],
})

export default router
