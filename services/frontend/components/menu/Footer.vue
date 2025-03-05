<template>
  <v-footer class="footer">
    <v-container class="text-white">
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <h5>Kontakt</h5>
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
          <h5>Tréningové hodiny</h5>
          <v-divider :thickness="3" />
          <div class="to_left">Pondělí: <span class="to_right">16:30 - 18:30 (VS)</span></div>
          <div class="to_left">Úterý: <span class="to_right">16:30 - 18:30 (VS)</span></div>
          <div class="to_left">Středa: <span class="to_right">16:30 - 18:30 (VS)</span></div>
          <div class="to_left">Čtvrtek: <span class="to_right">16:30 - 18:30 (VS)</span></div>
          <div class="to_left">Pátek: <span class="to_right">16:30 - 18:30 (VS)</span></div>
          <div class="to_left">Sobota: <span class="to_right">16:30 - 18:30 (VS)</span></div>
          <div class="to_left">Neděle: <span class="to_right">16:30 - 18:30 (VS)</span></div>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <h5>Sociální sítě</h5>
          <v-divider :thickness="3" />
          <big-icon icon="mdi-facebook" />
          <big-icon icon="mdi-instagram" />
          <big-icon icon="mdi-youtube" />
        </v-col>
      </v-row>
      <v-divider :thickness="3" style="margin-top: 60px" />
      <v-row>
        <v-col
          style="text-align: left"
        >
          <h5>Taneční klub Ostrava s.r.o. © {{date}}</h5>
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
import './assets/css/main.css'

const date = new Date().getFullYear()
</script>