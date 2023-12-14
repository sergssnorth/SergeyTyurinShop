import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import AdminHome from '../views/admin/AdminHome.vue'
import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'
import Home from '../views/user/Home.vue'
import Product from '../views/user/Product.vue'
import Cart from '../views/user/Cart.vue'
import Payment from '../views/user/Payment.vue'
import CategoryProduct from '../views/user/CategoryProduct.vue'



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
  {
    path: '/product/:big_category_slug/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/payment',
    name: 'Payment',
    component: Payment,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/products/:big_category_slug/:category_slug',
    name: 'CategoryProduct',
    component: CategoryProduct
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})


export default router
