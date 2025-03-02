
<template>

  <main class="flex flex-row">

      <ul class="menu menu-lg bg-base-200 w-80 min-h-screen mr-4">
        <li class="menu-title">Prueba técnica</li>
        <li>
          <div v-if="!user.pk" @click="openLoginForm">
            <Icon icon="solar:key-outline" width="24" height="24" />            
            Iniciar Sesión
          </div>
          <details v-if="user.pk">
            <summary>
              <Icon icon="majesticons:user-line" width="24" height="24" />
              {{ user.username }}
            </summary>
            <ul>
              <li @click="showConfirmation = true"><a>Cerrar Sesión</a></li>
            </ul>
          </details>
        </li>
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

  <dialog ref="loginForm" class="modal">
    <div class="modal-box p-0">
      <form method="dialog" class="text-right">
        <button class="btn btn-md btn-ghost m-2" ref="btnCloseLoginForm">
          <Icon icon="material-symbols:close" width="24" height="24" />
        </button>
      </form>
      <LoginForm @closeForm="closeLoginForm"/>
    </div>
  </dialog>

  <ConfirmationModal 
        :show="showConfirmation" 
        label="¿Quieres cerrar la sesión?"
        @cancel="showConfirmation=false"
        @accept="closeSession"
    />

</template>


<script>
  import { mapActions, mapState } from 'pinia';
  import { RouterLink, RouterView } from 'vue-router'
  import { useStore } from './stores/store';
  import { Icon } from '@iconify/vue';
  import LoginForm from './auth/LoginForm.vue';
  import ConfirmationModal from './components/notifications/ConfirmationModal.vue';

  export default {

    data(){
      return {
        showConfirmation: false
      }
    },
    components: {
      Icon,
      LoginForm,
      ConfirmationModal
    },
    computed: {
      ...mapState(useStore, ['user'])
    },
    methods: {
      ...mapActions(useStore, ['setStates', 'login', 'logout']),
      openLoginForm(){
        this.$refs.loginForm.showModal()
      },
      closeLoginForm(){
        this.$refs.btnCloseLoginForm.click()
      },
      async closeSession(){
        await this.logout()
        this.showConfirmation = false
      }
    },
    async mounted(){
      if (localStorage.getItem('token'))
        this.login(localStorage.getItem('token'))
      this.setStates()
    },
  }
</script>
