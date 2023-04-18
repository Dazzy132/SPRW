import React from 'react';
import {CircularProgress, Stack} from "@mui/material";

const Loader = () => {
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
};

export default Loader;