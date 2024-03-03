<template>
  <div id="nav">
    <router-link class="link" to="/">home</router-link> |
    <router-link class="link" to="/check-object">recyclable?</router-link> |
    <router-link class="link" to="/quiz-time">quiz-time!</router-link> |
  </div>
  <div class="container">
    <router-view></router-view>
  </div>
</template>

<!-- <script>
import { useRouter } from 'vue-router';

export default {
  name: 'App',
  setup() {
    const router = useRouter()
  },
}
</script> -->

<style>
.link{
  color: #009900;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
