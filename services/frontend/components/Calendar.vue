<template>
  <h1>Kalendář</h1>
  <h2>Podívejte se, kdy se můžete přidat!</h2>

  <v-sheet class="sheet__box">
    <v-calendar
      :firstDayOfWeek="0"
      locale="cs-CZ"
      ref="calendar"
      :showAdjacentMonths="true"
      view-mode="week"
      :events="events"
      :interval-start="7"
      :interval-height="25"
    />
  </v-sheet>
</template>

<script setup lang="ts">
import './assets/css/main.css'
import {useAPI} from "~/composables/useAPI";

interface Event {
  title: string;
  end: Date;
  start: Date;
  color: string;
}

const events = ref<Event[]>([]);

await loadEvents();

async function loadEvents() {
  const { error, data } = await useAPI<Event[]>('load-events/', { method: "GET" });

  if (data.value && Array.isArray(data.value)) {
    events.value = data.value as Event[];
    for(const i in data.value){
      data.value[i].end = new Date((data.value[i].end));
      data.value[i].start = new Date((data.value[i].start));
    }
  } else if (error.value) {
    console.error("Error loading events:", error.value);
  }
}
</script>