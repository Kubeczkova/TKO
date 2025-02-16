<template>
  <h1>Co dostanete s tanečním klubem</h1>
  <h2>Výhody tanečníka</h2>
  <card
    v-for="advantage in advantages"
    :key="advantage.id"
    class="advantage"
  >
    <v-row>
      <v-col cols="12" md="1">
        <small-icon :icon="advantage.icon" />
      </v-col>
      <v-col>
        <v-card-title class="advantage__title">
          {{advantage.title}}
        </v-card-title>
      </v-col>
    </v-row>
    <v-card-text class="advantage__text">
      {{ advantage.subtitle }}
    </v-card-text>
  </card>
</template>
<script setup lang="ts">
import './assets/css/main.css'

const advantages = [
  {id: 1, icon: "mdi mdi-heart", title: "Zdravé tělo a mysl",
    subtitle: "Seznamíte se s charaktery jednotlivých tanců, správným pohybem a jeho provedením, zrelaxujete se a zapomenete na každodenní starosti."},
  {id: 2, icon: "mdi mdi-music", title: "Skvělá hudba a kostýmy",
    subtitle: "Zažijete krásné chvíle v rytmu latinskoamerických a standardních tanců a pokud Vás tanec opravdu veme za srdce můžete se zůčastnit také tanečních vystoupení a tanečních soutěží."},
  {id: 3, icon: "mdi mdi-account-group", title: "Krealitvní a zábavní lidé",
    subtitle: "Příjemná společnost a tým lidí, ce kterém se také můžete spolehnout na individuální přístup lektorů, kteří tu vždy budou právě pro Vás."},
]
</script>