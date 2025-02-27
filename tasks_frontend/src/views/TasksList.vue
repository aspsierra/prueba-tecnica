<template>
    <main class="container px-40 pt-20 pb-10">
        <h1 class="text-3xl text-white font-bold mb-5">Listado de Tareas</h1>

        <TaskListFilters 

            :filters="filters" 
            :resetFilters="initialFilters"
            :families="families" 
            :states="states"
            @clearFilters="resetFilters"
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
                ordering: 'due_date'
            },
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
        this.tasks = await this.$api.getAllTasks(this.filters)
        this.families = await this.$api.getFamilies()
        this.states = await this.$api.getStates()
    },
    watch: {
        filters: {
            handler: _.debounce(async function (newFilters) {
                this.tasks = await this.$api.getAllTasks(newFilters)
            }, 300),
            deep: true
        }
    },
    methods:{
        resetFilters(){
            Object.assign(this.filters, _.cloneDeep(this.initialFilters));
        }
    }
}

</script>