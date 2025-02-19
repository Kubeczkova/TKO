<template>
  <ClientOnly>
    <v-layout>
      <v-app-bar style="position: fixed">
        <v-app-bar-nav-icon
            @click="drawer = !drawer"
            class="d-flex d-sm-none"
        />
        <a href="/"><big-icon icon="mdi-dance-ballroom" /></a>
        <v-app-bar-title class="app__title">Taneční klub Ostrava</v-app-bar-title>

        <v-tabs
          v-for="(tab, index) in tabs" :key="index"
          v-model="currentTab"
          align-with-title
          class="d-none d-sm-flex app__tab"
        >
          <v-tab v-if="tab.ref" :text="tab.name" :value="tab.name" @click="useGoTo(tab.ref)"></v-tab>
          <v-tab v-if="tab.href" :text="tab.name" :value="tab.name" :href="tab.href"></v-tab>
        </v-tabs>


<!--        <v-col-->
<!--          class="text-right"-->
<!--          @click="toggleTheme"-->
<!--        >-->
<!--          <big-icon icon="mdi-lightbulb-cfl"/>-->
<!--        </v-col>-->
      </v-app-bar>

      <v-fab
        :key="currentTab.ref"
        class="ms-4 mb-4"
      ></v-fab>

      <v-navigation-drawer
        v-model="drawer"
        absolute
        fixed
        left
      >
        <v-list
          nav
          dense
        >
          <v-list-item>
            <v-list-item v-for="(tab, index) in tabs" :key="index">
              <v-list-item-title @click="useGoTo(tab.ref)">{{ tab.name }}</v-list-item-title>
            </v-list-item>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-layout>
  </ClientOnly>
</template>

<script setup lang="ts">
function waitForElement (selector: string, timeout = 2000) : Promise<Element> {
  return new Promise((resolve, reject) => {
    const startTime = Date.now();
    // eslint-disable-next-line prefer-const
    let observer: MutationObserver;

    function checkElement () {
      const element = document.querySelector(selector);

      if (element) {
        resolve(element);
        observer.disconnect(); // Stop observing DOM changes
      } else if (Date.now() - startTime >= timeout) {
        reject(new Error(`Timeout exceeded while waiting for element with selector '${selector}'`));
        observer.disconnect(); // Stop observing DOM changes
      }
    }

    observer = new MutationObserver(checkElement);
    observer.observe(document.body, { childList: true, subtree: true });

    checkElement(); // Check initially in case the element is already present
  });
}


async function useGoTo (selector: string, props: {offset? :number} = {}): Promise<void> {
  console.log(selector);
  let element: Element;
  try {
    element = await waitForElement(selector);
  } catch {
    // element not found
    return;
  }
  const yOffset = props?.offset ?? -80;
  const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;

  window.scrollTo({ top: y, behavior: "smooth" });
}

const currentTab = ref({name: 'O nás', ref: "#about", href: "o-nas"});
const drawer = ref(null)
const tabs = [
  {name: 'O nás', ref: "#about", href: ""},
  {name: "Trenéři", ref: "#trainers", href: ""},
  {name: 'Kurzy', ref: "#courses", href: ""},
  {name: 'Galerie', ref: "", href: "/galerie"},
  {name: 'Aktuality', ref: "#article", href: ""},
  {name: 'Kontakty', ref: "", href: "/kontakty"},
]

// import { useTheme } from 'vuetify'
//
// const theme = useTheme()
//
// function toggleTheme () {
//   theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
// }

</script>