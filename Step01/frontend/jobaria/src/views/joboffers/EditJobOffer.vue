<template>
  <div class="createjoboffer">
      <div class="createjoboffer__form">
      <form v-on:submit.prevent="editJobOffer()">
        <h2>Modifier mon offre d'emploi</h2>
          <input
            type="text"
            v-model="input.title"
            placeholder="Titre de l'offre d'emploi"
            required=""
          />
          <input
            type="text"
            v-model="input.description"
            placeholder="Description de l'offre d'emploi"
            required=""
          />
        <button type="submit">
          Enregistrer
        </button>
      </form>
    </div>
  </div>
</template>

<script>

import axios from "axios";

export default {
    name: "EditJobOffer",
    data () {
        return {
            input: {
                title: "",
                description: ""
            }
        }
    },
    async mounted() {
      const { data } = await axios.post(
        "http://localhost:8000/api/",
        {
          query: `query JobOffer($job_offer_id: Int!) {
            jobOffer(
              job_offer_id: $job_offer_id
            ) {
              success {
                id
                title
                description
              }
              error
            }
          }`,
          variables: {
            job_offer_id: parseInt(this.$route.params.id)
          }
        }, {
          headers: {
            Authorization: this.$root.token
          }
        }
      );
      this.input.title = data.data.jobOffer.success.title
      this.input.description = data.data.jobOffer.success.description
      return { data }
    }, 
    methods: {
        async editJobOffer() {
            const { data } = await axios.post(
            "http://localhost:8000/api/",
                {
                    query: `mutation UpdateJobOffer($job_offer_id: Int!, $title: String!, $description: String!) {
                        updateJobOffer(
                            job_offer_id: $job_offer_id
                            title: $title
                            description: $description
                        ) {
                            success
                            error
                        }
                    }`,
                    variables: {
                        title: this.input.title,
                        description: this.input.description,
                        job_offer_id: parseInt(this.$route.params.id)
                    }
                }, {
                  headers: {
                    Authorization: this.$root.token
                  }
                }
            );
            this.$router.push("/myjoboffers")
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

.createjoboffer {
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