<template>
  <h1>Kalendář</h1>
  <h2>Podívejte se, kdy se můžete přidat!</h2>

  <v-sheet class="sheet__box">
    <v-calendar
      v-model="value"
      first-day-of-week="1"
      locale="cs-CZ"
      ref="calendar"
      view-mode="week"
      :events="events"
      :weekdays="[1, 2, 3, 4, 5, 6, 0]"
    />
  </v-sheet>
</template>

<script setup lang="ts">
import './assets/css/main.css'

const value = [new Date()];
const events = [
  {
    title: "ahoj",
    start: new Date(),
    end: new Date(),
    color: 'red',
  }
];
</script>