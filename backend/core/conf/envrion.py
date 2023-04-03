"""Для чтения .env file"""
import os.path

import environ

env = environ.Env(DEBUG=(bool, False))

if os.path.exists("core/.env"):
    environ.Env.read_env("core/.env")

# Что конкретно импортировать из файла
__all__ = [
    "env",
]