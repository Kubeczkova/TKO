<template>
  <ClientOnly>
    <v-layout style="margin-bottom: 3rem">
      <v-app-bar style="position: fixed">
        <div>
          <a href="/"><v-img class="app__logo" src="/logo.png" /></a>
        </div>
        <v-app-bar-title class="app__title" v-if="$vuetify.display.smAndUp">
          Taneční klub Ostrava
        </v-app-bar-title>

        <v-tabs v-model="currentTab" class="d-none d-sm-flex app__tab">
          <v-tab
            v-for="(tab, index) in tabs"
            :key="index"
            :text="tab.name"
            :value="tab.name"
            :href="tab.href ? tab.href : undefined"
            @click="handleNavigation(tab)"
          >
            {{ tab.name }}
          </v-tab>
        </v-tabs>

        <v-menu transition="slide-y-transition">
          <template v-slot:activator="{ props }">
            <v-app-bar-nav-icon
              class="d-flex d-sm-none app__tab ml-auto"
              style="padding-right: 1rem"
              v-bind="props"
            />
          </template>

          <v-list>
            <v-list-item
              v-for="(item, i) in homeTabs"
              :key="i"
              :value="i"
              @click="handleNavigation(item)"
            >
              <v-list-item-title>{{ item.name }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>
    </v-layout>
  </ClientOnly>
</template>

<script setup lang="ts">
import { useGoTo } from "~/composables/useGoTo";
import { useRoute } from "#vue-router";

const route = useRoute();
const currentTab = ref({ name: "O nás", ref: "#about", href: "o-nas" });

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
  { name: "Aktuality", ref: "", href: "/aktuality" },
  { name: "Kontakty", ref: "", href: "/kontakty" },
];

const tabs = computed(() => (route.path === "/" ? homeTabs : otherTabs));

const handleNavigation = (tab: any) => {
  if (tab.ref) {
    useGoTo(tab.ref);
  } else if (tab.href) {
    window.location.href = tab.href;
  }
};
</script>