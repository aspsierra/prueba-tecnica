<template>

    <SelectInput v-model="selectedFamily" label="Familia" :options="families"/>

</template>

<script>
import SelectInput from '../inputs/SelectInput.vue';

export default {
    data(){
        return {
            selectedFamily: null
        }
    },
    props:{
        families: Array,
    },
    components: {
        SelectInput
    },
    watch: {
        selectedFamily(newVal){
            this.$emit('update:modelValue', newVal)
        }
    }
}

</script>