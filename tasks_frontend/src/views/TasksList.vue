<template>
    <main class="container px-40 pt-20 pb-10">

        <header class="flex justify-between mb-5">
            <h1 class="text-3xl text-white font-bold mb-5 overflow-ellipsis">
                {{titleFamily ? titleFamily : 'Listado de Tareas'}}
            </h1>
            <RouterLink v-if="!fromFamily" to="/task/new" @click="openModal" class="btn btn-active btn-primary">
                <Icon icon="material-symbols:add-2-rounded" width="24" height="24" />
                Añadir tarea
            </RouterLink>
        </header>

        <TaskListFilters :filters="filters"  :families="families" :states="states"
            @order="orderTable" />

        <div class="mt-5">
            <div v-for="task in tasks" class="cursor-pointer border-gray-500 hover:brightness-75 border-b-2 mb-2">

                <RouterLink :to="`/task/${task.id}`" @click="openModal">
                    <TaskOverview  :task="task"></TaskOverview>
                </RouterLink>
            </div>
        </div>
    </main>

    <dialog ref="detailsModal" class="modal">   
        <RouterView />
    </dialog>

</template>

<script>

import { RouterLink, RouterView, useRoute } from 'vue-router'
import TaskListFilters from '@/components/filters/TaskListFilters.vue';
import TaskOverview from '@/components/TaskOverview.vue';
import { mapActions, mapState } from 'pinia';
import { useStore } from '@/stores/store';
import { Icon } from '@iconify/vue';


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
        }
    },
    props: ['id'],
    components: {
        TaskOverview,
        TaskListFilters,
        Icon
    },
    computed: {
        ...mapState(useStore, ['families', 'states', 'tasks', 'fromRoute'])
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
        ...mapActions(useStore, ['filterTasks', 'setTasks', 'setFamilies', 'setFromRoute']),
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
        }
    
    },
    async mounted() {
        console.log('mounted');
    }
}

</script>