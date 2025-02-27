<template>

    
        <h3 class="text-lg">{{ task.title }}</h3>
        <ul>
            <li class="inline mr-2 text-sm">{{ task.family.name }}</li>
            <li class="inline mr-2 text-sm">{{ task.state_display }}</li>
            <li class="inline mr-2 text-sm">{{ formatDate(task.due_date) || 'Sin fecha límite' }}</li>
        </ul>

</template>

<script>

export default {
    props: {
        task: Object,
    },
    methods: {
        formatDate(date){   
            return new Intl.DateTimeFormat("es-ES",).format(new Date(date))
        },
        openModal(){
            console.log(detailsModal);
            
        }

    }
}

</script>