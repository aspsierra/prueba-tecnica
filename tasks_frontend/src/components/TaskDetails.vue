<template>

  <div class="modal-box w-11/12 max-w-5xl h-screen p-0 flex flex-col overflow-visible">
    <form method="dialog">
      <div class="w-full text-right">
        <div v-if="newTask" @click="addTask" class="btn btn-md btn-info m-2">
          <Icon icon="material-symbols:add-2-rounded" width="24" height="24" />     
        </div>
        <div v-if="!newTask" @click="editTask" class="btn btn-md btn-info m-2">
          <Icon v-if="!editing" icon="material-symbols:edit-outline-rounded" width="24" height="24" />
          <Icon v-if="editing" icon="material-symbols:check-rounded" width="24" height="24" />        
        </div>
        <div v-if="!newTask" onclick="confirmationModal.showModal()" class="btn btn-md btn-error m-2">
          <Icon icon="material-symbols:delete-outline-rounded" width="24" height="24" />      
        </div>
        <button @click="closeModal" class="btn btn-md btn-ghost m-2" ref="closeDetails">
          <Icon icon="material-symbols:close" width="24" height="24" />
        </button>
      </div>
    </form>

    <div class="border-t-2 flex h-full justify-between">
      <main class="w-full h-full">
        <div class="my-5 m-10 text-xl font-bold text-white ">
          <p v-if="!editing">{{ task.title }}</p>

          <label v-if="editing" class="form-control">
            <div v-if="formErrorMsgs.title" class="label">
              <span class="label-text font-normal text-red-500"> {{ formErrorMsgs.title[0] }} </span>
            </div>
            <TextInput  class="w-full" :class="formErrorMsgs.title ? 'input-error' : ''" v-model="task.title" label="Título de la tarea" :value="task.title"/>
          </label>
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

          <label v-if="editing" class="form-control">
            <div v-if="formErrorMsgs.due_date" class="label">
              <span class="label-text font-normal text-red-500"> {{ formErrorMsgs.due_date[0] }} </span>
            </div>
          </label>
          <vue-tailwind-datepicker 
            :class="formErrorMsgs.due_date ? 'input-error' : ''"
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
          <label v-if="editing" class="form-control">
            <div v-if="formErrorMsgs.family" class="label">
              <span class="label-text font-normal text-red-500"> {{ formErrorMsgs.family[0] }} </span>
            </div>
          </label>
          <SelectInput class="w-full" 
            :class="formErrorMsgs.family ? 'select-error' : ''"
            v-model="task.family"  
            label="Familia" 
            :options="families"
            :selectedValue="task.family"
            :disabled="!editing"
          />

        </div>
        <div class="border-b-2 py-4 ">
          <p>Estado</p>
          <SelectInput class="w-full" 
            v-model="task.state"  
            label="Estado" 
            :options="states"
            :selectedValue="task.state"
            :disabled="!editing"
          />
        </div>
       
       </aside>
      </div>

  </div>

  <ToastSuccess v-if="editSuccess" @click="editSuccess = false" msg="Tarea actualizada correctamente"/>
  <ToastError v-if="editError" @click="editError = false" msg="Error al actualizar tarea"/>
  <ToastError v-if="deleteError" @click="deleteError = false" msg="Error al eliminar tarea"/>


  <dialog id="confirmationModal" class="modal">
    <div class="modal-box">
      <p class="py-4">¿Seguro que quieres eliminar esta tarea?</p>
      <div class="modal-action">
        <form method="dialog">
          <div class="btn w-20 btn-error mr-2" @click="deleteTask">Si</div>
          <button  ref="closeModalBtn" class="btn w-20 btn-accent">No</button>
        </form>
      </div>
    </div>
  </dialog>

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
import ToastSuccess from './notifications/ToastSuccess.vue';
import ToastError from './notifications/ToastError.vue';

export default {
  data(){
    return {
      id: null,
      formatter: {
        date: "YYYY-MM-DD",
        month: "MMM",
      },
      editing: false,
      editSuccess: false,
      addSuccess: false,
      editError: false,
      addError:false,
      deleteError: false,
      formErrorMsgs: {},
      newTask: false,
    }
  },
  components:{
    Icon,
    VueTailwindDatepicker,
    SelectInput,
    TextInput,
    TextareaInput,
    ToastSuccess,
    ToastError
  },
  computed:{
    ...mapState(useStore, ['task', 'states', 'families', 'fromRoute'])
  },
  methods: {
    ...mapActions(useStore, ['resetTask', 'addNewTask', 'setTasks', 'getTaskDetails', 'setFamilies', 'updateTaskDetails', 'deleteSelectedTask']),
    closeModal() {
      this.$router.push(this.fromRoute)
    },
    async editTask(){
      this.editing = !this.editing
        
      if(!this.editing){
        try {     
          this.editSuccess = await this.updateTaskDetails(this.task)
          this.formErrorMsgs = {}
          this.editError = false
          this.editing = false
        } catch (error) {
          this.formErrorMsgs = error.response.data
          this.editError = true
          this.editing = true
        }  
      }
    },
    async deleteTask(){
      try{
        await this.deleteSelectedTask()
        this.$refs.closeModalBtn.click()
        this.deleteError = false
        this.$refs.closeDetails.click()
        this.closeModal()
      } catch(err) {
        console.error(err);
        this.deleteError = true
      }
    },
    async addTask(){
      try{
        await this.addNewTask(this.task)
        this.editing = false
        this.newTask = false
        this.addSuccess = true
        this.$router.push(`/task/${this.task.id}`)
      } catch (err) {
        console.error(err);
        
        this.formErrorMsgs = err.response.data
        
      }
    }
  },
  async beforeMount(){
    const route = useRoute()
    console.log(route);

    if (route.fullPath != '/task/new'){
      this.id = route.params.id
      await this.getTaskDetails(this.id)
    } else {
      this.editing = true
      this.newTask = true
    }
    await this.setFamilies()
  },
  async unmounted(){
    this.resetTask()
    //await this.setTasks({}, 'due_date')
  }


}

</script>