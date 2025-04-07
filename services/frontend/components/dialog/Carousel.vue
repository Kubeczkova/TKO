<template>
  <v-card class="article__image">
    <v-card-title>
      {{ images[model] && images[model].title }}
      <v-icon class="to_right" @click="$emit('isActive', false)">mdi-close</v-icon>
    </v-card-title>

    <v-carousel
      v-model="model"
      :hide-delimiters="true"
      height="90vh"
    >
      <v-carousel-item
        v-for="(item, i) in props.images"
        :key="i"
        :src="item.image"
        cover
        class="carousel__image"
      />
    </v-carousel>
  </v-card>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import './assets/css/main.css';

interface ArticleImage {
  image: string;
  title: string;
}

const props = defineProps<{
  image: ArticleImage;
  images: ArticleImage[];
}>();

defineEmits(["isActive"]);

const model = ref(0);

watch(() => props.image, (newImage) => {
  const index = props.images.findIndex((img) => img.image === newImage.image);
  if (index !== -1) model.value = index;
}, { immediate: true });
</script>