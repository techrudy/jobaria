<template>
  <Nav />
  <div class="content-wrap">
    <router-view />
  </div>
  <Footer />
</template>

<script>
import Nav from "./components/Nav";
import Footer from "./components/Footer";
import { checkAuth } from "./functions/checkAuth";

import { ref } from "vue";

export default {
  components: {
    Nav,
    Footer
  },
  data() {
    return {
      token: ref(localStorage.getItem("token")),
      user: ref({})
    };
  },
  async mounted() {
    const {success, error} = await checkAuth(this.token);
    if(!error) this.user = success.user
  }
};
</script>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  outline: none;
  position: relative;
  min-height: 100vh;
}

.content-wrap {

  padding-bottom: 10em;

}
</style>
