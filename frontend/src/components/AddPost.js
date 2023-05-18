import React, {useState} from 'react';
import Input from "@mui/joy/Input";
import IconButton from "@mui/joy/IconButton";
import {PhotoCamera} from "@mui/icons-material";
import axios from "axios";
import {baseUrl} from "../api/routes";


const AddPost = () => {
  const [text, setText] = useState("")
  const [image, setImage] = useState(null)

  const getBase64 = (file) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function () {
      setImage(reader.result)
    };
    reader.onerror = function (error) {
      console.log('Error: ', error);
    }
  }

  function addPost(e) {
    e.preventDefault()

    const token = localStorage.getItem("token")
    console.log(image)
    const data = {
      text, image
    }

    axios.post(`${baseUrl}/posts/`, data, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }).then(response => console.log(response))


  }

  return (
    <form style={{marginBottom: 10}} onSubmit={addPost}>
      <Input
        placeholder="Что у вас нового?"
        variant="plain"
        endDecorator={
          <IconButton
            color="default"
            aria-label="upload picture"
            component="label"
          >
            {image &&
              <div style={{
                backgroundImage: `url(${image})`,
                width: 25,
                height: 25,
                backgroundSize: "25px 25px",
              }}
              />}
            <input onChange={e => {
              const file = e.target.files[0]
              getBase64(file)
            }} name="image" hidden accept="image/*" type="file"/>
            <PhotoCamera fontSize="small"/>
          </IconButton>}
        value={text}
        onChange={e => setText(e.target.value)}
        name="text"
      >
      </Input>
    </form>
  );
};

export default AddPost;