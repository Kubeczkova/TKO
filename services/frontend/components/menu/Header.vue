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

        <v-tabs
          v-if="$vuetify.display.smAndUp"
          v-model="currentTabName"
          class="app__tab"
        >
          <v-tab
            v-for="(tab, index) in tabs"
            :key="index"
            :value="tab.name"
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
import { computed, onMounted, watch, nextTick } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const homeTabs = [
  { name: "O nás", href: "#about" },
  { name: "Trenéři", href: "#trainers" },
  { name: "Kurzy", href: "#courses" },
  { name: "Galerie", href: "/galerie" },
  { name: "Aktuality", href: "#article" },
  { name: "Kontakty", href: "/kontakty" },
];

const otherTabs = [
  { name: "O nás", href: "/#about" },
  { name: "Trenéři", href: "/#trainers" },
  { name: "Kurzy", href: "/#courses" },
  { name: "Galerie", href: "/galerie" },
  { name: "Aktuality", href: "/aktuality" },
  { name: "Kontakty", href: "/kontakty" },
];

const tabs = computed(() => (route.path === "/" ? homeTabs : otherTabs));

type Tab = {
  name: string;
  href: string;
};

const currentTab = ref<Tab>({ name: "O nás", href: "#about" });

const currentTabName = computed<string>({
  get: () => currentTab.value.name,
  set: (newName: string) => {
    const tab = tabs.value.find(t => t.name === newName);
    if (tab) handleNavigation(tab);
  }
});

const handleNavigation = async (tab: { name: string, href: string }) => {
  currentTab.value = tab;

  if (tab.href.startsWith("#")) {
    await scrollToHash(tab.href);
  } else if (tab.href.startsWith("/#")) {
    await router.push(tab.href);
  } else {
    await router.push(tab.href);
  }
};

async function scrollToHash(hash: string) {
  await nextTick();

  const el = document.querySelector(hash);
  if (el) {
    const yOffset = -80;
    const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;
    window.scrollTo({ top: y, behavior: 'smooth' });
  }
}

onMounted(() => {
  if (route.path === "/" && route.hash) {
    const match = homeTabs.find(tab => tab.href === route.hash);
    if (match) {
      currentTab.value = match;
    }
    scrollToHash(route.hash);
  }
});

watch(() => route.hash, (newHash) => {
  if (route.path === "/" && newHash) {
    const match = homeTabs.find(tab => tab.href === newHash);
    if (match) currentTab.value = match;
    scrollToHash(newHash);
  }
});

watch(() => route.path, (newPath) => {
  if (newPath !== "/") {
    const match = otherTabs.find(tab => tab.href === newPath || tab.href === `${newPath}${route.hash}`);
    if (match) currentTab.value = match;
  }
}, { immediate: true });

</script>