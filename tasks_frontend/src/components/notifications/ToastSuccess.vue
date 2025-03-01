<template>

<div class="toast">
  <div class="alert alert-info">
    <span>{{ msg }}</span>
  </div>
</div>

</template>

<script>

export default {
    props: {
        msg: String
    }
}

</script>