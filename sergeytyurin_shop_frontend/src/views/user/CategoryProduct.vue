<template>
    <div class="category_product">
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
  import ProductBox from '@/components/ProductBox'
  
  export default {
    name: 'CategoryProduct',
    data() {
      return {
        products: []
      }
    },
    components: {
      ProductBox
    },
    mounted() {
      this.getCategoryProducts()
      document.image
      document.title = 'Главная страница | СТ'
    },
    methods: {
      async getCategoryProducts() {
        const bigCategorySlug = this.$route.params.big_category_slug
        const categorySlug = this.$route.params.category_slug
        
        this.$store.commit('setIsLoading', true)
  
        await axios
          .get(`/api/v1/products/${bigCategorySlug}/${categorySlug}`)
          .then(response => {
            this.products = response.data
          })
          .catch(error => {
            console.log(error)
          })
  
        this.$store.commit('setIsLoading', false)
      }
    }
  }
  </script>