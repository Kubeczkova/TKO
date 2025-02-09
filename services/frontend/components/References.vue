<template>
  <h1>Reference</h1>
      <v-expansion-panels class="pa-4" variant="popout">
    <v-expansion-panel
      v-for="(reference, id) in references"
      :key="id"
      hide-actions
    >
      <v-expansion-panel-title>
        <v-row
          align="center"
          class="spacer"
          no-gutters
        >
          <v-col
            cols="4"
            md="1"
            sm="2"
          >
            <v-avatar
              size="36px"
            >
              <v-img
                v-if="reference.avatar"
                alt="Avatar"
                :src="reference.avatar"
              ></v-img>
            </v-avatar>
          </v-col>

          <v-col
            md="3"
            sm="5"
          >
            <h2>{{ reference.name }}</h2>
            <div class="subtitle">{{ reference.title }}</div>
          </v-col>
        </v-row>
      </v-expansion-panel-title>

      <v-expansion-panel-text>
        <div class="subtitle">{{ reference.desc }}</div>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</template>
<script setup lang="ts">

const references = [
  {
    id: 1,
    avatar: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
    title: "Členka tanečního klubu",
    name: "Alenka",
    desc: "Dlouhý popisek"},
  {
    id: 2,
    avatar: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
    title: "Členka tanečního klubu",
    name: "Pepík",
    desc: "Dlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisek"
  },
  {
    id: 3,
    avatar: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
    title: "Občasný zájemce individuálního cvičení",
    name: "Davídek",
    desc: "Dlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekisek"},
  {
    id: 4,
    avatar: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
    title: "Trenér",
    name: "Franta",
    desc: "Dlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisek"
  },
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

.subtitle {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 1rem;
  color: #333; /* Dark gray */
}

</style>
