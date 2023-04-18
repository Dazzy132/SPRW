import MainPage from "../pages/MainPage";
import LoginPage from "../pages/LoginPage";
import PostList from "../components/PostList";
import LogoutPage from "../pages/LogoutPage";
import SignUpTemplate from "../pages/SignUp";
import ResetAccountPage from "../pages/ResetAccountPage";

export const publicRoutes = [
  {path: "/", element: MainPage},
  {path: "login/", element: LoginPage},
  {path: "logout/", element: LogoutPage},
  {path: "signup/", element: SignUpTemplate},
  {path: "reset-account/", element: ResetAccountPage},
  {path: "posts/", element: PostList},
]

export  const privateRoutes = [

]