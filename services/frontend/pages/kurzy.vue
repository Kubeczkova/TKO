<template>
  <h1 id="courses">Kurzy</h1>
  <h2>Vyberte, co Vám nejlépe vyhovuje</h2>

  <v-row>
    <v-col
        cols="12"
        md="4"
        v-for="(course, index) in courses"
        :key="index"
    >
      <v-card class="pricing-box">
        <h3>{{ course.name }}</h3>
        <v-card-subtitle><div class="pricing__subtitle">{{ course.time }}</div></v-card-subtitle>
        <v-card-title><div class="pricing__price">{{ course.price }}</div></v-card-title>
        <v-card-text v-if="course.desc"><div class="pricing__subtitle">{{ course.desc }}</div></v-card-text>
        <v-btn class="show_more"><v-icon icon="mdi-chevron-down"/>Kontaktujte nás<v-icon icon="mdi-chevron-down"/></v-btn>
      </v-card>
    </v-col>
  </v-row>
  <calendar/>
</template>
<script setup lang="ts">
import './assets/css/main.css'

// TODO: vyskakovací okno s kontaktním formulářem po rozkliku :)

const courses = [
  {name: "Sportovní taneční klub", time: "", price: "", desc: "Připojte se k našemu tanečnímu klubu a rozvíjejte své taneční dovednosti v přátelském prostředí. Nabízíme různé styly tance pro všechny úrovně."},
  {name: "Svatební tance", time: "", price: "", desc: "Udělejte svůj první tanec nezapomenutelným. Pomůžeme Vám vytvořit choreografii na míru, která bude odrážet Váš jedinečný styl."},
  {name: "Příprava na plesovou sezónu", time: "", price: "", desc: "Chcete zazářit na plese? Připravíme Vás na plesovou sezónu a naučíme Vás elegantní taneční kroky a etiketu."},
  {name: "Individuální taneční kurzy", time: "", price: "", desc: "Učte se tančit vlastním tempem s individuálním přístupem. Naši zkušení lektoři se zaměří na Vaše potřeby a pomohou Vám dosáhnout Vašich tanečních cílů."},
  {name: "Individuální lekce", time: "", price: "", desc: "Zlepšete své taneční dovednosti s intenzivními individuálními lekcemi. Zaměřte se na konkrétní taneční techniky nebo styly, které Vás zajímají."},
  {name: "Pronájem sálu", time: "", price: "", desc: "Hledáte ideální prostor pro tanec nebo jinou aktivitu? Náš taneční sál je k dispozici k pronájmu pro Vaše akce."},
]

</script>