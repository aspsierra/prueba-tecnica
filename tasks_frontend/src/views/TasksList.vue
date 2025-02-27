<template>
    <main class="container px-40 pt-20 pb-10">
        <h1 class="text-3xl text-white font-bold mb-5">Listado de Tareas</h1>

        <TaskListFilters 
            :filters="filters" 
            :resetFilters="initialFilters"
            :families="families" 
            :states="states"
            @clearFilters="resetFilters"
            @order="orderTable"
        />
        
        <div class="mt-5">
            <div v-for="task in tasks" class="cursor-pointer border-gray-500 hover:brightness-75 border-b-2 mb-2">      
                <TaskOverview :task="task"></TaskOverview>
            </div>
        </div>
    </main>

</template>

<script>

import TaskListFilters from '@/components/filters/TaskListFilters.vue';
import TaskOverview from '@/components/TaskOverview.vue';
import _ from 'lodash'


export default {
    data() {
        return {
            tasks: [],
            families: [],
            states:[],
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
            initialFilters: {
                family: null,
                title: null,
                state: null,
                due_date: {
                    after: null,
                    before: null,
                },
                ordering: 'due_date'
            },

        }
    },
    components: {
        TaskOverview,
        TaskListFilters
    },
    async mounted(){
        this.fetchTasks()
        this.families = await this.$api.getFamilies()
        this.states = await this.$api.getStates()
    },
    watch: {
        filters: {
            handler: _.debounce(async function (newFilters) {
                await this.fetchTasks(newFilters, this.ordering)
            }, 300),
            deep: true
        }
    },
    methods:{
        async fetchTasks(filters=this.filters, order=this.ordering) {
            this.tasks = await this.$api.getAllTasks(filters, order)
        },
        resetFilters(){
            Object.assign(this.filters, _.cloneDeep(this.initialFilters));
        },
        async orderTable(orderBy){
            this.ordering= orderBy 
            await this.fetchTasks()
            
        },
    }
}

</script>