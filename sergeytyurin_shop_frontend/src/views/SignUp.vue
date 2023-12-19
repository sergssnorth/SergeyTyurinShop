<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Регистрация</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Логин</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label>Повторите пароль</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark is-outlined mt-5">Регистрация</button>
                        </div>
                    </div>

                    <hr>
                    Или <router-link to="/log-in">кликните здесь</router-link> для Входа!
                    Нажимая кнопку "Получить код", Вы соглашаетесь c условиями <router-link to="/log-in">политики конфиденциальности</router-link>
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('Поле логин не заполнено!')
            }

            if (this.password === '') {
                this.errors.push('Поле пароль не заполнено!')
            }

            if (this.password2 === '') {
                this.errors.push('Поле поворите пароль не заполнено!')
            }


            if (this.password !== this.password2) {
                this.errors.push('Поле пароль и повторите пароль не заполнено!')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        toast({
                            message: 'Аккаунт создан, Вы можете войти!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>

<style lang="scss">
.button.is-success.is-outlined.mt-5:active{
    background-color: #333;
}


</style>