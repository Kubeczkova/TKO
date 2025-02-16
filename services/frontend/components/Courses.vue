<template>
  <h1 id="courses">Kurzy - cena</h1>
  <h2>Vyberte, co Vám nejlépe vyhovuje</h2>

  <v-row>
    <v-col
        cols="12"
        md="4"
        v-for="course in courses"
        :key="course.id"
    >
      <v-card class="pricing-box">
        <h3>{{ course.name }}</h3>
        <v-card-subtitle><div class="pricing__subtitle">{{ course.time }}</div></v-card-subtitle>
        <v-card-title><div class="pricing__price">{{ course.price }}</div></v-card-title>
        <v-card-subtitle v-if="course.desc"><div class="pricing__subtitle">{{ course.desc }}</div></v-card-subtitle>
      </v-card>
    </v-col>
  </v-row>
</template>
<script setup lang="ts">
import './assets/css/main.css'

const courses = [
  {id: 1, name: "Sportovní taneční klub", time: "24 hodin/měsíc", price: "600 Kč", desc: false},
  {id: 2, name: "Individuální lekce", time: "60min / taneční pár", price: "500 Kč", desc: "Pro veřejnost"},
  {id: 3, name: "Volný trénink s lektorem", time: "60min / taneční pár", price: "100 Kč", desc: "Pro členy tanečního klubu"},
]

</script>