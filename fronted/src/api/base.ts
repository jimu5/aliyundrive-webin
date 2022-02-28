import axios from 'axios'

axios.defaults.baseURL = 'api/'

export function get(url: string, params: object) {
  return new Promise((resolve, reject) => {
    axios
      .get(url, { params: params })
      .then(res => {
        resolve(res.data)
      })
      .catch(err => {
        reject(err.data)
      })
  })
}
