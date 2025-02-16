<template>
  <h1>Naši trenéři a lektoři</h1>
  <h2>Seznamte se s námi!</h2>
    <v-row style="margin-bottom: 2rem;">
      <v-col class="text-center" cols="12" md="3" v-for="lector in lectors" :key="lector.id">
          <v-avatar
            color="none"
            rounded="1"
            size="150"
            style="margin: 30px"
          >
            <v-img :src="lector.img" cover></v-img>
          </v-avatar>
        <h2>{{lector.name}}</h2>
        <h4>{{ lector.desc }}</h4>
      </v-col>
    </v-row>
</template>
<script setup lang="ts">
import './assets/css/main.css'

const lectors = [
  {
    id: 1,
    name: "Ondřej Gilar",
    img: "/Beblik.jpg",
    desc: "Trenér - latinskoamerické tance a Pro-AM",
  },
  {
    id: 2,
    name: "Leona Hruštincová",
    img: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg",
    desc: "Lektorka - tance pro děti",
  },
  {
    id: 1,
    name: "Ondřej Gilar",
    img: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg",
    desc: "Trenér - latinskoamerické tance a Pro-AM",
  },
  {
    id: 2,
    name: "Leona Hruštincová",
    img: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg",
    desc: "Lektorka - tance pro děti",
  },
]
</script>