<template>
  <div class="myjoboffers">
      <div v-if="this.$root.user.company">
        <h1>Mes offres d'emploi</h1>
        <ul v-if="myjoboffers.length" class="myjoboffers__list">
            <li v-for="joboffer in myjoboffers" :key="joboffer.id" class="myjoboffers__list--item">
                <div class="myjoboffers__company">Entreprise {{ joboffer.company.name }}</div>
                <div class="myjoboffers__title">{{ joboffer.title }}</div>
                <div class="myjoboffers__desc">{{ joboffer.description }}</div>
                <div class="myjoboffers__actions">
                    <button class="myjoboffers__actions--delete" v-on:click="deleteOffer(joboffer.id)">Supprimer l'offre</button>
                    <button class="myjoboffers__actions--update" v-on:click="this.$router.push(`/myjoboffers/edit/${joboffer.id}`)">Modifier l'offre</button>
                </div>
            </li>
        </ul>
      </div>
  <div class="myjoboffers" v-if="!this.$root.user.company">Pas le droit d'être ici</div>
  </div>
</template>

<script>
import axios from "axios";
export default {
    name: "GetMyJobOffers",
    data () {
        return {
            joboffers: [],
            myjoboffers: [],
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
        this.joboffers.forEach(joboffer => {
                if(joboffer.company.id == this.user.company.id) this.myjoboffers.push(joboffer)
            });
        return { data }
    },
    methods: {
        async deleteOffer(id) {
            const { data } = await axios.post(
                "http://localhost:8000/api/",
                {
                    query: `mutation DeleteJobOffer($job_offer_id: Int!){
                        deleteJobOffer(
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
            const index = this.myjoboffers.indexOf(this.myjoboffers.filter(offer => offer.id === id)[0])
            if (index > -1) {
                this.myjoboffers.splice(index, 1)
            }
            return { data }
        },
    }
}
</script>

<style lang="scss" scoped>
.myjoboffers {
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
    &__actions {
        display: flex;
        justify-content: space-between;
        &--delete {
            cursor: pointer;
            margin-top: 1em;
            background-color: #d9534f;
            color: white;
            border: none;
            border-radius: 1em;
            padding: 0.5em;
            font-weight: bold;
            outline: none;
        }
        &--update {
            cursor: pointer;
            margin-top: 1em;
            background-color: #f0ad4e;
            color: white;
            border: none;
            border-radius: 1em;
            padding: 0.5em;
            font-weight: bold;
            outline: none;
        }
    }
}
</style>