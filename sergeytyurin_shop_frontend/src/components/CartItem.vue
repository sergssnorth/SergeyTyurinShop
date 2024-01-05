<template>
    <tr>
        <td><router-link :to="item.product.get_absolute_url"><span>{{ item.product.name }}</span></router-link></td>
        <td>{{ item.size }}</td>
        <td>{{ item.product.price }} ₽</td>
        <td>
            <a @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle"></i></span></a>
            {{ item.quantity }}
            <a @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle"></i></span></a>
        </td>
        <td>{{ getItemTotal(item).toFixed(2) }} ₽</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }

            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1

            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)
            this.updateCart()
        },
    },
}
</script>


<style lang="scss">

a {
    color: #333;
    text-decoration: none;
}

a:hover {
    color: #000;
    text-decoration: none;
}
</style>