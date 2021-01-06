<template>
  <div class="jobboard">
    <h1>Les offres actuelles sur Jobaria</h1>
    <ul class="jobboard__list">
      <li v-for="joboffer in joboffers" :key="joboffer.id" class="jobboard__list--item">
        <div class="jobboard__head">
          <div class="jobboard__company">Entreprise {{ joboffer.company.name }}</div>
          <div class="jobboard__title">{{ joboffer.title }}</div>
          <div class="jobboard__desc">{{ joboffer.description }}</div>
        </div>
        <div class="jobboard__footer">
            <Button v-if="user.id && !user.company" text="Candidater" :value="joboffer.id" v-on:click="(e) => applyJobOffer(e.target.value)"/>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import Button from "./Button"
export default {
  name: "JobBoard",
  components: {
    Button,
  },
  data() {
    return {
      joboffers: [],
      user: {}
    }
  },
  async mounted() {
    const { data } = await axios.post(
      "http://localhost:8000/api/",
    {
      query: `query {
        jobOffers {
          id
                title
                description
                company {
                  id
                    name
                    description
                    created_at
                    updated_at
                }
                created_at
                updated_at
            }
        }`
    }
    );
    this.joboffers = data.data.jobOffers
    this.user = this.$root.user
  },
  methods: {
    async applyJobOffer(id) {
      const { data } = await axios.post(
        "http://localhost:8000/api/",
            {
                query: `mutation ApplyJobOffer($job_offer_id: ID!) {
                    applyJobOffer(
                        job_offer_id: $job_offer_id
                    ) {
                        success
                        error
                    }
                }`,
                variables: {
                    job_offer_id: id
                }
            }, {
              headers: {
                Authorization: this.$root.token
              }
            }
        );
      return { data }
    }
  }
}
</script>

<style lang="scss" scoped>
.jobboard {
  padding: 1em;
  &__list {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    list-style: none;
    gap: 3em;
    padding-top: 3em;
    &--item {
      background-color: white;
      padding: 1em;
      border-radius: 1em;
      box-shadow: 1px 0 8px rgba($color: #000000, $alpha: 0.5);
      font-weight: bold;
      text-align: left;
    }
  }
  &__head {
    padding-bottom: 1em;
  }
  &__footer {
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;
    align-content: flex-end;
  }
  &__company {
    padding-bottom: 1em;
  }
  &__title {
    text-align: center;
    font-size: 2em;
  }
  &__desc {
    padding-top: 3em;
  }
}
</style>