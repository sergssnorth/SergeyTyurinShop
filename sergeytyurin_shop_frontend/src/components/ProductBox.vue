<template>
    <div class="column is-3">
        <router-link v-bind:to="product.get_absolute_url">
            <div class="box">
                <figure class="image mb-4">
                    <img v-bind:src="product.get_image1">
                </figure>

                <h3 class="is-size-5 has-text-black">{{ product.name }}</h3>
                <p class="is-size-6 has-text-grey">₽ {{ product.price }}</p>
            </div>
        </router-link>
    </div>
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>

<style scoped>

.box {
    height: 100%;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
}

  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>