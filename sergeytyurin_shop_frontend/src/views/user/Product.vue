<template>
    <div class="page-product">
        <div class="columns">
            <div class="column is-8">   
                <div class="columns is-multiline is-gapless">
                    <div class="column is-6">
                        <figure class="image mb-6">
                            <img v-bind:src="product.get_image1">
                            <img v-bind:src="product.get_image3">
                        </figure>
                    </div>

                    <div class="column is-6">
                        <figure class="image mb-6">
                            <img v-bind:src="product.get_image2">
                            <img v-bind:src="product.get_image4">
                        </figure>
                    </div>
                </div>
            </div>
            <div class="column is-4">   
                <h1 class="title is-size-3">{{ product.name }}</h1>

                <h3 >Price: ${{ product.price }}</h3>

                <div class="tabs is-toggle">
                    <ul>
                        <li v-if="isActiveTrue" v-bind:class="{ 'is-active': isActive == 'XS' }"><a v-on:click="isActive = 'XS'">XS</a></li>
                        <li v-bind:class="{ 'is-active': isActive == 'S' }"><a v-on:click="isActive = 'S'">S</a></li>
                        <li v-bind:class="{ 'is-active': isActive == 'M' }"><a v-on:click="isActive = 'M'">M</a></li>
                        <li v-bind:class="{ 'is-active': isActive == 'L' }"><a v-on:click="isActive = 'L'">L</a></li>
                    </ul>
                    
                    </div>

                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart()">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Product',
    data() {
        return {
            isActiveTrue: false,
            isActive: 'L',
            product: {},
            quantity: 1
        }
    },
    mounted() {
        this.getProduct() 
    },
    methods: {
        async getProduct() {
            // this.$store.commit('setIsLoading', true)

            const big_category_slug = this.$route.params.big_category_slug
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/product/${big_category_slug}/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data
                    document.title = this.product.name + ' | Djackets'
                    console.log(this.product)
                })
                .catch(error => {
                    console.log(error)
                })
            
            // this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}
</script>