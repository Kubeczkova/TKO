<template>
  <v-parallax
    src="public/dark-dance.jpg"
  >
    <div class="d-flex flex-column fill-height justify-center">
      <h1 class="text-white">
        Taneční klub Ostrava
      </h1>
      <h2>
        Naučíme Vás tančit!
      </h2>
    </div>
  </v-parallax>
  <lazy-news :for-all="false"/>
  <lazy-about/>
  <lazy-courses/>
  <lazy-trainers/>
  <lazy-advantages/>
  <lazy-history/>
</template>

<script setup lang="ts">

</script>