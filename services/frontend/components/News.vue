<template>
  <h1>Aktuality</h1>
  <h2>Přečtěte si aktuality z našeho klubu</h2>
    <v-row>
      <v-col
        v-for="(article, index) in articles"
        :key="index"
        cols="12"
        md="6"
      >
      <v-card class="article">
        <v-row>
          <v-col>
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
            <v-row class="article__title">{{ article.title }}</v-row>
            <v-row class="article__date">{{ article.date}}</v-row>
            <v-row class="article__text">{{ article.desc }}</v-row>
            <v-row class="article__sign">{{ article.autor }}</v-row>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-row>
</template>
<script setup lang="ts">
import './assets/css/main.css'

const articles = [
  {
    autor: "Bebloid Obecný",
    date: "2. 2. 2025",
    title: "David potrolil soutěž",
    src: "https://melbourneentertainmentco.com.au/wp-content/uploads/2020/04/Juan-and-Jess-600x600-profile.jpg",
    desc: "V neděli 2. 2. David potrolil sambu, kde místo tančení lítal jako zmatená včelka. Terka, ačkoliv před soutěží velice zmatkovala a sebepoškozovala se, tak na parketě předvedla výborné představení. Na další trolení se můžeme všichni těšit do Brna na konci tohoto měsíce. "
  },
  {
    autor: "Bebloid Obecný",
    date: "2. 2. 2025",
    title: "David potrolil soutěž",
    src: "https://melbourneentertainmentco.com.au/wp-content/uploads/2020/04/Juan-and-Jess-600x600-profile.jpg",
    desc: "V neděli 2. 2. David potrolil sambu, kde místo tančení lítal jako zmatená včelka. Terka, ačkoliv před soutěží velice zmatkovala a sebepoškozovala se, tak na parketě předvedla výborné představení. Na další trolení se můžeme všichni těšit do Brna na konci tohoto měsíce. "
  },
]
</script>