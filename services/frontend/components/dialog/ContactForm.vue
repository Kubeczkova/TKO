<template>
  <v-form v-model="valid">
      <v-snackbar
          v-model="showSnackbar"
          :color="snackbarColor"
          :timeout="5000"
      >
        {{ snackbarMessage }}
      </v-snackbar>
      <v-container>
        <v-row>
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              dense
              hide-details="auto"
              v-model="fullName"
              :error-messages="get(errorMessages, 'name')"
              @change="hideError('name')"
              label="Jméno"
              variant="underlined"
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              dense
              hide-details="auto"
              type="email"
              autocomplete="email"
              v-model="email"
              :error-messages="get(errorMessages, 'email')"
              @change="hideError('email')"
              label="Emailová adresa"
              variant="underlined"
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              dense
              hide-details="auto"
              type="tel"
              v-model="phone"
              :error-messages="get(errorMessages, 'phone_number')"
              @change="hideError('phone_number')"
              label="Telefonní číslo"
              variant="underlined"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-textarea
              v-model="textField"
              :error-messages="get(errorMessages, 'content')"
              @change="hideError('content')"
              label="Váš dotaz"
              variant="underlined"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn
              auto-grow
              rows="3"
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
const errorMessages = ref<Record<string, string[]>>({});

const fullName = ref<string>("");
const email = ref<string>("");
const phone = ref<string>("");
const textField = ref<string>("");

const showSnackbar = ref(false);
const snackbarMessage = ref("");
const snackbarColor = ref("red-accent-4")

function get(obj: any, path: string, defaultValue = undefined) {
  return path.split('.').reduce((acc, part) => acc && acc[part], obj) ?? defaultValue;
}

function resetContractData() {
  fullName.value = "";
  email.value = "";
  phone.value = "";
  textField.value = "";
}

function hideError (key: string) {
  delete errorMessages.value[key];
}

async function sendContact() {
  const { error } = await useAPI('create-contact/', {
    method: "POST",
    body: {
      name: fullName.value,
      email: email.value,
      phone_number: phone.value,
      content: textField.value,
    }
  });

  if (error.value) {
    snackbarMessage.value = "Něco se pokazilo. Zkuste to znovu.";
    snackbarColor.value = "red-accent-4";
    errorMessages.value = error.value.data;
  } else {
    snackbarMessage.value = "Děkujeme! Vaše zpráva byla odeslána.";
    snackbarColor.value = "success";
    resetContractData();
  }

  showSnackbar.value = true;
}

</script>