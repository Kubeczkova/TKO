<template>
  <h1>Naši trenéři a lektoři</h1>
  <v-card>
    <v-row v-for="(lector, index) in lectors" :key="index">
      <v-col
      style="padding: 0;" >
        <v-img
          :src="lector.background"
          cover
        >
          <v-col style="text-align: center" cols="12" md="4">
            <v-avatar
              color="grey"
              rounded="1"
              size="300"
              style="margin: 30px"
            >
              <v-img :src="lector.img" cover></v-img>
            </v-avatar>
            <h2>{{lector.name}}</h2>
            <div class="subtitle">{{ lector.desc }}</div>
            <v-divider :thickness="3" />
            <h4>{{lector.story}}</h4>
          </v-col>
        </v-img>
      </v-col>
    </v-row>
  </v-card>
</template>
<script setup lang="ts">
const lectors = [
  {
    name: "Ondřej Gilar",
    img: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg",
    desc: "Trenér - latinskoamerické tance a Pro-AM",
    background: "https://cdn11.bigcommerce.com/s-07991/product_images/uploaded_images/latin-dance.jpg",
    story: "Něco velice zajímavého sepsané dlouhým textem, který snad někdo přečte, protože je to určitě zajímavé. Nová koloběžka bylo vrhnuta do řeky hned vedle pískoviště na počítači.",
  },
  {
    name: "Leona Hruštincová",
    img: "https://cdn.vuetifyjs.com/images/profiles/marcus.jpg",
    desc: "Lektorka - tance pro děti",
    background: "https://cdn11.bigcommerce.com/s-07991/product_images/uploaded_images/latin-dance.jpg",
    story: "Něco velice zajímavého sepsané dlouhým textem, který snad někdo přečte, protože je to určitě zajímavé. Nová koloběžka bylo vrhnuta do řeky hned vedle pískoviště na počítači.",
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
  margin-top: -2rem;
}

h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  color: #666; /* Light gray */
}

.subtitle {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 1.5rem;
  color: #333; /* Dark gray */
}
</style>