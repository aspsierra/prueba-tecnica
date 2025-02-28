
<template>

  <main class="flex flex-row">

      <ul class="menu menu-lg bg-base-200 w-80 min-h-screen mr-4">
        <li> 
          <RouterLink to="/">
            <Icon icon="grommet-icons:task" width="24" height="24" />
            Tareas
          </RouterLink>
        </li>
        <li>
          <RouterLink to="/families">
            <Icon icon="flowbite:tag-outline" width="24" height="24" />
            Familias
          </RouterLink>
        </li>
        <li>
          <a href="https://github.com/aspsierra/prueba-tecnica">
            <Icon icon="mdi:github" width="24" height="24"/>
            Repositorio
          </a>
        </li>
      </ul>


    <RouterView class="container"/>

  </main>

</template>


<script>
  import { mapActions } from 'pinia';
import { RouterLink, RouterView } from 'vue-router'
import { useStore } from './stores/store';
import { Icon } from '@iconify/vue';

  export default {

    async mounted(){
      this.setStates()
    },
    components: {
      Icon
    },
    methods: {
      ...mapActions(useStore, ['setStates'])
    },
  }
</script>
