<template>
  <h1>Kurzy - cena</h1>
  <h4>Vyberte, co Vám nejlépe vyhovuje</h4>
  <v-row>
    <v-col
        cols="12"
        md="4"
        v-for="course in courses"
        :key="course.id"
    >
      <v-card
        class="pricing-box"
      >
        <h2>{{ course.name }}</h2>
        <v-card-subtitle><div class="subtitle">{{ course.time }}</div></v-card-subtitle>
        <v-card-title><div class="price">{{ course.price }}</div></v-card-title>
        <v-card-subtitle v-if="course.desc"><div class="subtitle">{{ course.desc }}</div></v-card-subtitle>
      </v-card>
    </v-col>
  </v-row>
</template>
<script setup lang="ts">

const courses = [
  {id: 1, name: "Sportovní taneční klub", time: "24 hodin/měsíc", price: "600 Kč", desc: false},
  {id: 2, name: "Individuální lekce", time: "60min / taneční pár", price: "500 Kč", desc: "Pro veřejnost"},
  {id: 3, name: "Volný trénink s lektorem", time: "60min / taneční pár", price: "100 Kč", desc: "Pro členy tanečního klubu"},
]

</script>

<style scoped>
h1 {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 3rem;
  color: #333; /* Dark gray */
  text-align: center;
  margin-bottom: 1rem;
  margin-top: 2rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1); /* Subtle shadow */
}

h2 {
  font-family: 'Playfair Display', serif;
  font-size: 1.7rem;
  color: #666; /* Light gray */
}

h4 {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  color: #666; /* Light gray */
  text-align: center;
  margin-bottom: 0.5rem;
}

.pricing-box {
  padding: 20px;
  text-align: center;
  min-width: 80%;
  border-radius: 15px;
  height: 230px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
  margin: 50px
}

.pricing-box:not(:last-child) {
  margin: 20px;
}

.price {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 3.5rem;
  color: #333; /* Dark gray */
  text-align: center;
}

.subtitle {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 1rem;
  color: #333; /* Dark gray */
  text-align: center;
}
</style>