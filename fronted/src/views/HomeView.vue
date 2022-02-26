<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import Search from '@/views/Search.vue' // @ is an alias to /src

@Options({
  components: {
    Search
  }
})
export default class HomeView extends Vue {}
</script>
