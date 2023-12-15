<template>
    <div class="page-category">
        <div class="columns is-multiline">

            <ProductBox 
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import ProductBox from '@/components/ProductBox'

export default {
    name: 'Category',
    components: {
        ProductBox
    },
    data() {
        return {
            products: []
        }
    },
    mounted() {
        this.getCategory()
        const categorySlug = this.$route.params.category_slug
        document.title = categorySlug
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
                const categorySlug = this.$route.params.category_slug
                document.title = categorySlug
            }
        }
    },
    methods: {
        async getCategory() {
            const big_category_slug = this.$route.params.big_category_slug
            const categorySlug = this.$route.params.category_slug

            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/v1/products/${big_category_slug}/${categorySlug}/`)
                .then(response => {
                    this.products = response.data
                    console.log()
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Something went wrong. Please try again.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>