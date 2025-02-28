<template>

    <div class="flex mb-2 gap-2">

        <SelectInput v-model="filters.family" label="Familia" :options="families"/>
        <SelectInput v-model="filters.state" label="Estado" :options="states"/>
        <TextInput v-model="filters.title" label="Nombre de la tarea"/>
        <vue-tailwind-datepicker 
            v-model="filters.due_date" 
            class="w-1/2 max-w-xs h-full" 
            :formatter="formatter"
            :shortcuts="false"
            i18n="es"
            placeholder="Fecha de vencimiento"
            separator=" a "
            as-single use-range
        />
    </div>

    <div class="w-full">
        <div class="min-w-max flex justify-end">
            <p class="text-right content-end hover:underline cursor-pointer" @click="orderTable">Fecha de vencimiento</p>
            <Icon :icon="orderIcon" width="24" height="24" />
        </div>
    </div>

</template>

<script>
import SelectInput from '../inputs/SelectInput.vue';
import TextInput from '../inputs/TextInput.vue';
import VueTailwindDatepicker from "vue-tailwind-datepicker";
import { Icon } from '@iconify/vue';
import _ from 'lodash';

export default {
    data(){
        return {
            formatter: {
                date: "YYYY-MM-DD",
                month: "MMM",
            },
            order: false,
        }
    },
    props:{
        filters: Object,
        families: Array,
        states: Array,
    },
    components: {
        SelectInput,
        TextInput,
        VueTailwindDatepicker,
        Icon
    },
    computed:{
        orderIcon(){
            if(this.order) {
                return 'material-symbols:arrow-downward'
            }
            return 'material-symbols:arrow-upward'
        }
    },
    methods: {
        orderTable(){
            this.order = !this.order
            if(this.order) {
                this.$emit('order', '-due_date')
            } else {         
                this.$emit('order', 'due_date')
            }            
        }
    },
}

</script>