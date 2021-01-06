<template>
  <div class="navigation">
    <router-link to="/"><h1>Jobaria</h1></router-link>
    <ul>
      <router-link v-if="!this.$root.token" to="/login/candidate"
        ><Button text="Connexion Candidat"
      /></router-link>
      <router-link to="/login/professional"
        ><Button v-if="!this.$root.token" text="Connexion Entreprise"
      /></router-link>
      <router-link to="/myjoboffers/create">
      <Button v-if="this.$root.token && this.$root.user.company" text="Créer une offre d'emploi"
      /></router-link>
      <router-link to="/myjoboffers">
      <Button v-if="this.$root.token && this.$root.user.company" text="Mes offres d'emploi"
      /></router-link>
      <router-link to="/profile">
      <Button v-if="this.$root.token" text="Mon profil"
      /></router-link>
      <Button
        v-if="this.$root.token"
        v-on:click="logout()"
        text="Déconnexion"
      />
    </ul>
  </div>
</template>

<script>
import Button from "./Button";

export default {
  components: {
    Button,
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$root.token = null;
      this.$router.push("/");
    },
  },
};
</script>

<style lang="scss" scoped>
.navigation {
  display: grid;
  grid-template-columns: 1fr 1fr;
  padding: 1em;
  h1 {
    color: #2dad67;
  }
  a {
    text-decoration: none
  }
  ul {
    display: flex;
    list-style: none;
    grid-column: 2;
    justify-content: flex-end;
  }
}
</style>
