import streamlit as st
import psutil
import time

st.title("Machine Resources App")

st.write("CPU")
cpu_chart = st.line_chart()
st.write("RAM")
ram_chart = st.line_chart()

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent

    cpu_chart.add_rows([cpu_percent])
    ram_chart.add_rows([ram_percent])

    time.sleep(1)
