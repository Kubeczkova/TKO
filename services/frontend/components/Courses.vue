<template>
  <h1 id="courses">Kurzy</h1>
  <h2>Vyberte, co Vám nejlépe vyhovuje</h2>

<v-row class="pricing">
  <v-col
      cols="12"
      sm="6"
      md="4"
      lg="3"
      v-for="(course, index) in courses"
      :key="index"
  >
    <v-card class="pricing-box" @click="openDialog = true; chosenCourse = course">
      <div class="pricing-content">
        <h3 class="pricing-title">{{ course.name }}</h3>
        <v-card-subtitle v-if="course.time">
          <div class="pricing__subtitle">{{ course.time }}</div>
        </v-card-subtitle>
        <v-card-title v-if="course.price">
          <div class="pricing__price">{{ course.price }}</div>
        </v-card-title>
        <v-card-text v-if="course.desc">
          <div class="pricing__subtitle pricing-desc">{{ course.desc }}</div>
        </v-card-text>
      </div>
      <v-btn class="show_more">
        Kontaktujte nás
      </v-btn>
    </v-card>
  </v-col>
</v-row>
<template>
  <v-dialog
    v-model="openDialog"
    :fullscreen="$vuetify.display.smAndDown"
    scrollable
    transition="dialog-bottom-transition"
  >
    <v-card class="contact pa-4">
      <h1 class="contact__dialog__title d-flex align-center">
        <span class="flex-grow-1 text-center" style="margin-left: 40px;">{{ chosenCourse.name }}</span>
        <v-btn icon="mdi-close" variant="text" @click="openDialog = false"></v-btn>
      </h1>
        <v-card-text v-if="chosenCourse.desc" class="text-center">
          <div class="pricing__subtitle text-body-1">{{ chosenCourse.desc }}</div>
        </v-card-text>

        <v-divider class="my-4"></v-divider>

      <v-card-title class="contact__dialog__title text-center">
        Kontaktujte nás!
      </v-card-title>

        <dialog-contact-form class="mt-2" />
        </v-card>
      </v-dialog>
    </template>

<!--    <v-btn to="/kurzy" class="show_more">-->
<!--      <v-icon icon="mdi-chevron-down"/>Více informací<v-icon icon="mdi-chevron-down"/>-->
<!--    </v-btn>-->
</template>
<script setup lang="ts">
import './assets/css/main.css'

const openDialog = ref<boolean>(false);

const courses = [
  {name: "Sportovní taneční klub", time: "", price: "", desc: "Připojte se k našemu tanečnímu klubu a rozvíjejte své taneční dovednosti v přátelském prostředí. Nabízíme různé styly tance pro všechny úrovně."},
  {name: "Svatební tance", time: "", price: "", desc: "Udělejte svůj první tanec nezapomenutelným. Pomůžeme Vám vytvořit choreografii na míru, která bude odrážet Váš jedinečný styl."},
  {name: "Příprava na plesovou sezónu", time: "", price: "", desc: "Chcete zazářit na plese? Připravíme Vás na plesovou sezónu a naučíme Vás elegantní taneční kroky a etiketu."},
  {name: "Individuální taneční kurzy", time: "", price: "", desc: "Učte se tančit vlastním tempem s individuálním přístupem. Naši zkušení lektoři se zaměří na Vaše potřeby a pomohou Vám dosáhnout Vašich tanečních cílů."},
  {name: "Individuální lekce", time: "", price: "", desc: "Zlepšete své taneční dovednosti s intenzivními individuálními lekcemi. Zaměřte se na konkrétní taneční techniky nebo styly, které Vás zajímají."},
  {name: "Pronájem sálu", time: "", price: "", desc: "Hledáte ideální prostor pro tanec nebo jinou aktivitu? Náš taneční sál je k dispozici k pronájmu pro Vaše akce."},
]

const chosenCourse = ref(courses[0]);
</script>