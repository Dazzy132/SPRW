import * as React from 'react';
import {useState} from 'react';
import Typography from '@mui/material/Typography';
import {baseUrl} from "../api/routes";
import useSWR from "swr";
import PostItem from "./PostItem";
import {CircularProgress, Container, Stack} from "@mui/material";
import {Modal} from "@mui/joy";
import Box from "@mui/joy/Box";


export default function PostList() {
  const [open, setOpen] = useState(false);
  const [selectedPost, setSelectedPost] = useState(null);
  const handleOpen = (post) => {
    setSelectedPost(post);
    setOpen(true);
  };

  const handleClose = () => {
    setSelectedPost(null);
    setOpen(false);
  };

  const modalStyle = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 600,
    border: "2px solid #000",
    boxShadow: 24,
    backgroundColor: 'rgba(0,0,0,0.94)',
    p: 4,
  };

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
    <Container>
      {data.length === 0
        ? <Typography align={"center"}>Постов нет</Typography>
        : data.map(post => <PostItem key={post.id} post={post}
                                     handleOpen={handleOpen}/>)
      }
      {selectedPost && (
        <Modal
          open={open}
          aria-labelledby="modal-modal-title"
          aria-describedby="modal-modal-description"
          onClose={handleClose}
          BackdropProps={{onClick: handleClose}}
        >
          <Box sx={modalStyle}>
            <Typography id="modal-modal-title" variant="h6" component="h2">
              {selectedPost.text}
            </Typography>
            <img src={selectedPost.image} width="400px" alt=""/>
          </Box>
        </Modal>
      )}
    </Container>

  );
}