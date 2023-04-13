import PostList from "../components/PostList";
import {Container} from "@mui/material";

const MainPage = () => {
  document.title = "Главная страница"

  return (
    <Container maxWidth="sm">
      <PostList />
    </Container>
  );
};

export default MainPage;