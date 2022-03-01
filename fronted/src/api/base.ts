import axios from 'axios'

axios.defaults.baseURL = 'api/'

export function get(url: string, params: object) {
  return new Promise((resolve, reject) => {
    axios
      .get(url, { params: params })
      .then((res: any) => {
        resolve(res.data)
      })
      .catch((err: any) => {
        reject(err.data)
      })
  })
}
