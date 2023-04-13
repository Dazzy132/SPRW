import React, {useEffect, useState} from 'react';
import axios from "axios";
import {baseUrl} from "../api/routes";
import {useDispatch, useSelector} from "react-redux";
import {
  loginFailure,
  loginRequest,
  loginSuccess,
  logout
} from "../store/reducers/auth/actions";

const AuthPage = () => {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")
  const dispatch = useDispatch()

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      dispatch(loginSuccess(token));
    }
  }, [dispatch]);

  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)

  function loginButton(e) {
    e.preventDefault()
    dispatch(loginRequest())
    axios.post(`${baseUrl}/auth/login/`, {username, password})
      .then(response => {
        dispatch(loginSuccess(response.data["access_token"]))
        localStorage.setItem("token", response.data["access_token"])
        console.log(response)
      })
      .catch(e => {
        dispatch(loginFailure(e.message))
        setError(e.response.data.non_field_errors)
      })
  }

  function logoutButton(e) {
    e.preventDefault()
    const token = localStorage.getItem('token');

    axios.post(`${baseUrl}/auth/logout/`, null, {
      headers: {Authorization: `Bearer ${token}`}
    })
      .then(() => {
          localStorage.removeItem("token");
          dispatch(logout())
        }
      )
      .catch(e => setError(e.response.data.non_field_errors))
  }

  return (
    <div>

      {error &&
        <h1 style={{color: "red"}}>Произошла ошибка: {error}</h1>
      }

      {isAuthenticated ?
        <form onSubmit={logoutButton}>
          <div style={{marginBottom: 20}}>Вы авторизованы</div>
          <button>Выйти из аккаунта</button>
        </form>
        :
        <form onSubmit={loginButton}>
          <label htmlFor="loginOrEmail">Логин
            <input
              id="loginOrEmail"
              type="text"
              onChange={event => setUsername(event.target.value)}
            />
          </label>

          <br/>

          <label htmlFor="password">Пароль
            <input
              id="password"
              type={"password"}
              onChange={event => setPassword(event.target.value)}
            />
          </label>

          <br/>

          <button type="submit">
            Авторизоваться
          </button>
        </form>

      }

    </div>
  );
};

export default AuthPage;