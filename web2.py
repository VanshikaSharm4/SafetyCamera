import pandas as pd
import plotly.express as px
import streamlit as st
import xlwings as xw
from PIL import Image
import glob
st.set_page_config(layout="wide")
header_left, header_mid, header_right = st.columns([3,1,1],gap = 'small')

with header_left:
    st.title(':yellow[ Volunteer Dashboard]')


filepath = r"data.xlsx"




col1, col2 = st.columns(2)

ws = xw.Book(filepath).sheets['sheet']

x = ws.range("A1").value
y = ws.range("B1").value
with col1:
    st.title(':red[current status:]')

    if x + y == 2:
        st.header(':red[Potential Threat Detected!]')
        st.subheader("Attention Needed")
        st.write("Distress Signal Detected in your locality\n\n\n")
        st.divider()
        st.header("Location:")
        imagee = Image.open('static/img/location.png')
        st.image(imagee)

    elif x + y == 1:
        st.header("New Alert Detected!!")
        st.divider()
        st.header("Location:")
        imagee = Image.open('static/img/')
        st.image(imagee)

        st.divider()

    else:
        st.header(':yellow[No Attention Required]')

with col2:
    col3,col4=st.columns(2)

    if x + y > 0:
        st.header(':red[Snapshots]')
        snapshot_paths = sorted(glob.glob('data/frame*.jpg'))
        if snapshot_paths:
            cols = st.columns(3)
            for idx, path in enumerate(snapshot_paths):
                with cols[idx % 3]:
                    image = Image.open(path)
                    st.image(image, width=200)
        else:
            st.write('No snapshots available.')

    else:
        st.subheader("Snapshots \n from local surveillance cameras \n will be updated here in case of emergency")

# Add Volunteers Section
st.markdown('---')
st.markdown("""
<h2 style='text-align:center; color:#fff; font-family:Montserrat,Arial,sans-serif; font-size:2.7rem; font-weight:900; letter-spacing:1px; margin-bottom:0.5rem;'>Our Volunteers</h2>
""", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; margin-bottom:1.5rem;'>
  <p style='color:#fff; background:#232c53; border-radius:1.2rem; padding:1.2rem 1.5rem; font-size:1.15rem; font-family:Montserrat,Arial,sans-serif; box-shadow:0 2px 12px rgba(35,44,83,0.10); display:inline-block;'>
    <b>Verified volunteers</b> are trusted community members who receive real-time alerts during emergencies.<br>
    When an SOS is triggered by SafetyCam, they can respond quickly—reaching the location, assisting the victim, or alerting nearby authorities before the police arrive.<br>
    Their timely action can make a <span style='color:#ffd166;'>life-saving difference</span>.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; color:#ffd166; font-family:Montserrat,Arial,sans-serif; background:#232c53; border-radius:1.2rem 1.2rem 0 0; padding:0.7rem 0; margin-bottom:0;'>Volunteers in Area (Himachal Pradesh)</h2>", unsafe_allow_html=True)

volunteers = [
    {"name": "Vanshika Sharma", "desc": "First responder, medical aid specialist."},
    {"name": "Gaurav Thakur", "desc": "Community leader, coordinates local help."},
    {"name": "Aru Jain", "desc": "Tech-savvy, manages alert systems."},
    {"name": "Piyush Sharma", "desc": "Logistics and transport support."},
]

cols = st.columns(4)
for idx, v in enumerate(volunteers):
    with cols[idx]:
        st.markdown(f"<div style='background:#fff; border-radius:1.2rem; box-shadow:0 2px 12px rgba(35,44,83,0.13); padding:1.2rem 0.5rem 0.8rem 0.5rem; text-align:center; min-height:210px; margin-bottom:1.2rem;'>"
                    f"<div style='height:90px; width:90px; margin:0 auto 0.7rem auto; border-radius:50%; background:#f6f6f6; display:flex; align-items:center; justify-content:center; font-size:2.2rem; color:#ffd166;'>"
                    f"<span style='opacity:0.3;'>Image</span>"
                    f"</div>"
                    f"<div style='font-weight:700; color:#232c53; font-size:1.1rem; font-family:Montserrat,Arial,sans-serif;'>{v['name']}</div>"
                    f"<div style='color:#444; font-size:0.98rem; margin-top:0.4rem; font-family:Montserrat,Arial,sans-serif;'>{v['desc']}</div>"
                    f"</div>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; margin-top:1.5rem;'>
  <a href="#" style='display:inline-block; background:#ffd166; color:#232c53; font-weight:900; font-size:1.3rem; padding:1.1rem 2.8rem; border-radius:2.5rem; text-decoration:none; box-shadow:0 2px 12px rgba(35,44,83,0.10); font-family:Montserrat,Arial,sans-serif; letter-spacing:1px;'>
    <span style='vertical-align:middle;'>Be a Volunteer</span>
  </a>
</div>
""", unsafe_allow_html=True)