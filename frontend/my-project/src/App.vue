<template>
 <h2>
        Welcome to RecycleView!
    </h2>
    <button @click="$router.push('check-object')">
        Recyclable?
    </button>
    <button @click="$router.push('quiz-time')"> 
        Quiz Time!
    </button>
    <div>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
