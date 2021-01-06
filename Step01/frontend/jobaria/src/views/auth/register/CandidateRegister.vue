<template>
  <div class="register">
    <div class="register__form">
      <form v-on:submit.prevent="register()">
        <h2>Inscription Candidat</h2>
        <input
          type="text"
          v-model="input.username"
          placeholder="Nom d'utilisateur"
          required=""
        />
        <input
          type="text"
          v-model="input.firstname"
          placeholder="Prénom"
          required=""
        />
        <input
          type="text"
          v-model="input.lastname"
          placeholder="Nom"
          required=""
        />
        <input type="email" v-model="input.email" placeholder="Email" />
        <input
          type="password"
          v-model="input.password"
          placeholder="Mot de passe"
        />
        <input type="password" placeholder="Répétez le mot de passe" />
        <button type="submit">
          S'inscrire
        </button>
      </form>
      <router-link to="/login/candidate"
        >Déjà un compte ? Je veux me connecter !</router-link
      >
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "CandidateRegister",
  data() {
    return {
      input: {
        username: "",
        firstname: "",
        lastname: "",
        email: "",
        password: "",
      },
    };
  },
  methods: {
    async register() {
      const { data } = await axios.post(
      "http://localhost:8000/api/",
      {
        query: `
          mutation CreateCandidate($username: String!, $password: String!, $email: String!, $firstname: String!, $lastname: String!) {
            createCandidate(
              username: $username
              password: $password
              email: $email
              firstname: $firstname
              lastname: $lastname
            ) {
              success
              error
            }
          }
        `,
      variables: {
          username: this.input.username,
          password: this.input.password,
          firstname: this.input.firstname,
          lastname: this.input.lastname,
          email: this.input.email
      }
      });
        this.$router.push("/login/candidate")
        return { data }
    }
  }
}
</script>

<style lang="scss" scoped>
$form-bg: #f8f4e5;
$form-shadow: #2dad67;
$form-primary-highlight: #2d7049;
$form-secondary-highlight: #2dad67;
$font-size: 14pt;
$font-color: #2a293e;

.register {
  display: flex;
  justify-content: center;
  padding: 1em;
  margin: 1em;

  &__form {
    width: 50%;
    height: 50%;
    background: $form-bg;
    padding: 50px 100px;
    border: 2px solid rgba(0, 0, 0, 1);
    box-shadow: 15px 15px 1px $form-shadow, 15px 15px 1px 2px rgba(0, 0, 0, 1);
  }
}

h2 {
  padding-bottom: 1em;
  font-weight: bold;
}

a {
  text-decoration: none;
  color: #2dad67;
}

input {
  display: block;
  width: 100%;
  font-size: $font-size;
  line-height: $font-size * 2;
  margin-bottom: $font-size * 2;
  border: none;
  border-bottom: 3px solid rgba(0, 0, 0, 1);
  background: $form-bg;
  min-width: 250px;
  padding-left: 5px;
  outline: none;
  color: rgba(0, 0, 0, 1);
}

input:focus {
  border-bottom: 3px solid $form-shadow;
}

button {
  display: block;
  margin: 0 auto;
  line-height: $font-size * 2;
  padding: 0 20px;
  background: $form-shadow;
  letter-spacing: 2px;
  transition: 0.2s all ease-in-out;
  border: none;
  color: white;
  border-radius: 2em;
  font-weight: bold;

  &:hover {
    background: rgba(0, 0, 0, 1);
    color: white;
  }
}
::selection {
  background: $form-secondary-highlight;
}

input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus {
  border-bottom: 3px solid $form-primary-highlight;
  -webkit-text-fill-color: $font-color;
  box-shadow: 0 0 0px 1000px $form-bg inset;
  transition: background-color 5000s ease-in-out 0s;
}
</style>
