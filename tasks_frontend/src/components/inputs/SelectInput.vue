<template>
        <select :disabled="disabled" class="select select-primary w-1/2 max-w-xs" @change="emitValue($event)">
            <option :selected="selectedValue" value="">{{ label }}</option>
            <option :selected="option.id === selectedValue" v-for="option in options" :value="option.id">{{ option.name }}</option>
        </select>
</template>

<script>

export default {
    props:{
        label: String,
        options: Array,
        selectedValue: [String, Number],
        disabled: Boolean
    },
    methods: {
        emitValue(event){
            this.$emit('update:modelValue', event.target.value)
        }
    }
}


</script>