<template>

    <textarea 
        :placeholder="label" 
        class="textarea textarea-bordered textarea-md  h-full">
        {{ modelValue }}
    </textarea>

</template>

<script>

export default {
    props: {
        label: String,
        modelValue: String
    },
    methods: {
        emitValue(event) {
            this.$emit('update:modelValue', event.target.value)
        }
    },
    mounted(){
        console.log(this.label);
        
    }

}

</script>
