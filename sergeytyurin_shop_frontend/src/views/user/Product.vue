<template>
    <div class="page-product">
        <div class="columns">
            <div class="column is-8">   
                <div class="columns is-multiline is-gapless">
                    <div class="column is-6">
                        <figure class="image">
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
                <h3 class="title is-size-4">Цена: {{ product.price }} ₽</h3>

                <template v-if="availableProductSize">
                    <div class="tabs is-toggle">
                        <ul>
                            <li v-for="size in product.available_product_size" v-bind:class="{ 'is-active': isActive == size.size_name }">
                                <a v-on:click="isActive = size.size_name">
                                    {{ size.size_name }}
                                </a>
                            </li>
                        </ul>
                    </div>

                    <div class="columns is-mobile is-gapless">
                        <div class="column mr-1">
                            <button class="button is-outlined is-dark" @click="quantityMinus"><font-awesome-icon icon="fa-solid fa-minus"/></button>
                        </div>
                        <div class="column is-2">
                            <input class="input " min="1" v-model="quantity">
                        </div>
                        <div class="column ml-1">
                            <button class="button is-outlined is-dark" @click="quantityPlus"><font-awesome-icon icon="fa-solid fa-plus" /> </button>
                        </div>
                        <div class="column is-8">
                        </div>
                    </div>
                    <div class="field has-addons mt-2">
                        <div class="control">
                            <a class="button is-outlined is-dark" @click="addToCart()">Добавить в корзину</a>
                        </div>
                    </div>

                </template>
                <template v-else>
                    <span class="title is-4">Нет в наличии</span>
                </template>
                
                <div>
                    <div class="divider">Информация</div>
                </div>

                <p class="mb-1"><span class="title is-6">Описание: </span>Эта футболка из мягкого хлопкового джерси, сочетающая визуальные признаки вечной роскоши с
                современной графической привлекательностью, украшена фирменным логотипом amiri и мотивом ma
                в сезонном градиенте. этот чай является культовой эмблемой мира и прекрасно сочетается с
                домашней джинсовой одеждой, брюками или шортами.</p>
                <p class="mb-1"><span class="title is-6">Коллекция: </span>до весны 2024 года</p>
                <p class="mb-1"><span class="title is-6">Производство: </span>сделано в италии</p>
                <p class="mb-1"><span class="title is-6">Состав: </span>100% хлопок</p>
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
            isActive: 'L',
            product: {
                id : 0,
                name: "",
                get_absolute_url: "",
                price: "",
                get_image1: "",
                get_image2: "",
                get_image3: "",
                get_image4: "",
                available_product_size: []
            },
            quantity: 1
        }
    },
    mounted() {
        this.getProduct() 
    },
    computed: {
        availableProductSize() {
            console.log(this.product.available_product_size)
            console.log(this.product.available_product_size.length)
            if (this.product.available_product_size.length > 0) {
                return true
            }
        }
    },
    methods: {
        quantityPlus() {
            this.quantity += 1
        },
        quantityMinus() {
            this.quantity -= 1
        },

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
                size: this.isActive,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'Продукт добавлен в корзину',
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


<style lang="scss">
@import '../../../node_modules/bulma';
@import '../../../node_modules/~@creativebulma/bulma-divider';
.tabs.is-toggle li.is-active a {
  background-color: #333;
  color: #fff;
}

.button.is-dark.is-outlined:focus{
    background-color: transparent;
    border-color: hsl(0, 0%, 21%);
    color: hsl(0, 0%, 21%);
}

.button.is-dark.is-outlined:active{
    background-color: transparent;
    border-color: hsl(0, 0%, 21%);
    color: hsl(0, 0%, 21%);
}


.input {
    background-color: hsl(0, 0%, 100%);
    border-color: #333;
    border-radius: 4px;
    color: hsl(0, 0%, 21%);
}

span {
    color: #333
}

</style>