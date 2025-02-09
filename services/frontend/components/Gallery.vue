<template>
  <h1>Galerie</h1>
  <v-row>
    <v-col
      v-for="(photo, index) in photos"
      :key="index"
      cols="4"
      style="padding: 0;"
    >
      <v-img
        :lazy-src="photo.src"
        :src="photo.src"
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
  </v-row>
</template>
<script setup lang="ts">

const photos = [
  {src: "https://www.danceus.org/parse/files/Bjy5anNVI0Q81M8bmrwIiuU20x4kepQTxzDBfqpR/70d831b8f51edc1f6e1a4320d52f164b_latin-dance.jpg"},
  {src: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"},
  {src: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"},
  {src: "https://danceostrava.cz/wp-content/uploads/2021/10/IMG_5203-scaled.jpg"},
  {src: "https://cdn11.bigcommerce.com/s-07991/product_images/uploaded_images/latin-dance.jpg"},
  {src: "https://www.danceus.org/parse/files/Bjy5anNVI0Q81M8bmrwIiuU20x4kepQTxzDBfqpR/70d831b8f51edc1f6e1a4320d52f164b_latin-dance.jpg"},
  {src: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"},
  {src: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"},
  {src: "https://danceostrava.cz/wp-content/uploads/2021/10/IMG_5203-scaled.jpg"},
  {src: "https://cdn11.bigcommerce.com/s-07991/product_images/uploaded_images/latin-dance.jpg"},
  {src: "https://www.danceus.org/parse/files/Bjy5anNVI0Q81M8bmrwIiuU20x4kepQTxzDBfqpR/70d831b8f51edc1f6e1a4320d52f164b_latin-dance.jpg"},
  {src: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"},
  {src: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"},
  {src: "https://danceostrava.cz/wp-content/uploads/2021/10/IMG_5203-scaled.jpg"},
  {src: "https://cdn11.bigcommerce.com/s-07991/product_images/uploaded_images/latin-dance.jpg"},
  {src: "https://www.danceus.org/parse/files/Bjy5anNVI0Q81M8bmrwIiuU20x4kepQTxzDBfqpR/70d831b8f51edc1f6e1a4320d52f164b_latin-dance.jpg"},
  {src: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"},
  {src: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"},
  {src: "https://danceostrava.cz/wp-content/uploads/2021/10/IMG_5203-scaled.jpg"},
  {src: "https://cdn11.bigcommerce.com/s-07991/product_images/uploaded_images/latin-dance.jpg"},
  {src: "https://www.danceus.org/parse/files/Bjy5anNVI0Q81M8bmrwIiuU20x4kepQTxzDBfqpR/70d831b8f51edc1f6e1a4320d52f164b_latin-dance.jpg"},
  {src: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"},
  {src: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"},
  {src: "https://danceostrava.cz/wp-content/uploads/2021/10/IMG_5203-scaled.jpg"},
  {src: "https://cdn11.bigcommerce.com/s-07991/product_images/uploaded_images/latin-dance.jpg"},
  {src: "https://www.danceus.org/parse/files/Bjy5anNVI0Q81M8bmrwIiuU20x4kepQTxzDBfqpR/70d831b8f51edc1f6e1a4320d52f164b_latin-dance.jpg"},
  {src: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"},
  {src: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"},
  {src: "https://danceostrava.cz/wp-content/uploads/2021/10/IMG_5203-scaled.jpg"},
  {src: "https://cdn11.bigcommerce.com/s-07991/product_images/uploaded_images/latin-dance.jpg"},
]

</script>

<style scoped>
h1 {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 3rem;
  color: #333; /* Dark gray */
  text-align: center;
  margin-bottom: 1rem;
  margin-top: -2rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1); /* Subtle shadow */
}
</style>