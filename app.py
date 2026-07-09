import streamlit as pd_st
import asyncio
import os # <-- Tambahkan ini jika belum ada

# Trik Otomatisasi Instalasi Biner Playwright di Server Cloud
if not os.path.exists("/home/adminuser/.cache/ms-playwright"):
    os.system("playwright install chromium")
