<template>
  <div>
    <el-container>
      <el-header>
        <h2>搜索</h2>
      </el-header>
      <el-main>
        <el-row :gutter="20">
          <el-col :span="12" :offset="6">
            <el-input v-model="searchWord" placeholder="请输入">
              <template #prefix>
                <el-icon class="el-input__icon"><search /></el-icon>
              </template>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button :icon="Search" circle @click="search"></el-button>
          </el-col>
        </el-row>
        <el-row :gutter="20" v-for="data in searchData" :key="data">
          <el-col :span="12" :offset="6">
            <el-card shadow="hover">
              <div style="padding: 14px">
                <span> {{ data.name }} </span>
                <el-button @click="download(data.file_id)">下载</el-button>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { Search } from '@element-plus/icons-vue'
</script>

<script lang="ts">
import { defineComponent } from 'vue'
import { searchFile, getDownloadUrl } from '../api/search'
import { ElMessage } from 'element-plus'
import { getDownloadRes } from '../api/types/search'

export default defineComponent({
  name: 'SearchView',
  data() {
    return {
      searchWord: '',
      searchData: JSON
    }
  },
  methods: {
    search() {
      if (this.searchWord === '') {
        ElMessage.error('请输入搜索内容')
        return
      }
      searchFile({ filename: this.searchWord })
        .then(res => {
          this.searchData = res as JSON
        })
        .catch(err => {
          ElMessage.error('Oops, this is a error message.' + err)
        })
    },

    download(file_id: string) {
      getDownloadUrl({ file_id: file_id })
        .then((res: getDownloadRes) => {
          window.open(res.download_url)
        })
        .catch((err: getDownloadRes) => {
          ElMessage.error('Oops, this is a error message.' + err)
        })
    }
  }
})
</script>
