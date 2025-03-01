<template>

    <div class="flex mb-2 gap-2">

        <TextInput v-model="filters.name" label="Nombre de la familia"/>
    </div>

    <div class="w-full">
        <div class="min-w-max flex justify-end">
            <p class="text-right content-end hover:underline cursor-pointer" @click="orderTable">Nombre</p>
            <Icon :icon="orderIcon" width="24" height="24" />
        </div>
    </div>

</template>

<script>
import { Icon } from '@iconify/vue';
import TextInput from '../inputs/TextInput.vue';


export default {
    data(){
        return {
            order: false
        }
    },
    props: {
        filters: Object,
        resetFilters: Object
    },
    components: {
        TextInput,
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
                this.$emit('order', '-name')
            } else {         
                this.$emit('order', 'name')
            console.log(this.filters.ordering);
            }
        }
    }
}

</script>
