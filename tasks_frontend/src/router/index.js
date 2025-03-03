import { createRouter, createWebHistory } from 'vue-router'
import TasksList from '@/views/TasksList.vue'
import FamilyList from '@/views/FamilyList.vue'
import TaskDetails from '@/components/TaskDetails.vue'
import NotFound404 from '@/views/error/notFound404.vue'

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
      children: [
      ]
    },
    {
      path: '/family/:id',
      name: 'tasksByFamily',
      component: TasksList,
      props: true
    },
    {
      path: "/:pathMatch(.*)*", 
      name: 'notFound',
      component: NotFound404
    }
  ],
})

export default router
