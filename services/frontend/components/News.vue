<template>
  <h1>Články</h1>
  <v-card>
    <v-row>
    <v-col
      v-for="(article, index) in articles"
      :key="index"
      cols="12"
      md="6"
    >
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-img
            :lazy-src="article.src"
            :src="article.src"
            aspect-ratio="1"
            cover
          >
            <template v-slot:placeholder>
              <v-row>
                <v-progress-circular
                  color="grey-lighten-5"
                  indeterminate
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
        </v-col>
        <v-col
          cols="12"
          md="8"
        >
            <v-row><v-card-title><h2>{{ article.title }}</h2></v-card-title></v-row>
            <v-row><v-card-subtitle><h4>{{ article.autor }}, ({{ article.date}})</h4></v-card-subtitle></v-row>
            <v-row><v-card-text><div class="subtitle">{{ article.desc }}</div></v-card-text></v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
  </v-card>
</template>
<script setup lang="ts">
const articles = [
  {
    autor: "Bebloid Obecný",
    date: "2. 2. 2025",
    title: "David potrolil soutěž",
    src: "https://melbourneentertainmentco.com.au/wp-content/uploads/2020/04/Juan-and-Jess-600x600-profile.jpg",
    desc: "V neděli 2. 2. David potrolil sambu, kde místo tančení lítal jako zmatená včelka. Terka, ačkoliv před soutěží velice zmatkovala a sebepoškozovala se, tak na parketě předvedla výborné představení. Na další trolení se můžeme všichni těšit do Brna na konci tohoto měsíce. "
  },
]
</script>

<style scoped>
h1 {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 3rem;
  color: #333; /* Dark gray */
  text-align: center;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  margin-top: 2rem;
  margin-bottom: 1rem;
}

h2 {
  font-family: 'Playfair Display', serif;
  text-align: center;
  font-size: 1.7rem;
  color: #666; /* Light gray */
}

.subtitle {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 1rem;
  color: #333; /* Dark gray */
}
</style>