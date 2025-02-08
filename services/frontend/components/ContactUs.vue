<template>
  <v-card>
      <v-card-title>
        <h1>Kontaktujte nás!</h1>
      </v-card-title>
  <v-form v-model="valid" @submit="sendContact">
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="fullName"
            label="Jméno a příjmení"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="email"
            label="Emailová adresa *"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="phone"
            label="Telefonní číslo"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-textarea
            v-model="textField"
            label="Váš dotaz *"
            required
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn
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

const valid = ref<boolean>(false);

const fullName = ref<string>("");
const email = ref<string>("");
const phone = ref<string>("");
const textField = ref<string>("");

function sendContact() {
  console.log("KONTAKT NEZASLAN");
}

</script>

<style scoped>

</style>