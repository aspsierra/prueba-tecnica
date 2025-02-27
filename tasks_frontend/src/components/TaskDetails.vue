<template>

  <div class="modal-box">
    <form method="dialog">
      <button @click="" class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
    </form>
    <h3 class="text-lg font-bold">Hello!</h3>
    <p class="py-4">Press ESC key or click on ✕ button to close</p>
  </div>

</template>

<script>
import { useRoute } from 'vue-router';




export default {
  data(){
    return {
      id: null,
      task: {}
    }
  },
  updated(){
    const route = useRoute()
    this.id = route.params.id
    console.log(route.params.id);
    
  },
  methods: {
    
  }
}

</script>