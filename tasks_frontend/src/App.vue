
<template>

  <main class="flex flex-row">

    <ul class="menu menu-lg bg-base-200 w-80 min-h-screen mr-4">
      <li> <RouterLink to="/">Tareas</RouterLink></li>
      <li> <RouterLink to="/families">Familias</RouterLink></li>
    </ul>

    <RouterView class="container"/>

  </main>

</template>


<script>
  import { RouterLink, RouterView } from 'vue-router'
</script>
