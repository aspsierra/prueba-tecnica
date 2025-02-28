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
        <BtnClear tooltip="Eliminar filtros" @clear="clearFilters"/>
    </div>

    <div class="w-full">
        <div class="min-w-max flex justify-end">
            <p class="text-right content-end hover:underline cursor-pointer" @click="orderTable">Fecha de vencimiento</p>
            <Icon :icon="orderIcon" width="24" height="24" />
        </div>
    </div>

</template>

<script>
import BtnClear from '../inputs/BtnClear.vue';
import SelectInput from '../inputs/SelectInput.vue';
import TextInput from '../inputs/TextInput.vue';
import VueTailwindDatepicker from "vue-tailwind-datepicker";
import { Icon } from '@iconify/vue';
import _ from 'lodash';

export default {
    data(){
        return {
            formatter: {
                date: "YYYY-MM_AA",
                month: "MMM",
            },
            order: false,
        }
    },
    props:{
        filters: Object,
        resetFilters: Object,
        families: Array,
        states: Array,
    },
    components: {
        SelectInput,
        TextInput,
        VueTailwindDatepicker,
        BtnClear,
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
        clearFilters(){
            this.$emit('clearFilters')
            Object.assign(this.filters, _.cloneDeep(this.$parent.initialFilters));
            // Object.assign(this.filters, this.resetFilters);
            // console.log(this.filters);
        },
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