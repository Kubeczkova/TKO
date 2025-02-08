<template>
  <v-card>
    <v-card-title>
      <h1>Naši trenéři a lektoři</h1>
    </v-card-title>
    <v-row>
      <v-col v-for="lector in lectors" :key="lector.id" cols="12" md="6" lg="4">
        <v-img
          src="https://cdn11.bigcommerce.com/s-07991/product_images/uploaded_images/latin-dance.jpg"
          max-height="250"
          max-width="700"
          min-width="500"
          width="50%"
          cover
        >
          <v-avatar
            color="grey"
            rounded="0"
            size="150"
          >
            <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg" cover></v-img>
          </v-avatar>
          <v-list-item
            class="text-white"
            :subtitle="lector.desc"
            :title="lector.name"
          ></v-list-item>
        </v-img>
      </v-col>
    </v-row>
  </v-card>
</template>
<script setup lang="ts">
const lectors = [
  {id: 1, name: "Ondřej Gilar", desc: "Trenér - latinskoamerické tance a Pro-AM"},
  {id: 2, name: "Leona Hruštincová", desc: "Lektorka - tance pro děti"},
  {id: 3, name: "Ondřej Gilar", desc: "Trenér - latinskoamerické tance a Pro-AM"},
  {id: 4, name: "Leona Hruštincová", desc: "Lektorka - tance pro děti"},
]
</script>

<style scoped>

</style>