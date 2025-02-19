// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  ssr: false,
  devtools: { enabled: true },
  typescript: { typeCheck: true},
  build: {
    transpile: ['vuetify'],
  },
  runtimeConfig: {
    public: {
      backendUrl: process.env.BACKEND_URL ?? "http://localhost:8000"
    },
  },
  modules: [
   (_options, nuxt) => {
     nuxt.hooks.hook('vite:extendConfig', (config) => {
       // @ts-expect-error
       config.plugins.push(vuetify({ autoImport: true }))
     })
   },
  ],
  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },
})
