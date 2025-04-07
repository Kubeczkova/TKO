<template>
  <h1>Galerie</h1>
  <div class="masonry-gallery">
    <div
      class="masonry-item"
      v-for="(photo, index) in gallery"
      :key="index"
      @click="openCarousel(photo)"
    >
      <v-img
        :src="photo.image"
        :lazy-src="photo.image"
        aspect-ratio=""
        class="article__image rounded-lg"
        cover
      >
        <template #placeholder>
          <v-row justify="center" align="center" style="height: 100px;">
            <v-progress-circular indeterminate color="grey-lighten-1" />
          </v-row>
        </template>
      </v-img>
    </div>
    <v-dialog v-model="showCarousel">
      <dialog-carousel
        v-if="selectedImage"
        :image="selectedImage"
        :images="gallery"
        @isActive="showCarousel = false"
      />
    </v-dialog>
  </div>
</template>
<script setup lang="ts">
import './assets/css/main.css'
import { useAPI } from "~/composables/useAPI";

const showCarousel = ref(false);
const selectedImage = ref<ArticleImage | null>(null);

function openCarousel(photo: ArticleImage) {
  selectedImage.value = photo;
  showCarousel.value = true;
}

interface ArticleImage {
  image: string;
  title: string;
}

const gallery = ref<ArticleImage[]>([]);

loadImages();

async function loadImages(){
  const { error, data } = await useAPI<ArticleImage[]>('load-gallery/', {method: "GET"});

  if ( data.value ){
    gallery.value = data.value as ArticleImage[];
  }
  else if (error.value) {
    console.error("Error loading gallery:", error.value);
  }
}




</script>