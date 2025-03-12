<template>
  <h1>Galerie</h1>
  <v-row>
    <v-col
      v-for="(photo, index) in gallery"
      :key="index"
      cols="4"
      style="padding: 0;"
    >
      <v-img
        :lazy-src="photo.image"
        :src="photo.image"
        aspect-ratio="1"
        cover
        @click="showCarousel = true"
      >
        <template v-slot:placeholder>
          <v-row>
            <v-progress-circular
              color="grey-lighten-5"
              indeterminate
            ></v-progress-circular>
          </v-row>
        </template>
        <v-dialog v-model="showCarousel">
          <dialog-carousel
            :image="photo.image"
            :images="gallery"
            :title="photo.title"
            @isActive="showCarousel = false"
          />
        </v-dialog>
      </v-img>
    </v-col>
  </v-row>
</template>
<script setup lang="ts">
import './assets/css/main.css'
import { useAPI } from "~/composables/useAPI";

const showCarousel = ref(false);

interface ArticleImage {
  image: string;
  title: string;
}

const gallery = ref<ArticleImage[]>([]);

const { error, data } = await useAPI<ArticleImage[]>('load-gallery/', {method: "GET"});

if ( data.value ){
    gallery.value = data.value as ArticleImage[];
}
else if (error.value) {
  console.error("Error loading gallery:", error.value);
}
</script>