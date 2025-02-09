<template>
  <v-parallax
    src="https://www.danceus.org/parse/files/Bjy5anNVI0Q81M8bmrwIiuU20x4kepQTxzDBfqpR/70d831b8f51edc1f6e1a4320d52f164b_latin-dance.jpg"
    style="max-height: 580px"
  >
        <v-container fluid fill-height>
    <v-row align="center" justify="center">
      <v-col
        cols="12"
        md="4"
      />
      <v-col
        cols="12"
        md="8"
        style="color: white; padding: 50px"
      >
        <v-card
          class="overflow-y-auto"
          max-height="460"
          style="background-color: transparent"
        >
          <h1>Vítejte v tanečním klubu!</h1>
          <h4>Tanec je vášeň!</h4>
          <div class="subtitle">
            Sportovní taneční klub jsme založili v roce 2016 s absolventy středoškolských tanečních kurzů taneční školy Bolero Ostrava.
            Společně jsme se zaměřili na profesionální stránku tance, našli jsme pár aktivních tanečníků se kterými jsme začali pravidelně trénovat pohyb, krokové variace a techniku jednotlivých tanců.
            Po roce tréninků se dostavily i první výsledky a dnes již tito mladí tanečníci skvěle reprezentují klub na celé řadě tanečních soutěží.
            <br><br>
            O rok později v roce 2017 jsme založili také společenský taneční klub pro dospělé, kteří by se rádi také tanci věnovali.
            Příjemná atmosféra, zábava, ale i chuť se učit novým věcem, to jsou tři slova, které by mohly charakterizovat atmosféru v tanečních lekcích.
            Taneční klub, ať už sportovní tak i společenský vítá všechny milovníky tance, kteří chtějí poodhalit tajemství ladných tanečních pohybů, sdílet nezaměnitelnou atmosféru a dovědět se více o taneční technice.
            Našim přáním je, abyste na tanečním parketu jednoduše zářili.
          </div>
        </v-card>
      </v-col>
    </v-row>
        </v-container>
  </v-parallax>
</template>
<script setup lang="ts">

</script>

<style scoped>
h1 {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 3rem;
  color: #ddd; /* reverse Dark gray */
  text-align: center;
  margin-bottom: 1rem;
  margin-top: 2rem;
  text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.1); /* Subtle shadow */
}

h4 {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  color: #aaa; /* Light gray */
  text-align: center;
  margin-bottom: 0.5rem;
}
.subtitle {
  font-family: 'Playfair Display', serif; /* Or a similar elegant font */
  font-size: 1.2rem;
  text-align: center;
  color: #ddd; /* Dark gray */
}
</style>