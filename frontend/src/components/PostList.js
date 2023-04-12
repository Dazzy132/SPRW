import React from 'react';
import useSWR from 'swr'
import {baseUrl} from "../api/routes";
import PostItem from "./PostItem";

const PostList = () => {
  const fetcher = (...args) => fetch(...args).then(res => res.json())
  const {data, error, isLoading} = useSWR(`${baseUrl}/posts/`, fetcher)

  if (error) return <h1>Произошла ошибка {error}</h1>
  if (isLoading) return <h1>Идёт загрузка...</h1>

  return (
    <div>
      {data.map(post =>
        <PostItem key={post.id} data={post} />
      )}
    </div>
  );
};

export default PostList;