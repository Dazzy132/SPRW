export const LOGIN_REQUEST = "LOGIN_REQUEST";
export const LOGIN_SUCCESS = "LOGIN_SUCCESS"
export const LOGIN_FAILURE = "LOGIN_FAILURE"
export const LOGOUT = "LOGOUT"

export const loginRequest = () => ({
  type: LOGIN_REQUEST,
  isAuthenticated: false,
  isLoading: true
})

export const loginSuccess = (token) => ({
  type: LOGIN_SUCCESS,
  token,
  isAuthenticated: true,
  isLoading: false
})

export const loginFailure = (error) => ({
  type: LOGIN_FAILURE,
  error,
  isAuthenticated: false,
  isLoading: false
})

export const logout = () => ({
  type: LOGOUT,
  isAuthenticated: false,
})
