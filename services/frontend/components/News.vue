<template v-if="articles">
  <h1 id="article">Aktuality</h1>
  <h2>Přečtěte si aktuality z našeho klubu</h2>
    <v-row class="articles">
      <v-col
        v-for="article in articles"
        :key="article.id"
        cols="12"
        md="6"
      >
      <v-card class="article">
        <v-row class="article__title">{{ article.title }}</v-row>
        <v-row>
          <v-col>
            <v-img
              :lazy-src="article.image"
              :src="article.image"
              aspect-ratio="1"
              class="article__image"
              @click="showCarousel = true"
            >
              <template v-slot:placeholder>
                <v-row justify="center" align="center" class="fill-height">
                  <v-progress-circular color="grey-lighten-5" indeterminate></v-progress-circular>
                </v-row>
              </template>
              <v-dialog v-model="showCarousel">
                <dialog-carousel
                  :image="article.image"
                  :images="article.images"
                  :title="article.title"
                  @isActive="showCarousel = false"
                />
              </v-dialog>
            </v-img>
          </v-col>
          <v-col
            cols="12"
            md="8"
          >

            <v-row class="article__text">{{ article.content }}</v-row>
          </v-col>
        </v-row>
            <v-row class="article__sign">Dne {{ article.date}}, {{ article.author }}</v-row>
      </v-card>
    </v-col>
  </v-row>
  <v-btn to="/aktuality" class="show_more" v-if="!props.forAll">
    <v-icon icon="mdi-chevron-down"/>Další aktuality<v-icon icon="mdi-chevron-down"/>
  </v-btn>
</template>
<script setup lang="ts">
import './assets/css/main.css'
import { useAPI } from "~/composables/useAPI";

const showCarousel = ref(false);

const props = defineProps<{
  forAll: boolean
}>();

interface ArticleImage {
  image: string;
}

interface Article {
  id: number;
  title: string;
  image: string;
  images: ArticleImage[];
  date: string;
  content: string;
  author: string;
}

const articles = ref<Article[]>([]);

const endpoint = props.forAll ? 'load-all-articles/' : 'load-articles/';

const { error, data } = await useAPI<Article[]>(endpoint, {method: "GET"});

if ( data.value ){
    articles.value = data.value;
}
else if (error.value) {
  console.error("Error loading articles:", error.value);
}

</script>