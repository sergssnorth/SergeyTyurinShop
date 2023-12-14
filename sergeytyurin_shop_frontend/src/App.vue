<template>
  <div id="wrapper">
    <nav class="navbar is-spaced is-size-5 has-shadow">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="@/assets/LogoST.png" width="168" height="28">
        </router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-targer="navbar-menu" @click="showMobileMenu =!showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">
          <div class="navbar-item has-dropdown is-hoverable is-boxed">
            <a class="navbar-link">
              Мужчины
            </a>
            <div class="navbar-dropdown">
              <a v-for="category in men_categories" class="navbar-item">
                <router-link v-bind:to="category.get_absolute_url" class="custom_a is-size-6" replace>
                  {{ category.name }}
                </router-link>
              </a>
            </div>
          </div>
          
          <div class="navbar-item has-dropdown is-hoverable is-boxed">
            <a class="navbar-link">
              Женщины
            </a>
            <div class="navbar-dropdown">
              <a v-for="category in women_categories" class="navbar-item">
                <router-link v-bind:to="category.get_absolute_url" class="custom_a is-size-6">
                  {{ category.name }}
                </router-link>
              </a>
            </div>
          </div>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-orders" class="icon is-medium"><font-awesome-icon icon="fa-solid fa-box-archive"/></router-link>
                <router-link to="/my-account" class="icon is-medium ml-3"><font-awesome-icon icon="fa-solid fa-user"/></router-link>
                <router-link to="/cart" class="icon is-medium ml-3">
                  <font-awesome-icon icon="fa-solid fa-cart-shopping"/>
                  <span class="mb-1 ml-2">{{ cartTotalLength }}</span>
                </router-link>
              </template>
              <template v-else>
                <router-link to="/log-in" class="icon is-medium"><font-awesome-icon icon="fa-solid fa-user"/></router-link>
                <router-link to="/cart" class="icon is-medium ml-3">
                  <font-awesome-icon icon="fa-solid fa-cart-shopping"/>
                  <div><span>{{ cartTotalLength }}</span></div>
                  <span>{{ cartTotalLength }}</span>
                </router-link>
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>
    
    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section is-spaced">
      <router-view/>
    </section>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      },
      men_categories: [],
      women_categories: [],
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
    this.getCategories()
  },
  computed: {
        cartTotalLength() {
            let totalLength = 0
            for (let i = 0; i < this.cart.items.length; i++) {
                totalLength += this.cart.items[i].quantity
            }
            if (totalLength == 0) {
            return ''
            }

            return totalLength
        }
    },
    methods: {
        async getCategories() {
            this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/categories/mens/')
                    .then(response => {
                        this.men_categories = response.data
                        console.log(this.men_categories)
                    })
                    .catch(error => {
                        console.log(error)
                    })
                
                    await axios
                    .get('/api/v1/categories/womens/')
                    .then(response => {
                        this.women_categories = response.data
                        console.log(this.women_categories)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.button.is-info.is-outlined {
  background-color: transparent;
  border-color: #333;
  color: #333;
}

a.navbar-link:not(.is-arrowless)::after {
  border-color: #333;
}
a.navbar-link:hover {
    color: #000;
}

.icon {
  color: #333;
}

a.custom_a {
    color: #333;
}

a.custom_a:hover {
    color: #000;
}

.icon:hover {
  color: #fff;
  stroke: black;
  stroke-width: 1.5em;
}

.button.is-info.is-outlined:hover{
  background-color: #333;
  border-color: #fff;
  color: #fff;
}

.router-link-active.router-link-exact-active.button.is-outlined.is-info {
  background-color: transparent;
  border-color: #333;
  color: #333;
}

.router-link-active.router-link-exact-active.button.is-outlined.is-success{
  background-color: #333;
  border-color: #fff;
  color: #fff;
}

.button.is-success.is-outlined {
  background-color: #333;
  border-color: #fff;
  color: #fff;
}

.button.is-success.is-outlined:hover {
  background-color: transparent;
  border-color: #333;
  color: #333;
}

.navbar-link:not(.is-arrowless)::after{
  border-color: #333;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
* {
  margin: 0;
  padding: 0;
}

</style>
