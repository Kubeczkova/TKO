<template>
  <v-parallax
    class="trainers__parallax"
    src="public/img/black-pink.jpg"
  >
    <v-container id="trainers">
      <v-card class="trainers">
        <v-card-title class="about__title">Naši trenéři a lektoři</v-card-title>
        <v-card-subtitle class="about__subtitle">Seznamte se s námi!</v-card-subtitle>
        <v-row>
          <v-col class="text-center" cols="12" md="3" v-for="lector in lectors" :key="lector.id">
              <v-avatar
                color="none"
                rounded="1"
                size="150"
                style="margin: 30px"
              >
                <v-img :src="lector.img" cover></v-img>
              </v-avatar>
            <v-card-subtitle class="about__subtitle">{{lector.name}}</v-card-subtitle>
            <v-card-text class="about__text">{{ lector.desc }}</v-card-text>
          </v-col>
        </v-row>
      </v-card>
    </v-container>
  </v-parallax>
</template>
<script setup lang="ts">
import './assets/css/main.css'

const lectors = [
  {
    id: 1,
    name: "Ondřej Gilar",
    img: "/trainers/img.png",
    desc: "Trenér - latinskoamerické tance a Pro-AM",
  },
  {
    id: 2,
    name: "Leona Hruštincová",
    img: "/trainers/img.png",
    desc: "Lektorka - tance pro děti",
  },
  {
    id: 1,
    name: "Ondřej Gilar",
    img: "/trainers/img.png",
    desc: "Trenér - latinskoamerické tance a Pro-AM",
  },
  {
    id: 2,
    name: "Leona Hruštincová",
    img: "/trainers/img.png",
    desc: "Lektorka - tance pro děti",
  },
]
</script>