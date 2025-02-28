<template>
    <main class="container px-40 pt-20 pb-10">
        <header class="flex justify-between mb-5">
            <h1 class="text-3xl text-white font-bold mb-5">Listado de Tareas</h1>
            <RouterLink to="/task/new" @click="openModal" class="btn btn-active btn-primary">
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

import { RouterLink, RouterView } from 'vue-router'
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
        }
    },
    components: {
        TaskOverview,
        TaskListFilters,
        Icon
    },
    computed: {
        ...mapState(useStore, ['families', 'states', 'tasks'])
    },
    watch: {
        filters: {
            handler:  function (newFilters) {
                this.filterTasks(newFilters, this.ordering)
            },
            deep: true
        }
    },
    methods: {
        ...mapActions(useStore, ['filterTasks', 'setTasks', 'setFamilies']),
        async orderTable(orderBy) {
            this.ordering = orderBy
            await this.setTasks(this.filters, this.ordering)    
        },
        openModal(){
            this.$refs.detailsModal.showModal()   
        }
    },
    mounted() {
        this.setTasks({}, 'due_date')
        this.setFamilies({}, 'name')
    }
}

</script>