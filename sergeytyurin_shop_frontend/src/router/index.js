import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import AdminHome from '../views/admin/AdminHome.vue'
import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'
import Home from '../views/user/Home.vue'


const routes = [
  {
    path: '/admin',
    name: 'AdminHome',
    component: AdminHome
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
