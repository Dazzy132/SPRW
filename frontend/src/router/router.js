import MainPage from "../pages/MainPage";
import PostList from "../components/PostList";
import AuthPage from "../pages/AuthPage";

export const publicRoutes = [
  {path: "/", element: MainPage},
  {path: "auth/", element: AuthPage},
  {path: "posts/", element: PostList},
]

export  const privateRoutes = [

]