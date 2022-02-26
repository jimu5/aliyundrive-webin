<template>
  <div>
    <el-container>
      <el-header>
        <h2>搜索</h2>
      </el-header>
      <el-main>
        <el-input v-model="search_word" placeholder="请输入">
          <template #prefix>
            <el-icon class="el-input__icon"><search /></el-icon>
          </template>
        </el-input>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { Search } from '@element-plus/icons-vue'
export default {
  name: 'SearchBook',
  components: {
    Search
  },
  data() {
    return {
      search_word: '',
      search_data: ''
    }
  }
}
</script>
