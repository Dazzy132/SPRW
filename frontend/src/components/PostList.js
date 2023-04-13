import * as React from 'react';
import Typography from '@mui/material/Typography';
import {useEffect, useState} from "react";
import {baseUrl} from "../api/routes";
import useSWR from "swr";
import {useDispatch} from "react-redux";
import {loginSuccess} from "../store/reducers/auth/actions";
import PostItem from "./PostItem";

export default function PostList() {

  const fetcher = (...args) => fetch(...args).then(res => res.json())
  const {data, error, isLoading, mutate} = useSWR(`${baseUrl}/posts/`, fetcher)
  const dispatch = useDispatch()

  // TODO: Сделать глобально
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      dispatch(loginSuccess(token));
    }
  }, [dispatch]);


  if (isLoading) {
    return <h1>Идёт загрузка...</h1>
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
      : data.map(post => <PostItem post={post}/>)
      }
    </div>

  );
}