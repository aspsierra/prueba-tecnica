<template>

    <select class="select select-primary w-1/2 max-w-xs" @change="emitValue($event)">
        <option selected>{{ label }}</option>
        <option v-for="option in options" :value="option.id">{{ option.name }}</option>
    </select>

</template>

<script>

export default {
    props:{
        label: String,
        options: ArrayBuffer,
    },
    methods: {
        emitValue(event){
            this.$emit('update:modelValue', event.target.value)
        }
    }
}


</script>