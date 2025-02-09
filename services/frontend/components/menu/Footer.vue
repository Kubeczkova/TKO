<template>
  <v-footer
    style="background-color: black"
  >
    <v-container class="text-white">
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <h4>Kontakt</h4>
          <v-divider :thickness="3" />
          <div class="footer-text">Tomáš Ožana</div>
          <div class="footer-text">Zimmlerova 2893/47, Ostrava</div>
          <div class="footer-text">tanecniklub-ostrava@email.cz</div>
          <div class="footer-text">+420774908180</div>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <h4>Tréningové hodiny</h4>
          <v-divider :thickness="3" />
          <div class="footer-text">Pondělí: <span class="timespan">16:30 - 18:30 (VS)</span></div>
          <div class="footer-text">Úterý: <span class="timespan">16:30 - 18:30 (VS)</span></div>
          <div class="footer-text">Středa: <span class="timespan">16:30 - 18:30 (VS)</span></div>
          <div class="footer-text">Čtvrtek: <span class="timespan">16:30 - 18:30 (VS)</span></div>
          <div class="footer-text">Pátek: <span class="timespan">16:30 - 18:30 (VS)</span></div>
          <div class="footer-text">Sobota: <span class="timespan">16:30 - 18:30 (VS)</span></div>
          <div class="footer-text">Neděle: <span class="timespan">16:30 - 18:30 (VS)</span></div>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <h4>Sociální sítě</h4>
          <v-divider :thickness="3" />
<!--          https://pictogrammers.com/library/mdi/icon/youtube/-->
          <span class="mdi mdi-facebook" style="font-size: 60px"></span>
          <span class="mdi mdi-instagram" style="font-size: 60px"></span>
          <span class="mdi mdi-youtube" style="font-size: 60px"></span>
        </v-col>
      </v-row>
      <v-divider :thickness="3" style="margin-top: 60px" />
      <v-row>
        <v-col
          style="text-align: left"
        >
          <h5>Taneční klub Ostrava © 2025</h5>
        </v-col>
        <v-col
          style="text-align: right"
        >
          <h5>created by Beeebooo Crew</h5>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>
<script setup lang="ts">

</script>

<style scoped>
h4 {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  color: #aaa; /* Light gray */
  text-align: center;
  margin-bottom: 0.5rem;
}

h5 {
  font-family: 'Playfair Display', serif;
  font-size: 1rem;
  color: #aaa; /* Light gray */
  margin-top: 1rem;
}

.footer-text {
  font-family: 'Playfair Display', serif;
  font-size: 1rem;
  color: #aaa; /* Light gray */
}

.timespan {
  float: right; /* Aligns the timespan to the right */
}
</style>