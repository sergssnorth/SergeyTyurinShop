<template>
    <div class="container-fluid">
        <div class="row justify-content-center d-flex align-items-center min-vh-100">
            <div class="col-4">
                <div class="card">
                    <div class="card-body">
                        <form>
                            <div class="text-center">
                                <h1>Вход</h1>
                            </div>
                            <div class="form-floating mb-3">
                                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                                <label for="floatingInput">Логин</label>
                            </div>
                            <div class="form-floating mb-3">
                                <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                                <label for="floatingPassword">Пароль</label>
                            </div>
                            <div class="form-floating mb-3">
                                <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                                <label for="floatingPassword">Повторите пароль</label>
                            </div>
        
                            <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
                            </form>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

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
.row {
    padding-bottom: 10rem;
}
</style>