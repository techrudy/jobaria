<template>
  <div class="profile">
      <Card v-if="user" :user="user"/>
  </div>
</template>

<script>
import { checkAuth } from "../../functions/checkAuth"
import Card from "../../components/Card"
export default {
  name: "UserProfile",
  components: {
    Card
  },
  data () {
    return {
      user: {}
    }
  },
  async mounted() {
    const user = await checkAuth(this.$root.token);
    this.user = user.success.user
    this.$root.user = this.user
  } 
}
</script>

<style></style>
