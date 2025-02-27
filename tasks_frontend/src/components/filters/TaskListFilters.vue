<template>

    <SelectInput v-model="filters.family" label="Familia" :options="families"/>
    <TextInput v-model="filters.title" label="nombre de la tarea"/>
    <vue-tailwind-datepicker 
        v-model="filters.due_date" 
        class="w-1/2 max-w-xs" 
        :formatter="formatter"
        :shortcuts="false"
        i18n="es"
        placeholder="Fecha de vencimiento"
        separator=" a "
        as-single use-range
        @input="console.log('ajjjj')"
    />

</template>

<script>
import SelectInput from '../inputs/SelectInput.vue';
import TextInput from '../inputs/TextInput.vue';
import VueTailwindDatepicker from "vue-tailwind-datepicker";

export default {
    data(){
        return {
            selectedFamily: null,
            title: '',
            formatter: {
                date: "DD MMM YYYY",
                month: "MMM",
            }
        }
    },
    props:{
        filters: Object,
        families: Array
    },
    components: {
        SelectInput,
        TextInput,
        VueTailwindDatepicker
    },
}

</script>