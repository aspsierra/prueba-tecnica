<template>
    <main class="container px-40 pt-20 pb-10">
        <h1 class="text-3xl text-white font-bold mb-5">Listado de Tareas</h1>
        <div>
            <div v-for="task in tasks" class="cursor-pointer border-gray-500 hover:brightness-75 border-b-2 mb-2">
                <h3 class="text-lg">{{ task.title }}</h3>
                <ul>
                    <li class="inline mr-2">{{ task.family.name }}</li>
                    <li class="inline mr-2">{{ task.state_display }}</li>
                    <li class="inline mr-2">{{ task.due_date || 'Sin fecha límite' }}</li>
                </ul>
            </div>
        </div>
    </main>

</template>

<script>

export default {
    data() {
        return {
            tasks: [],
        }
    },
    async mounted(){
        this.tasks = await this.$api.getAllTasks()
        console.log(this.tasks);  
    }
}

</script>