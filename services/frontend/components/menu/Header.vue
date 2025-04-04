<template>
  <ClientOnly>
    <v-layout>
      <v-app-bar style="position: fixed">
        <v-app-bar-nav-icon
          @click="drawer = !drawer"
          class="d-flex d-sm-none"
        />
        <div>
          <a href="/"><v-img class="app__logo" src="/logo.png" /></a>
        </div>
        <v-app-bar-title class="app__title">Taneční klub Ostrava</v-app-bar-title>

        <v-tabs v-model="currentTab" class="d-none d-sm-flex app__tab">
          <div
            v-for="(tab, index) in tabs"
            :key="index"
          >
            <v-tab
              v-if="tab.ref"
              :text="tab.name"
              :value="tab.name"
              @click="useGoTo(tab.ref)"
            >
              {{ tab.name }}
            </v-tab>
            <v-tab
              v-if="tab.href"
              :text="tab.name"
              :value="tab.name"
              :href="tab.href"
            >
              {{ tab.name }}
            </v-tab>
          </div>
        </v-tabs>


<!--        <v-col-->
<!--          class="text-right"-->
<!--          @click="toggleTheme"-->
<!--        >-->
<!--          <big-icon icon="mdi-lightbulb-cfl"/>-->
<!--        </v-col>-->
      </v-app-bar>

      <v-fab
        class="ms-4 mb-4"
      ></v-fab>

      <v-navigation-drawer
        v-model="drawer"
        absolute
        fixed
        left
      >
        <v-list nav dense>
          <v-list-item v-for="(tab, index) in tabs" :key="index">
            <v-list-item-title @click="useGoTo(tab.ref)">{{ tab.name }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-layout>
  </ClientOnly>
</template>

<script setup lang="ts">
import { useGoTo } from "~/composables/useGoTo";
import {useRoute} from "#vue-router";
const route = useRoute();

const currentTab = ref({ name: 'O nás', ref: "#about", href: "o-nas" });
const drawer = ref(null)

const homeTabs = [
  { name: "O nás", ref: "#about", href: "" },
  { name: "Trenéři", ref: "#trainers", href: "" },
  { name: "Kurzy", ref: "#courses", href: "" },
  { name: "Galerie", ref: "", href: "/galerie" },
  { name: "Aktuality", ref: "#article", href: "" },
  { name: "Kontakty", ref: "", href: "/kontakty" },
];

const otherTabs = [
  { name: "O nás", ref: "", href: "/" },
  { name: "Trenéři", ref: "", href: "/" },
  { name: "Kurzy", ref: "", href: "/" },
  { name: "Galerie", ref: "", href: "/galerie" },
  { name: "Aktuality", ref: "", href: "/" },
  { name: "Kontakty", ref: "", href: "/kontakty" },
];

const tabs = computed(() => (route.path === "/" ? homeTabs : otherTabs));
// import { useTheme } from 'vuetify'
//
// const theme = useTheme()
//
// function toggleTheme () {
//   theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
// }


</script>