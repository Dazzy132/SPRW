import MainPage from "../pages/MainPage";
import AuthPage from "../pages/AuthPage";
import PostList from "../components/PostList";

export const publicRoutes = [
  {path: "/", element: MainPage},
  {path: "auth/", element: AuthPage},
  {path: "posts/", element: PostList},
]

export  const privateRoutes = [

]