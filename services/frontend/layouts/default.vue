<template>
  <v-layout>
    <v-app app>
      <menu-header/>
      <v-main>
        <slot />
      </v-main>
      <menu-footer/>
    </v-app>
  </v-layout>
</template>
<script setup lang="ts">

</script>

<style scoped>

</style>