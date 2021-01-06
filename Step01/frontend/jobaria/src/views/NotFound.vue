<template>
  <div class="notfound">
      <h1 v-if="!isRaph" v-on:click="() => isRaph = !isRaph">404</h1>
      <img class="notfound__raph" v-if="isRaph" src="../assets/raph.jpg">
  </div>
</template>

<script>
export default {
name: "NotFound",
data() {
  return {
    isRaph: false
  }
},
}
</script>

<style lang="scss" scoped>
.notfound {
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;
    height: 50vh;

    h1 {
      color: #2dad67;
      font-size: 10em;
      cursor: default;
    }

  &__raph {

    width: 18%;
    border: 5px dashed #2dad67;

  }
}
</style>