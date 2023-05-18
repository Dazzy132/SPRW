import PostList from "../components/PostList";
import {Container} from "@mui/material";
import Header from "../components/Header";
import AddPost from "../components/AddPost";

const MainPage = () => {
  document.title = "Главная страница"

  return (
    <>
      <Header />
      <Container maxWidth="sm">
      <AddPost />
        <PostList/>
      </Container>

    </>
  );
};

export default MainPage;