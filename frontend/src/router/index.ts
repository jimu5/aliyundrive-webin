import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Search from '../views/Search.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: Search,
    meta: {
      title: "搜索"
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
