import {applyMiddleware, combineReducers, createStore} from "redux";
import {authReducer} from "./reducers/auth";
import thunk from "redux-thunk";

const rootReducer = combineReducers({
  auth: authReducer,
})

export const store = createStore(
  rootReducer, window._REDUX_DEVTOOLS_EXTENSION_ && window.__REDUX_DEVTOOLS_EXTENSION__(),
  applyMiddleware(thunk)
)