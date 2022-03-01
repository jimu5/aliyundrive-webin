import { get } from './base'

export const searchFile = (p: object) => get('search', p)
export const getDownloadUrl = (p: object) => get('/get_download', p)
