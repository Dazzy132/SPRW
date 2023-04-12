import {LOGIN_FAILURE, LOGIN_REQUEST, LOGIN_SUCCESS, LOGOUT} from "./actions";

const initialState = {
  isLogged: false,
  user: null,
  error: null,
}


export const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOGIN_REQUEST:
      return {...state, isLoading: true, isAuthenticated: false}
    case LOGIN_SUCCESS: {
      return {...state, isLoading: false, isAuthenticated: true, token: action.token}
    }
    case LOGIN_FAILURE: {
      return {...state, isLoading: false, isAuthenticated: false, error: action.error}
    }
    case LOGOUT: {
      return {...state, isLoading: false, isAuthenticated: false}
    }
    default:
      return state
  }
}
