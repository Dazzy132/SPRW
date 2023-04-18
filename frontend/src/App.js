import './styles/main.css'
import {useNavigate} from "react-router-dom";
import AppRouter from "./components/AppRouter";
import * as React from "react";
import {useEffect, useState} from "react";
import AuthContext from "./context/AuthContext";
import UserContext from "./context/UserContext";
import {baseUrl} from "./api/routes";
import axios from "axios";
import Loader from "./components/Loader";

function App() {

  const [loggedIn, setLoggedIn] = useState(false)
  const [user, setUser] = useState({})
  const [isLoading, setIsLoading] = useState(true)
  const history = useNavigate()

  function getCurrentUser(token) {
    return axios.get(`${baseUrl}/auth/user/`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    }).then(response => response.data)
      .catch(error => {
        history('/auth/')
        setLoggedIn(false)
      })
      .finally(() => setIsLoading(false))
  }

  useEffect(() => {
    const token = localStorage.getItem("token")

    if (token) {
      getCurrentUser(token)
        .then(data => {
          setUser(data)
          setLoggedIn(true)
        })
    }

    setIsLoading(false)
  }, [])

  if (loggedIn === null) {
    return (
      <Loader/>
    )
  }

  return (
    <AuthContext.Provider
      value={{loggedIn, setLoggedIn, isLoading, setIsLoading}}>
      <UserContext.Provider value={{user, setUser}}>
        <AppRouter/>
      </UserContext.Provider>
    </AuthContext.Provider>
  );

}

export default App;
