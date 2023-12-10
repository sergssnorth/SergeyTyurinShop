<template>
  <div id="wrapper">
    <nav class="navbar is-spaced is-size-5 has-shadow">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="@/assets/LogoST.png" width="168" height="28">
        </router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-targer="navbar-menu" @click="showMobileMenu =!showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">
          <div class="navbar-item has-dropdown is-hoverable is-boxed">
            <a class="navbar-link">
              Мужчины
            </a>

            <div class="navbar-dropdown">
              <a class="navbar-item">
                About
              </a>
              <a class="navbar-item">
                Jobs
              </a>
              <a class="navbar-item">
                Contact
              </a>
              <hr class="navbar-divider">
              <a class="navbar-item">
                Report an issue
              </a>
            </div>
          </div>
          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">
              Женщины
            </a>
            <div class="navbar-dropdown">
              <div class="columns">
                <div class="column">
                  <a class="navbar-item">
                    About
                  </a>
                </div>
                <div class="column">
                  <a class="navbar-item">
                    About
                  </a>
                </div>
              </div>
              <a class="navbar-item">
                About
              </a>
              <a class="navbar-item">
                Jobs
              </a>
              <a class="navbar-item">
                Contact
              </a>
              <hr class="navbar-divider">
              <a class="navbar-item">
                Report an issue
              </a>
            </div>
          </div>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">Мой аккаунт</router-link>
                <router-link to="/my-records" class="button is-info">
                  <span>Мои записи</span>
                </router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-outlined is-info"><span>Вход</span></router-link>
                <router-link to="/sign-up" class="button is-outlined is-success"><span>Регистрация</span></router-link>
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>
    
    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section is-spaced">
      <router-view/>
    </section>
    
  </div>
</template>


<style lang="scss">
@import '../node_modules/bulma';

.button.is-info.is-outlined {
  background-color: transparent;
  border-color: #333;
  color: #333;
}

.button.is-info.is-outlined:hover{
  background-color: #333;
  border-color: #fff;
  color: #fff;
}

.router-link-active.router-link-exact-active.button.is-outlined.is-info {
  background-color: transparent;
  border-color: #333;
  color: #333;
}

.router-link-active.router-link-exact-active.button.is-outlined.is-success{
  background-color: #333;
  border-color: #fff;
  color: #fff;
}

.button.is-success.is-outlined {
  background-color: #333;
  border-color: #fff;
  color: #fff;
}

.button.is-success.is-outlined:hover {
  background-color: transparent;
  border-color: #333;
  color: #333;
}

.navbar-link:not(.is-arrowless)::after{
  border-color: #333;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
* {
  margin: 0;
  padding: 0;
}

</style>
