import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import { library } from "@fortawesome/fontawesome-svg-core";
import { faPlus, faMinus, faUser, faCartPlus, faCartShopping, faTruckMoving, faBoxArchive, faInfoCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faPlus, faMinus, faUser, faCartPlus, faCartShopping, faTruckMoving, faBoxArchive, faInfoCircle)

axios.defaults.baseURL = "http://127.0.0.1:8000"
createApp(App).use(store).use(router, axios).component('font-awesome-icon', FontAwesomeIcon).mount('#app')

