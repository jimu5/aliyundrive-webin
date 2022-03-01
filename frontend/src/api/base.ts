import axios from 'axios'
import { ResponseResult } from './types/base'

axios.defaults.baseURL = 'api/'

export function get(url: string, params: object): Promise<any> {
  return new Promise((resolve, reject) => {
    axios
      .get(url, { params: params })
      .then((res: ResponseResult) => {
        resolve(res.data)
      })
      .catch((err: ResponseResult) => {
        reject(err.data)
      })
  })
}
