<template>
  <v-parallax class="trainers__parallax" src="public/img/black-pink.jpg">
    <v-container id="trainers">
      <v-card class="trainers pa-4">
        <v-card-title class="about__title ">Naši trenéři a lektoři</v-card-title>
        <v-card-subtitle class="about__subtitle ">Seznamte se s námi!</v-card-subtitle>

        <v-carousel cycle interval="4000" hide-delimiters show-arrows="hover">
          <v-carousel-item v-for="(group, index) in trainerGroups" :key="index">
            <v-row justify="center">
              <v-col
                v-for="(lector, index) in group"
                :key="index"
                cols="12"
                sm="6"
                md="4"
                lg="3"
                class="text-center"
              >
                <v-avatar
                  color="none"
                  rounded="1"
                  size="150"
                  style="margin: 30px"
                >
                  <v-img :src="lector.img" cover></v-img>
                </v-avatar>
                <v-card-subtitle class="about__subtitle">{{ lector.name }}</v-card-subtitle>
                <v-card-text class="about__text">{{ lector.desc }}</v-card-text>
              </v-col>
            </v-row>
          </v-carousel-item>
        </v-carousel>
      </v-card>
    </v-container>
  </v-parallax>
</template>
<script setup lang="ts">
import './assets/css/main.css'

const lectors = [
  {
    name: "Ondřej Gilar",
    img: "/trainers/img.png",
    desc: "Trenér - latinskoamerické tance a Pro-AM",
  },
  {
    name: "Leona Hruštincová",
    img: "/trainers/img.png",
    desc: "Lektorka - tance pro děti",
  },
  {
    name: "Ondřej Gilar",
    img: "/trainers/img.png",
    desc: "Trenér - latinskoamerické tance a Pro-AM",
  },
  {
    name: "Leona Hruštincová",
    img: "/trainers/img.png",
    desc: "Lektorka - tance pro děti",
  },
  {
    name: "Leona Hruštincová",
    img: "/trainers/img.png",
    desc: "Lektorka - tance pro děti",
  },
]

const trainerGroups = computed(() => {
  const groups: typeof lectors[] = [];
  const perSlide = window.innerWidth >= 1280 ? 4 : window.innerWidth >= 600 ? 2 : 1;
  for (let i = 0; i < lectors.length; i += perSlide) {
    groups.push(lectors.slice(i, i + perSlide));
  }
  return groups;
});
</script>