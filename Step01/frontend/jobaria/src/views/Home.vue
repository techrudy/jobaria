<template>
  <div class="home">
    <JobBoard />
  </div>
</template>

<script>
// @ is an alias to /src
import JobBoard from "../components/JobBoard"
export default {
  name: "Home",
  components: {
    JobBoard,
  }
};
</script>

<style lang="scss" scoped>

.home {

  text-align: center;

}

</style>
