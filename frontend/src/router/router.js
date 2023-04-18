import MainPage from "../pages/MainPage";
import LoginPage from "../pages/LoginPage";
import PostList from "../components/PostList";
import LogoutPage from "../pages/LogoutPage";
import SignUpTemplate from "../pages/SignUp";

export const publicRoutes = [
  {path: "/", element: MainPage},
  {path: "login/", element: LoginPage},
  {path: "logout/", element: LogoutPage},
  {path: "signup/", element: SignUpTemplate},
  {path: "posts/", element: PostList},
]

export  const privateRoutes = [

]