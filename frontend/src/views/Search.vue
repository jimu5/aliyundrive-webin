<template>
  <el-container style="height: 95%">
    <el-header height="115px">
      <h2>搜索</h2>
      <el-row :gutter="20">
        <el-col :span="16" :offset="4">
          <el-input v-model="searchWord" placeholder="请输入" @keyup.enter="search">
            <template #prefix>
              <el-icon class="el-input__icon"><search /></el-icon>
            </template>
          </el-input>
        </el-col>
        <el-col :span="2">
          <el-button v-loading.fullscreen.lock="isLoading" :icon="Search" circle @click="search"></el-button>
        </el-col>
      </el-row>
    </el-header>
    <el-main>
      <el-row v-if="none_result_flag" style="margin-bottom: 8px">
        <el-col :span="20" :offset="2">
          <p>未搜索到相关数据</p>
        </el-col>
      </el-row>
      <div
        v-infinite-scroll="scrollDataLoad"
        :infinite-scroll-disabled="isLoading || next_page_marker === ''"
        infinite-scroll-delay="1000"
      >
        <el-row
          :gutter="5"
          v-for="data in searchData"
          :key="data"
          style="margin-bottom: 15px"
        >
          <el-col :span="20" :offset="2">
            <el-card shadow="hover">
              <div>
                <span class="text item" style="word-break: break-all"> {{ data.name }} </span>
                <el-button @click="download(data.file_id)" style="float: right"
                  >下载</el-button
                >
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row v-if="next_page_marker !== ''" style="margin-bottom: 8px">
          <el-col :span="20" :offset="2">
            <p>...</p>
          </el-col>
        </el-row>
      </div>
    </el-main>
  </el-container>
</template>

<script lang="ts" setup>
import { Search } from '@element-plus/icons-vue'

document.title = "搜索"
</script>

<script lang="ts">
import { defineComponent } from 'vue'
import { searchFile, getDownloadUrl } from '../api/search'
import { ElMessage } from 'element-plus'
import { getDownloadRes, getSearchResultRes } from '../api/types/search'

export default defineComponent({
  name: 'SearchView',
  data() {
    return {
      isLoading: false,
      searchWord: '',
      searchData: [],
      next_page_marker: '',
      none_result_flag: false,
      times: 3,
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
        .then((res: getSearchResultRes) => {
          this.searchData = res.result
          this.isLoading = false
          this.next_page_marker = res.next_page_marker
          if (this.searchData.length === 0) {
            this.none_result_flag = true
          } else {
            this.none_result_flag = false
          }
        })
        .catch(err => {
          this.isLoading = false
          ElMessage.error('Oops, this is a error message.' + err)
        })
    },

    scrollDataLoad() {
      if (this.times === 0) {
        return
      }
      this.times -= 1
      if (this.isLoading) {
        return
      }
      this.isLoading = true
      searchFile({ filename: this.searchWord, page_marker: this.next_page_marker })
        .then((res: getSearchResultRes) => {
          this.searchData.push(...res.result)
          this.isLoading = false
          this.next_page_marker = res.next_page_marker
          if (this.searchData.length === 0) {
            this.none_result_flag = true
          } else {
            this.none_result_flag = false
          }
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
    },
  }
})
</script>
