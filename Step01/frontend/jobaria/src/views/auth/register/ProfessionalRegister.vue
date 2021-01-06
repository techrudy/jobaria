<template>
  <div class="register">
    <div class="register__form">
      <form v-on:submit.prevent="register()">
        <h2>Inscription Professionnel</h2>
        <div class="register__form--company">
          <h3>Enregistrer mon entreprise</h3>
          <input
            type="text"
            v-model="company_input.name"
            placeholder="Nom de l'entreprise"
            required=""
          />
          <label for="desc">Description de l'entreprise</label>
          <textarea v-model="company_input.description" id="desc" name="desc"></textarea>
        </div>
        <div class="register__form--professional">
          <h3>Enregistrer mes identifiants</h3>
          <input
            type="text"
            v-model="professional_input.username"
            placeholder="Nom d'utilisateur"
            required=""
          />
          <input
            type="text"
            v-model="professional_input.firstname"
            placeholder="Prénom"
            required=""
          />
          <input
            type="text"
            v-model="professional_input.lastname"
            placeholder="Nom"
            required=""
          />
          <input type="email" v-model="professional_input.email" placeholder="Email" />
          <input
            type="password"
            v-model="professional_input.password"
            placeholder="Mot de passe"
          />
          <input type="password" placeholder="Répétez le mot de passe" />
        </div>
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
      professional_input: {
        username: "",
        firstname: "",
        lastname: "",
        email: "",
        password: "",
        company_id: 0
      },
      company_input: {
        name: "",
        description: "",
      },
    };
  },
  methods: {
    async register() {

      const registerCompany = async cb => {
        const { data } = await axios.post(
        "http://localhost:8000/api/", {
          query: `
            mutation CreateCompany($name: String!, $description: String!) {
              createCompany(
                name: $name
                description: $description
              ) {
                success {
                  msg
                  company {
                    id
                  }
                }
                error
              }
            }
          `,
          variables: {
            name: this.company_input.name,
            description: this.company_input.description,
          }
        });

        this.professional_input.company_id = data.data.createCompany.success.company.id;

        cb();

        return { data };
      }

      const registerProfessional = async () =>  await axios.post(
        "http://localhost:8000/api/",
        {
          query: `
            mutation CreateProfessional($username: String!, $password: String!, $email: String!, $firstname: String!, $lastname: String!, $company_id: ID!) {
              createProfessional(
                username: $username
                password: $password
                email: $email
                firstname: $firstname
                lastname: $lastname
                company_id: $company_id
              ) {
                success
                error
              }
            }
          `,
        variables: {
            username: this.professional_input.username,
            password: this.professional_input.password,
            firstname: this.professional_input.firstname,
            lastname: this.professional_input.lastname,
            email: this.professional_input.email,
            company_id: this.professional_input.company_id,
        }
        });

        
      registerCompany(() => {
        registerProfessional()
      });

      this.$router.push("/login/professional")
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

label {
  font-weight: bold;
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

textarea {
  display: block;
  width: 100%;
  font-size: $font-size;
  line-height: $font-size * 2;
  margin-bottom: $font-size * 2;
  border: 3px solid black;
  background: rgb(230, 229, 229);
  min-width: 250px;
  padding-left: 5px;
  outline: none;
  color: black;
  margin-top: 1em;
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
