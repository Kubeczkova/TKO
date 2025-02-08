<template>
  <v-card>
    <v-card-title>
      <h1>Reference</h1>
    </v-card-title>
    <v-card-item>
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
            <strong v-html="reference.name" style="font-size: 20px"></strong>
            <div>
            <v-rating
              readonly
              :length="5"
              :size="20"
              :model-value="5"
             />
            </div>
          </v-col>
        </v-row>
      </v-expansion-panel-title>

      <v-expansion-panel-text>
        <v-card-text v-text="reference.desc"></v-card-text>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
    </v-card-item>
  </v-card>
</template>
<script setup lang="ts">

const references = [
  {id: 1, avatar: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460", name: "Alenka", desc: "Dlouhý popisek"},
  {
    id: 2, avatar: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
    name: "Pepík",
    desc: "Dlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisek"
  },
  {id: 3, avatar: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460", name: "Davídek", desc: "Dlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekisek"},
  {
    id: 4, avatar: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
    name: "Franta",
    desc: "Dlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisekDlouhý popisek"
  },
]

</script>

<style scoped>

</style>
