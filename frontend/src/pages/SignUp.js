import * as React from 'react';
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
import {FormControlLabel} from "@mui/material";
import {Radio, RadioGroup} from "@mui/joy";


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


export default function SignUpTemplate() {

  function registrationButton(event) {
    event.preventDefault()

    const formElements = event.currentTarget.elements
    console.log(formElements)
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

            {/*{error &&*/}
            {/*  <Typography variant="body2" sx={{backgroundColor: 'rgba(248,43,43,0.57)', color: 'white', mb: 2, p: 1}} textAlign="center">*/}
            {/*    {error}*/}
            {/*  </Typography>*/}
            {/*}*/}

            <form method="post" onSubmit={registrationButton}>
              <FormControl required>
                <FormLabel>Логин</FormLabel>
                <Input placeholder="Введите свой логин" type="text"
                       name="username"/>
              </FormControl>

              <FormControl required>
                <FormLabel>Почта</FormLabel>
                <Input placeholder="Введите свою почту" type="email"
                       name="email"/>
              </FormControl>

              <FormControl required>
                <FormLabel>Имя</FormLabel>
                <Input placeholder="Введите своё имя" type="text"
                       name="first_name"/>
              </FormControl>

              <FormControl required>
                <FormLabel>Фамилия</FormLabel>
                <Input placeholder="Введите свою фамилию" type="text"
                       name="last_name"/>
              </FormControl>

              <FormControl required>
                <FormLabel id="demo-row-radio-buttons-group-label">Пол</FormLabel>
                <RadioGroup
                  aria-labelledby="demo-row-radio-buttons-group-label"
                  name="row-radio-buttons-group"
                  sx={{paddingLeft: "10px"}}
                >
                  <FormControlLabel value="male" control={<Radio />} label="Мужской" />
                  <FormControlLabel value="female" control={<Radio />} label="Женский" />
                </RadioGroup>
              </FormControl>

              <FormControl required>
                <FormLabel>Пароль</FormLabel>
                <Input placeholder="•••••••" type="password" name="password1"/>
              </FormControl>

               <FormControl required>
                <FormLabel>Подтвердите пароль</FormLabel>
                <Input placeholder="•••••••" type="password" name="password2"/>
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
                  У меня уже есть аккаунт
                </Link>

              </Box>
              <Button type="submit" fullWidth>
                Зарегистрироваться
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
