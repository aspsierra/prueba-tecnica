<template>
    <label class="input input-bordered flex items-center gap-2">
        <input type="text" class="grow" :placeholder="label" @input="emitValue($event)" :value="modelValue"/>
    </label>
</template>

<script>

export default{
    props: {
        label: String,
        modelValue: String
    },
    methods: {
        emitValue(event){
            this.$emit('update:modelValue', event.target.value)
        }
    }
}

</script>