<template>
    <nav class="navbar fixed-top navbar-expand-lg shadow-sm p-3 mb-5 bg-body">
        <div class="container-fluid justify-content-between">
            
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCategories" aria-controls="navbarCategories" aria-expanded="false" aria-label="Toggle navigation">
                <i class="bi bi-heart" style="font-size: 20px"></i>
            </button>

            <div class="d-lg-none">
                <router-link to="/">
                    <a class="navbar-brand" href="#" style="margin-right: 0">
                        <img src="@/assets/ShortLogo.png" width="46" height="28">
                    </a>
                </router-link>
            </div>

            <div class="d-lg-none">
                <div class="">
                    <router-link to="/cart">
                        <i class="px-2 bi bi-person-circle" style="font-size: 24px"></i>
                    </router-link>

                    <router-link to="/cart">
                        <i class="px-2 bi bi-bag" style="font-size: 24px"></i>
                    </router-link>
                </div>
            </div>


            <div class="collapse navbar-collapse" id="navbarCategories">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Мужчины
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Женщины
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </li>
                </ul>
            </div>

            

            <div class="collapse navbar-collapse justify-content-center" id="navbarLogo">
                <router-link to="/">
                    <a class="navbar-brand" href="#" style="margin-right: 0">
                        <img src="@/assets/LogoST.png" width="168" height="28">
                    </a>
                </router-link>
            </div>
            
            <div class="collapse navbar-collapse justify-content-end" id="navbarMenu">
                <div class="">
                    <router-link to="/my-account">
                        <i class="px-2 bi bi-person-circle" style="font-size: 24px"></i>
                    </router-link>

                    <router-link to="/favourite">
                        <i class="px-2 bi bi-bookmark-heart" style="font-size: 24px"></i>
                    </router-link>

                    <router-link to="/cart">
                        <i class="px-2 bi bi-bag" style="font-size: 24px"></i>
                    </router-link>
                </div>
                
                    
                
                <!-- <div class="container">
                    <div class="row"></div>
                </div> -->
            </div>
            
        </div>
    </nav>


    <section class="section is-spaced">
      <router-view/>
    </section>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            showCategoryMen: false,
            showMobileMenu: false,
            cart: {
                items: []
            },
            big_categories: [],
            categories: [],
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
    async mounted() {
    document.body.classList.add('has-navbar-fixed-top')
    this.cart = this.$store.state.cart
    await this.getBigCategories()
    await this.getCategories()
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
      async getBigCategories() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get('/api/v1/big-categories/')
                    .then(response => {
                        this.big_categories = response.data
                        console.log(this.big_categories)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            this.$store.commit('setIsLoading', false)
        },

        async getCategories() {
            this.$store.commit('setIsLoading', true)

            
            var big_categories = this.big_categories
            await Promise.all(
                big_categories.map(async (big_category) => {
                await axios
                    .get(`/api/v1/categories/${big_category.slug}/`)
                    .then(response => {
                        this.categories.push(response.data)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }))
            console.log("1")
            console.log(this.categories)
            console.log("1")
            
            this.$store.commit('setIsLoading', false)
        },
    }
}
</script>


<style lang="scss">
@import "../node_modules/bootstrap/scss/functions";
@import "../node_modules/bootstrap/scss/variables";
@import "../node_modules/bootstrap/scss/variables-dark";

body { padding-top: 73px; }


button.navbar-toggler {
    color: $gray-800;
    border-color: $gray-800;
}

button.navbar-toggler:focus {
    color: $black;
    border-color: $black;
}



a#navbarDropdown {
    color: $gray-800;
}

a#navbarDropdown:hover {
    color: $black;
}

a#navbarDropdown:active {
    color: $black;
}

.bi-bag {
    color: $gray-800;
}

.bi-bag:hover {
    color: $black;
}

.bi-person-circle {
    color: $gray-800;
}

.bi-person-circle:hover {
    color: $black;
}

.bi-bookmark-heart {
    color: $gray-800;
}

.bi-bookmark-heart:hover {
    color: $black;
}


#app {
    font-family: 'Geologica', sans-serif;
    font-weight: 500;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
}
</style>
