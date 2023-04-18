import React, {useContext, useState} from 'react';
import axios from "axios";
import {baseUrl} from "../api/routes";
import AuthContext from "../context/AuthContext";
import UserContext from "../context/UserContext";
import {Navigate, useNavigate} from "react-router-dom";


const LogoutPage = () => {
  const [error, setError] = useState("")
  const history = useNavigate()

  const {loggedIn} = useContext(AuthContext)
  const {user} = useContext(UserContext)

  function logoutButton(e) {
    e.preventDefault()
    const token = localStorage.getItem('token');

    axios.post(`${baseUrl}/auth/logout/`, null, {
      headers: {Authorization: `Bearer ${token}`}
    }).then(() => {
        localStorage.removeItem("token");
        history('/login/')
      }
    ).catch(e => setError(e.response.data.non_field_errors))
  }

  return (
    <div>

      {error &&
        <h1 style={{color: "red"}}>Произошла ошибка: {error}</h1>
      }

      {loggedIn &&
        <form onSubmit={logoutButton}>
          <div style={{marginBottom: 20}}>Вы авторизованы под {user.username}</div>
          <button>Выйти из аккаунта</button>
        </form>
      }

    </div>
  );
};

export default LogoutPage;