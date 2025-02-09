<template>
    <v-app-bar  style="position: sticky">
     <v-app-bar-nav-icon
         @click="drawer = !drawer"
         class="d-flex d-sm-none"
     />
      <span class="mdi mdi-dance-ballroom" style="font-size: 60px"></span>
      Taneční klub Ostrava
          <v-tabs
            v-model="tab"
            align-with-title
            class="d-none d-sm-flex"
          >

            <v-tab
              v-for="item in items"
              :key="item"
            >
              {{ item }}
            </v-tab>
          </v-tabs>
    </v-app-bar>

    <!-- Add a navigation bar -->
    <v-navigation-drawer
      v-model="drawer"
      absolute
      fixed
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item>
          <v-list-item v-for="(item, index) in items">
            <v-list-item-title @click="tab = index">{{ item }}</v-list-item-title>
          </v-list-item>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</template>

<script>
export default {
  el: '#app',
  data () {
    return {
      drawer: false,
      tab: null,
      items: [
        'O nás', "Trenéři", 'Kurzy', 'Galerie', 'Aktuality', 'Kontakty',
      ],
    }
  }
}
</script>