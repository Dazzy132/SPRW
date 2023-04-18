import * as React from 'react';
import {useState} from 'react';
import {CssVarsProvider, useColorScheme} from '@mui/joy/styles';
import GlobalStyles from '@mui/joy/GlobalStyles';
import CssBaseline from '@mui/joy/CssBaseline';
import Box from '@mui/joy/Box';
import Button from '@mui/joy/Button';
import FormControl from '@mui/joy/FormControl';
import FormLabel, {formLabelClasses} from '@mui/joy/FormLabel';
import IconButton from '@mui/joy/IconButton';
import Link from '@mui/joy/Link';
import Input from '@mui/joy/Input';
import Typography from '@mui/joy/Typography';
import DarkModeRoundedIcon from '@mui/icons-material/DarkModeRounded';
import LightModeRoundedIcon from '@mui/icons-material/LightModeRounded';
import customTheme from '../styles/login/theme';
import GoogleIcon from '../styles/login/GoogleIcon';
import axios from "axios";
import {baseUrl} from "../api/routes";
import {useNavigate} from "react-router-dom";


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


export default function JoySignInSideTemplate() {

  const [error, setError] = useState("")
  const history = useNavigate()

  function loginButton(event) {
    event.preventDefault()

    const formElements = event.currentTarget.elements;
    const data = {
      email: formElements.email.value,
      password: formElements.password.value,
    };
    // alert(JSON.stringify(data, null, 2));

    axios.post(`${baseUrl}/auth/login/`, data)
      .then(response => {
        localStorage.setItem("token", response.data["access_token"])
        history('/')
      })
      .catch(e => {
        const firstError = Object.values(e.response.data)[0][0];
        setError(firstError)
      })
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
                Добро пожаловать
              </Typography>
              <Typography level="body2" sx={{my: 1, mb: 3}} textAlign="center">
                Давайте начнем! Пожалуйста, введите свои данные.
              </Typography>
            </div>

            {error &&
              <Typography variant="body2" sx={{backgroundColor: 'rgba(248,43,43,0.57)', color: 'white', mb: 2, p: 1}} textAlign="center">
                {error}
              </Typography>
            }

            <form method="post" onSubmit={loginButton}>
              <FormControl required>
                <FormLabel>Почта</FormLabel>
                <Input placeholder="Введите свою почту" type="email"
                       name="email"/>
              </FormControl>
              <FormControl required>
                <FormLabel>Пароль</FormLabel>
                <Input placeholder="•••••••" type="password" name="password"/>
              </FormControl>
              <Box
                sx={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                }}
              >
                <Link fontSize="sm" href="#replace-with-a-link"
                      fontWeight="lg">
                  Зарегистрироваться
                </Link>
                <Link fontSize="sm" href="#replace-with-a-link"
                      fontWeight="lg">
                  Не помню пароль
                </Link>
              </Box>
              <Button type="submit" fullWidth>
                Войти
              </Button>
            </form>
            <Button
              variant="outlined"
              color="neutral"
              fullWidth
              startDecorator={<GoogleIcon/>}
            >
              Войти с помощью Google
            </Button>
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
}
