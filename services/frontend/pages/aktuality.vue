<template v-if="articles">
  <h1 id="article">Aktuality</h1>
  <h2>Přečtěte si aktuality z našeho klubu</h2>
    <v-row>
      <v-col
        v-for="article in articles"
        :key="article.id"
        cols="12"
        md="6"
      >
      <v-card class="article">
        <v-row>
          <v-col>
            <v-img
              :lazy-src="article.image"
              :src="article.image"
              aspect-ratio="1"
              cover
              class="article__image"
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
            <v-row class="article__text">{{ article.content }}</v-row>
            <v-row class="article__sign">{{ article.author }}</v-row>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import './assets/css/main.css'

import {useAPI} from "~/composables/useAPI";

interface Article {
  id: number;
  title: string;
  image: string;
  date: string;
  content: string;
  author: string;
}

const articles = ref<Article[]>([]);

const { error, data } = await useAPI('load-all-articles/', {method: "GET"});

if ( data.value ){
    articles.value = data.value as Article[];
}
else if (error.value) {
  console.error("Error loading articles:", error.value);
}
</script>