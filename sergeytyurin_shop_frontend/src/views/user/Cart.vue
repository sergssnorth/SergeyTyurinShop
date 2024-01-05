<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <h1 class="title text-center">Корзина</h1>
                <table class="table" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Продукт</th>
                            <th>Размер</th>
                            <th>Цена</th>
                            <th>Количество</th>
                            <th>Сумма</th>

                        </tr>
                    </thead>

                    <tbody class="table-group-divider">
                        <CartItem
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                            v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart" />
                    </tbody>
                </table>
                <p v-else>У вас нет никаких товаров в вашей корзине...</p>

            </div>
       </div>
    </div>
</template>

<script>
import CartItem from '@/components/CartItem.vue'

export default {
    name: 'Cart',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            function RemoveItem(i) {
                if(i.product.id !== item.product.id && i.size !== item.size) {
                    return i
                }
            }
            this.cart.items = this.cart.items.filter(RemoveItem)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
    }
}
</script>