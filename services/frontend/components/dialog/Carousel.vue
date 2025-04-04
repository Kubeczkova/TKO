<template>
  <v-card class="article__image">
    <v-card-title>{{ title }}
      <v-icon class="to_right" @click="$emit('isActive', false)">mdi-close</v-icon>
    </v-card-title>
    <v-carousel
      :hide-delimiters="true"
      height="90vh"
    >
      <v-carousel-item
        v-for="(item, i) in images"
        :key="i"
        :src="item.image"
        cover
        class="carousel__image"
      ></v-carousel-item>
    </v-carousel>
  </v-card>
</template>

<script setup lang="ts">
import './assets/css/main.css';

interface ArticleImage {
  image: string;
}

defineProps<{
  image: string;
  images: ArticleImage[];
  title: string;
}>();

defineEmits(["isActive"])
</script>