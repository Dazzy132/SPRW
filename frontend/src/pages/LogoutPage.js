import React, {useContext, useEffect, useState} from 'react';
import axios from "axios";
import {baseUrl} from "../api/routes";
import AuthContext from "../context/AuthContext";
import UserContext from "../context/UserContext";
import {Navigate, useNavigate} from "react-router-dom";
import {CssVarsProvider, useColorScheme} from "@mui/joy/styles";
import customTheme from "../styles/login/theme";
import CssBaseline from "@mui/joy/CssBaseline";
import GlobalStyles from "@mui/joy/GlobalStyles";
import Box from "@mui/joy/Box";
import Typography from "@mui/joy/Typography";
import FormLabel, {formLabelClasses} from "@mui/joy/FormLabel";
import FormControl from "@mui/joy/FormControl";
import Input from "@mui/joy/Input";
import Link from "@mui/joy/Link";
import Button from "@mui/joy/Button";
import GoogleIcon from "../styles/login/GoogleIcon";
import IconButton from "@mui/joy/IconButton";
import DarkModeRoundedIcon from "@mui/icons-material/DarkModeRounded";
import LightModeRoundedIcon from "@mui/icons-material/LightModeRounded";
import getUser from "../api";
import Loader from "../components/Loader";


function ColorSchemeToggle({onClick, ...props}) {
  const {mode, setMode} = useColorScheme();
  const [mounted, setMounted] = React.useState(false);
  React.useEffect(() => {
    setMounted(true);
  }, []);
  if (!mounted) {
    return <IconButton size="sm" variant="plain" color="neutral" disabled/>;
  }
  return (
    <IconButton
      id="toggle-mode"
      size="sm"
      variant="plain"
      color="neutral"
      {...props}
      onClick={(event) => {
        if (mode === 'light') {
          setMode('dark');
        } else {
          setMode('light');
        }
        onClick?.(event);
      }}
    >
      {mode === 'light' ? <DarkModeRoundedIcon/> : <LightModeRoundedIcon/>}
    </IconButton>
  );
}


const LogoutPage = () => {
  const [error, setError] = useState("")
  const history = useNavigate()
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    getUser()
      .then(response => {
        if (response.status !== 200) {
          history('/')
        }
      })
      .catch(e => null)
      .finally(() => {
        setIsLoading(false)
      })
  }, [])

  function logoutButton(e) {
    e.preventDefault()
    const token = localStorage.getItem('token');

    axios.post(`${baseUrl}/auth/logout/`, null, {
      headers: {Authorization: `Bearer ${token}`}
    }).then(() => {
        localStorage.removeItem("token");
        history('/login/')
      }
    ).catch(e => setError(e.response.data.non_field_errors))
  }

  if (isLoading) {
    return <Loader/>
  }

  return (

    <CssVarsProvider
      defaultMode="dark"
      disableTransitionOnChange
      theme={customTheme}
    >
      <CssBaseline/>
      <GlobalStyles
        styles={{
          ':root': {
            '--Collapsed-breakpoint': '769px', // form will stretch when viewport is below `769px`
            '--Cover-width': '40vw', // must be `vw` only
            '--Form-maxWidth': '700px',
            '--Transition-duration': '0.4s', // set to `none` to disable transition
          },
        }}
      />
      <Box
        sx={(theme) => ({
          width:
            'clamp(100vw - var(--Cover-width), (var(--Collapsed-breakpoint) - 100vw) * 999, 100vw)',
          transition: 'width var(--Transition-duration)',
          transitionDelay: 'calc(var(--Transition-duration) + 0.1s)',
          position: 'relative',
          zIndex: 1,
          display: 'flex',
          justifyContent: 'center',
          backdropFilter: 'blur(4px)',
          margin: "auto",
          backgroundColor: 'rgba(255 255 255 / 0.6)',
          [theme.getColorSchemeSelector('dark')]: {
            backgroundColor: 'rgba(19 19 24 / 0.4)',
          },
        })}
      >
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            minHeight: '100dvh',
            width:
              'clamp(var(--Form-maxWidth), (var(--Collapsed-breakpoint) - 100vw) * 999, 100%)',
            maxWidth: '100%',
            px: 2,
          }}
        >
          <Box
            component="header"
            sx={{
              py: 3,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
            }}
          >
            <Typography fontWeight="lg">SPRW</Typography>
            <ColorSchemeToggle/>
          </Box>
          <Box
            component="main"
            sx={{
              my: 'auto',
              py: 2,
              pb: 5,
              display: 'flex',
              flexDirection: 'column',
              gap: 2,
              width: 400,
              maxWidth: '100%',
              mx: 'auto',
              borderRadius: 'sm',
              '& form': {
                display: 'flex',
                flexDirection: 'column',
                gap: 2,
              },
              [`& .${formLabelClasses.asterisk}`]: {
                visibility: 'hidden',
              },
            }}
          >
            <div>
              <Typography component="h2" fontSize="xl2" fontWeight="lg"
                          textAlign="center">
                Выход из аккаунта
              </Typography>
            </div>

            {error &&
              <Typography variant="body2" sx={{
                backgroundColor: 'rgba(248,43,43,0.57)',
                color: 'white',
                mb: 2,
                p: 1
              }} textAlign="center">
                {error}
              </Typography>
            }

            <form method="post" onSubmit={logoutButton}>

              <Box
                sx={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                }}
              >
              </Box>
              <Button type="submit" fullWidth>
                Выйти
              </Button>
            </form>

          </Box>
          <Box component="footer" sx={{py: 3}}>
            <Typography level="body3" textAlign="center">
              © SPRW {new Date().getFullYear()}
            </Typography>
          </Box>
        </Box>
      </Box>

    </CssVarsProvider>
  );

};

export default LogoutPage;