<template>
  <v-parallax
    class="about__parallax"
    src="public/dark-dance.jpg"
    scale="0.8"
  >
    <v-container id="about">
      <v-card class="about">
        <v-card-title class="about__title">Vítejte v tanečním klubu!</v-card-title>
        <v-card-subtitle class="about__subtitle">Vítejte na webu Tanečního klubu Ostrava!</v-card-subtitle>
        <v-card-text class="about__text">
          Objevte kouzlo tance s námi! Ať už jste začátečník nebo zkušený tanečník, v našem klubu najdete místo, kde se můžete rozvíjet, bavit a sdílet svou vášeň pro pohyb. Nabízíme kurzy pro všechny věkové kategorie, od společenských tanců po moderní styly.
          <br><br>
          Přidejte se k nám a nechte tanec proměnit váš život! 💃🕺
          <br><br>
          👉 Podívejte se na naše kurzy a přihlaste se ještě dnes!
        </v-card-text>
      </v-card>
    </v-container>
  </v-parallax>
</template>

<script setup lang="ts">
import './assets/css/main.css'
</script>