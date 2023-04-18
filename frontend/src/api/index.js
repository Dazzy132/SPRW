import axios from "axios";
import {baseUrl} from "./routes";


export default function getUser() {
  const token = localStorage.getItem("token")
  return axios.get(`${baseUrl}/auth/user/`, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    }
  })
}