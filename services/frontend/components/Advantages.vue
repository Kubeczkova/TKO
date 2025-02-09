<template>
  <h1>Co dostanete s tanečním klubem</h1>
  <h4>Výhody tanečníka</h4>
  <v-card
    v-for="advantage in advantages"
    :key="advantage.id"
    :prepend-icon="advantage.icon"
    class="advantage-box"
    :title="advantage.title"
  >
    <v-card-text style="color: #666">{{ advantage.subtitle }}</v-card-text>
  </v-card>
</template>
<script setup lang="ts">

const advantages = [
  {id: 1, icon: "mdi mdi-heart", title: "Zdravé tělo a mysl",
    subtitle: "Seznamíte se s charaktery jednotlivých tanců, správným pohybem a jeho provedením, zrelaxujete se a zapomenete na každodenní starosti."},
  {id: 2, icon: "mdi mdi-music", title: "Skvělá hudba a kostýmy",
    subtitle: "Zažijete krásné chvíle v rytmu latinskoamerických a standardních tanců a pokud Vás tanec opravdu veme za srdce můžete se zůčastnit také tanečních vystoupení a tanečních soutěží."},
  {id: 3, icon: "mdi mdi-account-group", title: "Krealitvní a zábavní lidé",
    subtitle: "Příjemná společnost a tým lidí, ce kterém se také můžete spolehnout na individuální přístup lektorů, kteří tu vždy budou právě pro Vás."},
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

h4 {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  color: #666; /* Light gray */
  text-align: center;
  margin-bottom: 0.5rem;
}

.advantage-box {
  min-width: 400px;
  border-radius: 15px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
  margin-top: 20px;
  margin-left: calc(20% - 40px); /* Subtract half of min-width from left margin */
  margin-right: calc(20% - 40px); /* Subtract half of min-width from right margin */
}

</style>