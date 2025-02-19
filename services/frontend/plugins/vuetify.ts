// import this after install `@mdi/font` package
import '@mdi/font/css/materialdesignicons.css'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import {VIcon} from "vuetify/components";
import {VCalendar} from "vuetify/labs/VCalendar";

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    components: {
      VCalendar,
    },
    icons: {  // https://pictogrammers.com/library/mdi/icon/youtube/
      defaultSet: 'mdi',
    },
    theme: {
      defaultTheme: 'light',
      themes: {
        light: {
          colors: {
            background: '#ffffff',
            primary: '#303030',
            'primary-darken': '#d0d0d0',
            secondary: '#606060',
            'secondary-darken': '#a0a0a0',
            color: '#CF3476',
            light: '#d0d0d0',
            dark: '#303030'
          },
        },
        // dark: {
        //   colors: {
        //     background: '#000',
        //     primary: '#d0d0d0',
        //     'primary-darken': '#303030',
        //     secondary: '#a0a0a0',
        //     'secondary-darken': '#606060',
        //     color: '#CF3476',
        //   }
        // }
      },
    },
    aliases: {
      SmallIcon: VIcon,
      BigIcon: VIcon,
    },
    defaults: {
      SmallIcon: {
        color: 'color',
        style: [{ 'margin-left': '20px', 'margin-top': '15px', 'font-size': '30px'}]
      },
      BigIcon: {
        color: 'color',
        style: [{ margin: '20px', 'font-size': '60px'}]
      },
    },
    locale: {
      locale: 'cs',
    },
    date: {
      locale: {
        cs: 'cs-CZ',
      }
    }
  })

  app.vueApp.use(vuetify)
})
