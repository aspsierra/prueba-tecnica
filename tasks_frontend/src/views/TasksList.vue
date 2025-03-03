<template>
    <main class="container px-40 pt-20 pb-10">

        <header class="flex justify-between mb-5">
            <h1 class="text-3xl  font-bold mb-5 overflow-ellipsis">
                {{titleFamily ? titleFamily : 'Listado de Tareas'}}
            </h1>
            <RouterLink v-if="!fromFamily" to="/task/new" @click="openModal" class="btn btn-active btn-primary"
                :class="user.pk ? '': 'btn-disabled'"
                >
                <Icon icon="material-symbols:add-2-rounded" width="24" height="24" />
                Añadir tarea
            </RouterLink>
        </header>

        <TaskListFilters :filters="filters"  :families="families" :states="states"
            @order="orderTable" />

        <div class="mt-5">
            <div v-for="task in tasks" class="cursor-pointer border-gray-500 hover:brightness-75 border-b-2 mb-2 flex justify-between group">
                <RouterLink :to="`/task/${task.id}`" @click="openModal">
                    <TaskOverview  :task="task"></TaskOverview>
                </RouterLink>
                <div v-if="user.pk" @click="confirmDelete(task.id)" class="hidden group-hover:inline-flex btn btn-sm btn-outline btn-error m-2">
                    <Icon icon="material-symbols:delete-outline-rounded" width="24" height="24" />      
                </div>
            </div>
        </div>
    </main>

    <dialog ref="detailsModal" class="modal">   
        <RouterView />
    </dialog>

    <ConfirmationModal 
        :show="showConfirmation" 
        label="¿Seguro que quieres eliminar esta tarea?"
        @cancel="showConfirmation=false"
        @accept="deleteTask"
    />

</template>

<script>

import { RouterLink, RouterView, useRoute } from 'vue-router'
import TaskListFilters from '@/components/filters/TaskListFilters.vue';
import TaskOverview from '@/components/TaskOverview.vue';
import { mapActions, mapState } from 'pinia';
import { useStore } from '@/stores/store';
import { Icon } from '@iconify/vue';
import ConfirmationModal from '@/components/notifications/ConfirmationModal.vue';


export default {
    data() {
        return {
            filters: {
                family: null,
                title: null,
                state: null,
                due_date: {
                    after: null,
                    before: null,
                },

            },
            ordering: 'due_date',
            titleFamily:'',
            fromFamily: false,
            showConfirmation: false,
            taskToDelete: null,
        }
    },
    props: ['id'],
    components: {
        TaskOverview,
        TaskListFilters,
        Icon,
        ConfirmationModal
    },
    computed: {
        ...mapState(useStore, ['families', 'states', 'tasks', 'fromRoute', 'user'])
    },
    watch: {
        filters: {
            handler:  function (newFilters) {
                this.filterTasks(newFilters, this.ordering)
            },
            deep: true
        },
        id: {
            handler: async function(newId) {
                console.log('aca', this.$route.path);
                
                this.fetchData(newId)
            },
            immediate: true,
        },
        async $route(newRoute) {  
            console.log(newRoute);
                    
            if (!newRoute.path.startsWith('/task/')) {
                this.$refs.detailsModal.close() 

                this.fetchData(newRoute.params.id)
            }
        }
    },
    methods: {
        ...mapActions(useStore, ['filterTasks', 'setTasks', 'setFamilies', 'setFromRoute', 'deleteSelectedTask']),
        async orderTable(orderBy) {
            this.ordering = orderBy
            await this.setTasks(this.filters, this.ordering)    
        },
        openModal(){
            this.$refs.detailsModal.showModal()   
        },
        async fetchData(id) {
            if (!this.$route.path.startsWith('/task/')) {
                if (id === undefined) {
                    console.log('indefinido');
                    await this.setFamilies({}, 'name')
                    await this.setTasks({}, 'due_date')
                    this.setFromRoute('/')
                    this.fromFamily = false
                    this.titleFamily = ''

                } else {
                    console.log('Cargando tareas para:', id);
                    await this.setFamilies({ id: id }, 'name')
                    await this.setTasks({ family: id }, 'due_date')
                    this.titleFamily = this.families[0].name
                    this.setFromRoute(this.$route.path)
                    this.fromFamily = true
                }
            }
        },
        confirmDelete(taskId){
            this.showConfirmation = true
            this.taskToDelete = taskId
        },
        async deleteTask(){
            try{
                await this.deleteSelectedTask(this.taskToDelete)
                this.showConfirmation = false
            } catch(err) {
                console.error(err);
                this.deleteError = true
            }
        }
    
    },
    async mounted() {
        console.log('mounted');
    }
}

</script>