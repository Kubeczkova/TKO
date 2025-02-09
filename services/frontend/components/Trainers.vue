<template>
  <h1>Naši trenéři a lektoři</h1>
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
        <div class="subtitle">{{ lector.desc }}</div>
      </v-col>
    </v-row>
</template>
<script setup lang="ts">
const lectors = [
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

<style scoped>
h1 {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 3rem;
  color: #333; /* Dark gray */
  text-align: center;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  margin-top: 2rem;
  margin-bottom: 1rem;
}

h2 {
  font-family: 'Playfair Display', serif;
  text-align: center;
  font-size: 1.7rem;
  color: #666; /* Light gray */
}

.subtitle {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 1rem;
  color: #333; /* Dark gray */
  text-align: center;
}
</style>