import React from 'react';
import PostList from "../components/PostList";

const MainPage = () => {
  document.title = "Главная страница"

  return (
    <PostList />
  );
};

export default MainPage;