<template>
    <h1>Listado de Tareas</h1>
</template>

<script>

export default {
    async mounted(){
        console.log(await this.$api.getAllTasks());
        
    }
}

</script>