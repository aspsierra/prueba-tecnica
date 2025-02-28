<template>
    <main class="container px-40 pt-20 pb-10">
        <h1 class="text-3xl text-white font-bold mb-5">Listado de Tareas</h1>

        <TaskListFilters :filters="filters" :resetFilters="initialFilters" :families="families" :states="states"
            @clearFilters="resetFilters" @order="orderTable" />

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
        resetFilters() {
            Object.assign(this.filters, _.cloneDeep(this.initialFilters));
        },
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