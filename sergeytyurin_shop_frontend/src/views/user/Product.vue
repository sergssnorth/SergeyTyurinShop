<template>
        <div class="container-fluid">
            <div class="row">
                <div class="col-8">
                    <div class="row"> 
                        <div class="col-lg-6 px-0">
                            <div class="card rounded-0 border-0">
                                <img v-bind:src="product.get_image1" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />

                                <img v-bind:src="product.get_image3" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                        <div class="col-lg-6 px-0">
                            <div class="card rounded-0 border-0">
                                <img v-bind:src="product.get_image2" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />

                                <img v-bind:src="product.get_image4" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-4"> 
                    <h1 class="">{{ product.name }}</h1>
                    <h3 class="">Цена: {{ product.price }} ₽</h3>

                    <template v-if="availableProductSize">

                        <div class="list-group list-group-horizontal mb-3">
                            <a href="#" v-for = "size in product.available_product_size" class="list-group-item" v-bind:class="{ 'active' : isSelected(size.size_name) }" v-on:click="selected = size.size_name"> {{ size.size_name }}</a>
                        </div>

                        <div class="row  p-0">
                            <div class="col-4">
                                <div class="btn-group btn-group-sm mb-3" role="group" aria-label="Basic outlined example">
                            <button type="button" @click="quantityMinus" class="btn"><i class="bi bi-dash-circle" style="font-size: 24px"></i></button>
                            <input type="number" class="form-control border-0 text-center " v-model="quantity" aria-describedby="button-addon1">
                            <button type="button" @click="quantityPlus" class="btn"><i class="bi bi-plus-circle" style="font-size: 24px"></i></button>
                        </div>
                            </div>
                            <div class="col-8">
                            </div>
                        </div>
                        
                        
                            <button type="button" class="btn btn-dark" @click="addToCart()">Добавить в корзину</button>
                            <button type="button" class="btn" style="outline: 0 !important"><i class="bi bi-heart mx-3" @click="addToFavorite()" style="font-size: 20px"></i></button>
                        
                        
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
import ModalImage from '@/components/ModalImage'

export default {
    name: 'Product',
    data() {
        return {
            selected: 0,
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
    components: {
        ModalImage
    },
    mounted() {
        this.getProduct() 
    },
    computed: {
        availableProductSize() {
            if (this.product.available_product_size.length > 0) {
                return true
            }
        }
    },
    methods: {
        isSelected: function (i) {
            return i === this.selected
        },
        quantityPlus() {
            this.quantity += 1
        },
        quantityMinus() {
            this.quantity -= 1
        },

        async getProduct() {
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
        },
        addToFavorite() {
            const item = {
                product: this.product,
            }
            this.$store.commit('addToFavorite', item)
        }
    }
}
</script>


<style lang="scss">
button:focus {
  outline:  0 !important;
  border:none;
}

.list-group-item.active {
    color: #fff;
    background-color: #333;
    border-color: #333;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    /* display: none; <- Crashes Chrome on hover */
    -webkit-appearance: none;
    margin: 0; /* <-- Apparently some margin are still there even though it's hidden */
}

input[type=number] {
    -moz-appearance:textfield; /* Firefox */
}


</style>
