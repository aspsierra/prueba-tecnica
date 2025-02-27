<template>
    <main class="container px-40 pt-20 pb-10">
        <h1 class="text-3xl text-white font-bold mb-5">Listado de Tareas</h1>

        <TaskListFilters :filters="filters" :families="families"/>
        
        <div>
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
            filters: {
                family: null,
                title: null,
                state: null,
                due_date: null,
            },
        }
    },
    components: {
        TaskOverview,
        TaskListFilters
    },
    async mounted(){
        this.tasks = await this.$api.getAllTasks()
        this.families = await this.$api.getFamilies()
    },
    watch: {
        filters: {
            handler: _.debounce(async function (newFilters) {
                this.tasks = await this.$api.getAllTasks(newFilters)
            }, 500),
            deep: true
        }
    
    }
}

</script>