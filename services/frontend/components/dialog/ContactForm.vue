<template>
  <v-form v-model="valid">
      <v-container>
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
              label="Váš dotaz"
              variant="underlined"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn
              class="contact__button"
              type="submit"
              @click.prevent="sendContact"
            >
              Poslat
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
</template>
<script setup lang="ts">
import './assets/css/main.css'
import {useAPI} from "~/composables/useAPI";

const valid = ref<boolean>(false);

const fullName = ref<string>("");
const email = ref<string>("");
const phone = ref<string>("");
const textField = ref<string>("");

async function sendContact() {
  const { data, error } = await useAPI('create-contact/', {
    method: "POST",
    body: {
      name: fullName.value,
      email: email.value,
      phone_number: phone.value,
      content: textField.value,
    }
  });
}

</script>