// class Api {
//   constructor(url, headers) {
//     this._url = url
//     this._headers = headers
//   }
//
//   getPosts() {
//     const token = localStorage.getItem("token")
//     return fetch("/api/v1/posts/",
//       {method: "GET", headers: {...this._headers}}
//     )
//   }
// }
//
// export default new Api(
//   'http://localhost:8000', { 'content-type': 'application/json' }
// )


import axios from "axios";
import {baseUrl} from "./routes";


export default function getUser() {
  const token = localStorage.getItem("token")
  return axios.get(`${baseUrl}/auth/user/`, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }
  }).then(response => response.data)
}