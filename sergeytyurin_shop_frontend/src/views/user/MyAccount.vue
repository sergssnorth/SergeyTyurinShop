<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-8">
                <h1 v-if="nameIsPresent" class="title is-size-4">Здравствуйте, {{ first_name }}</h1>
                <h1 v-else  class="title is-size-4">Здравствуйте</h1>
            </div>
            <div class="column is-2"></div>
            <div class="column is-2 customcolumn">
                <button @click="logout()" class="button is-danger">Выйти</button>
            </div>

            <div class="column is-12 mb-0">
                <p class="has-text-grey mb-4">* Все поля обязательны к заполнению</p>
                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>Имя*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Фамилия*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.sname">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="accountInformation.email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Телефон*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Область*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.client_delivery_information[0].region">
                            </div>
                        </div>

                        <div class="field">
                            <label>Город*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.client_delivery_information[0].city">
                            </div>
                        </div>

                        <div class="field">
                            <label>Улица*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.client_delivery_information[0].street">
                            </div>
                        </div>

                        <div class="field">
                            <label>Дом*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.client_delivery_information[0].building">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <button class="button is-dark" @click="submitForm">Сохранить</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Checkout',
    data() {
        return {
            user_id: 0,
            accountInformation: {
                client_delivery_information: [
                    {
                        region: "",
                        city: "",
                        street: "",
                        building: ""
                    }
                ],
                name: "",
                sname: "",
                email: "",
                phone: ""
            },

            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            city: '',
            address: '',
            building: '',
            errors: [],
            nameIsPresent: false,
        }
    },
    async mounted() {
        document.title = 'Аккаунт'
        await this.getUserId()
        await this.getClientInformation()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        },

        async getUserId() {
            this.$store.commit('setIsLoading', true)
            const token = this.$store.state.token
            await axios
                .get(`/api/v1/user/get_user_id/${token}/`)
                .then(response => {
                    this.user_id = response.data[0].user_id
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },

        async getClientInformation() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get(`/api/v1/client/${this.user_id}/info/`)
                .then(response => {
                    if (response.data.length == 0) {
                        console.log("Нет")
                    }
                    else {

                        this.accountInformation = response.data[0]
                        console.log(this.accountInformation)
                    }
                    
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },


        submitForm() {
            this.errors = []

            if (this.accountInformation.name === '') {
                this.errors.push('Поле имя не заполнено!')
            }

            if (this.accountInformation.sname === '') {
                this.errors.push('Поле фамилия не заполнено!')
            }

            if (this.accountInformation.email === '') {
                this.errors.push('Поле e-mail не заполненно!')
            }

            if (this.accountInformation.phone === '') {
                this.errors.push('Поле телефон не заполненно!')
            }

            if (this.accountInformation.client_delivery_information[0].region === '') {
                this.errors.push('Поле область не заполненно!')
            }

            if (this.accountInformation.client_delivery_information[0].city === '') {
                this.errors.push('Поле город не заполненно!')
            }

            if (this.accountInformation.client_delivery_information[0].street === '') {
                this.errors.push('Поле улица не заполненно!')
            }

            if (this.accountInformation.client_delivery_information[0].building === '') {
                this.errors.push('Поле дом не заполненно!')
            }

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                
            }
        },
    },
}
</script>


<style scoped>

.button.is-info.is-outlined{
    margin-top: 30px; 
}
.customcolumn {
    display: flex;
    justify-content: flex-end;
}
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>