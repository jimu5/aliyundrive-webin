<template>
  <div>
    <el-container>
      <el-header>
        <h2>搜索</h2>
      </el-header>
      <el-main>
        <el-row :gutter="20" style="margin-bottom: 30px">
          <el-col :span="16" :offset="4">
            <el-input v-model="searchWord" placeholder="请输入">
              <template #prefix>
                <el-icon class="el-input__icon"><search /></el-icon>
              </template>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button v-loading.fullscreen.lock="isLoading" :icon="Search" circle @click="search"></el-button>
          </el-col>
        </el-row>
        <el-row
          :gutter="5"
          v-for="data in searchData"
          :key="data"
          style="margin-bottom: 15px"
        >
          <el-col :span="20" :offset="2">
            <el-card shadow="hover">
              <div>
                <span> {{ data.name }} </span>
                <el-button @click="download(data.file_id)" style="float: right"
                  >下载</el-button
                >
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
      isLoading: false,
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
      this.isLoading = true
      searchFile({ filename: this.searchWord })
        .then(res => {
          this.searchData = res as JSON
          this.isLoading = false
        })
        .catch(err => {
          this.isLoading = false
          ElMessage.error('Oops, this is a error message.' + err)
        })
    },

    download(file_id: string) {
      const newWindow: any = window.open('', '_blank')
      getDownloadUrl({ file_id: file_id })
        .then((res: getDownloadRes) => {
          newWindow.eval(`location.replace("${res.download_url}")`)
        })
        .catch((err: getDownloadRes) => {
          newWindow.close()
          ElMessage.error('Oops, this is a error message.' + err)
        })
    }
  }
})
</script>
