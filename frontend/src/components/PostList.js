import * as React from 'react';
import Typography from '@mui/material/Typography';
import {baseUrl} from "../api/routes";
import useSWR from "swr";
import PostItem from "./PostItem";
import {CircularProgress, Stack} from "@mui/material";


export default function PostList() {

  const fetcher = (...args) => fetch(...args).then(res => res.json())
  const {data, error, isLoading, mutate} = useSWR(`${baseUrl}/posts/`, fetcher)

  if (isLoading) {
    return (
      <Stack
        sx={{
          color: 'brown.500',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100vh',
        }}
      >
        <CircularProgress color="inherit" sx={{margin: 'auto'}}/>
      </Stack>
    )
  }

  if (error) {
    return <h1>Произошла ошибка {error.message}</h1>
  }

  if (data.length < 1) {
    return <Typography align={"center"}>Постов нет</Typography>
  }

  return (
    <div>
      {data.length === 0
        ? <Typography align={"center"}>Постов нет</Typography>
        : data.map(post => <PostItem key={post.id} post={post}/>)
      }
    </div>

  );
}