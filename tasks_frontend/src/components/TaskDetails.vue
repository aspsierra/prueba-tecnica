<template>

  <div class="modal-box w-11/12 max-w-5xl h-screen p-0 flex flex-col overflow-visible">
    <form method="dialog" class=" flex justify-between items-center">
      <p class="ml-10">{{ family.name }}</p>
      <button @click="closeModal" class="btn btn-md btn-ghost m-2">
        <Icon icon="material-symbols:close" width="24" height="24" />
      </button>
    </form>

    <div class="border-t-2 flex h-full">
      <main class="">
        <p class="text-xl font-bold text-white my-5 m-10">{{ task.title }}</p>
        <p class="text-lg m-10">
          {{ task.description }}
        </p>
      </main>
      <aside class="w-80 bg-slate-800 px-4">
        <div class="border-b-2  py-4">
          <p>Familia</p>
          <p>{{ family.name }}</p>
        </div>
        <div class="border-b-2 py-4">
          <p>Estado</p>
          <p>{{ task.state }}</p>
        </div>
        <div class="border-b-2  py-4">
          <p>Fecha de vencimiento</p>

          <vue-tailwind-datepicker 
            v-model="task.due_date" 
            as-single
            :formatter="formatter"
            :shortcuts="false"
            i18n="es"
            disabled
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
import SelectInput from './inputs/SelectInput.vue';
import { mapActions, mapState } from 'pinia';
import { useStore } from '@/stores/store';

export default {
  data(){
    return {
      id: null,
      //task: {},
      family: {},
      state: {},
      formatter: {
        date: "DD/MM/YYYY",
        month: "MMM",
      },
      dueDate: ''
    }
  },
  components:{
    Icon,
    VueTailwindDatepicker,
    SelectInput
  },
  computed:{
    ...mapState(useStore, ['task'])
  },
  async mounted(){
    const route = useRoute()
    this.id = route.params.id
    await this.getTaskDetails(this.id)
    
    //await this.fetchFamily()
  },
  methods: {
    ...mapActions(useStore, ['getTaskDetails']),
    async fetchFamily() {
      //this.family = await this.$api.getSingleFamily(this.task.family)
      console.log(this.family);
      
    },
    async fetchStates(){

    },
    closeModal() {
      this.$router.back()
    },
  }
}

</script>