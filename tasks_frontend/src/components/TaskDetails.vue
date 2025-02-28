<template>

  <div class="modal-box w-11/12 max-w-5xl h-screen p-0 flex flex-col overflow-visible">
    <form method="dialog" class=" flex justify-between items-center">
      <p class="ml-10">{{ task.family.name }}</p>
      <div>
        <div @click="editTask" class="btn btn-md btn-info m-2">
          <Icon v-if="!editing" icon="material-symbols:edit-outline-rounded" width="24" height="24" />
          <Icon v-if="editing" icon="material-symbols:check-rounded" width="24" height="24" />        
        </div>
        <button @click="closeModal" class="btn btn-md btn-ghost m-2">
          <Icon icon="material-symbols:close" width="24" height="24" />
        </button>
      </div>
    </form>

    <div class="border-t-2 flex h-full justify-between">
      <main class="w-full h-full">
        <div class="my-5 m-10 text-xl font-bold text-white ">
          <p v-if="!editing">{{ task.title }}</p>
          <TextInput v-if="editing"  class="w-full" v-model="task.title" label="Título de la tarea" :value="task.title"/>
        </div>
        <div class="text-lg m-10 h-72">
          <p v-if="!editing" class="">
            {{ task.description }}
          </p>
          <TextareaInput v-if="editing" v-model="task.description" class="w-full" label="Descripción de la tarea"/>
        </div>
      </main>

      <aside class="w-80 max-w-xs bg-slate-800 px-4">
        <div class="border-b-2  py-4">
          <p>Fecha de vencimiento</p>

          <vue-tailwind-datepicker 
            v-model="task.due_date" 
            as-single
            :formatter="formatter"
            :shortcuts="false"
            i18n="es"
            :disabled="!editing"
            />
        </div>

        <div class="border-b-2  py-4">
          <p>Familia</p>
          <SelectInput class="w-full" 
            v-model="task.family.id"  
            label="Familia" 
            :options="families"
            :selectedValue="task.family.id"
            :disabled="!editing"
          />
        </div>
        <div class="border-b-2 py-4 ">
          <p>Estado</p>
          <SelectInput class="w-full" 
            v-model="task.state"  
            label="Estado" 
            :options="states"
            :selectedValue="task.state_full.value"
            :disabled="!editing"
          />
        </div>
       
       </aside>

       
      </div>

  </div>

</template>

<script>
import { Icon } from '@iconify/vue';
import { useRoute } from 'vue-router';
import VueTailwindDatepicker from "vue-tailwind-datepicker";
import { mapActions, mapState } from 'pinia';
import { useStore } from '@/stores/store';
import TextInput from './inputs/TextInput.vue';
import SelectInput from './inputs/SelectInput.vue';
import TextareaInput from './inputs/TextareaInput.vue';

export default {
  data(){
    return {
      id: null,
      formatter: {
        date: "DD/MM/YYYY",
        month: "MMM",
      },
      editing: false
    }
  },
  components:{
    Icon,
    VueTailwindDatepicker,
    SelectInput,
    TextInput,
    TextareaInput
  },
  computed:{
    ...mapState(useStore, ['task', 'states', 'families'])
  },
  async beforeMount(){
    const route = useRoute()
    this.id = route.params.id
    await this.getTaskDetails(this.id)
    await this.setFamilies()
  },
  methods: {
    ...mapActions(useStore, ['getTaskDetails', 'setFamilies']),
    closeModal() {
      this.$router.back()
    },
    editTask(){
      console.log('ejja');
      this.editing = !this.editing
    }
  }
}

</script>