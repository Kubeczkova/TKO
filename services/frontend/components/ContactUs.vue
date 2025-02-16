<template>
  <v-card class="contact">
    <v-form v-model="valid" @submit="sendContact">
      <v-container>
        <v-card-title class="contact__title">Kontaktujte nás!</v-card-title>
        <v-row>
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="fullName"
              label="Jméno"
              variant="underlined"
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="email"
              label="Emailová adresa"
              variant="underlined"
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="phone"
              label="Telefonní číslo"
              variant="underlined"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-textarea
              v-model="textField"
              label="Váš dotaz *"
              variant="underlined"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn
              class="contact__button"
              type="submit"
            >
              Poslat
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-card>
</template>
<script setup lang="ts">
import './assets/css/main.css'

const valid = ref<boolean>(false);

const fullName = ref<string>("");
const email = ref<string>("");
const phone = ref<string>("");
const textField = ref<string>("");

function sendContact() {
  console.log("KONTAKT NEZASLAN");
}

</script>