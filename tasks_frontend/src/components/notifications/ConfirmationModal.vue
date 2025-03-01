<template>

    <dialog ref="confirmationModal" class="modal">
        <div class="modal-box">
        <p class="py-4">{{ label }}</p>
        <div class="modal-action">
            <form method="dialog">
                <div class="btn w-20 btn-error mr-2" @click="$emit('accept')">Si</div>
                <button ref="closeModalBtn" @click="$emit('cancel')" class="btn w-20 btn-accent">No</button>
            </form>
        </div>
        </div>
    </dialog>

</template>

<script>

export default {

    props: {
        label: String,
        show: Boolean
    },
    watch: {
        show(state){
            if(state) {
                this.$refs.confirmationModal.showModal()
            } else {
                this.$refs.closeModalBtn.click()
            }
        }
    }

}

</script>