import pandas as pd
import plotly.express as px
import streamlit as st
import xlwings as xw
from PIL import Image, ImageSequence
import glob
import geocoder
import time
import os
import datetime

st.set_page_config(layout="wide")

# Get last 6 distress images
distress_images = sorted(glob.glob(
    r'data\frame*.jpg'))[-6:]

# Get last 4 weapon images
weapon_images = sorted(glob.glob(
    r'wep_img\wep_*.jpg'))[-4:]

# Get GIF frames
gif_frame_paths = sorted(
    [f for f in glob.glob(
        r'data\frame*.jpg')
     if int(os.path.basename(f).replace("frame", "").replace(".jpg", "")) % 20 == 0]
)

# Create GIF
gif_path = "data\output.gif"
if gif_frame_paths:
    frames = [Image.open(f) for f in gif_frame_paths]
    frames[0].save(gif_path, format="GIF", save_all=True, append_images=frames[1:], duration=200, loop=0)

header_left, header_mid, header_right = st.columns([3, 1, 1], gap='small')

with header_left:
    st.title(':yellow[Police Dashboard]')

filepath = r"data.xlsx"

col1, col2 = st.columns(2)

# Open Excel file without showing the application
app = xw.App(visible=False)
ws = app.books.open(filepath).sheets['sheet']

x = ws.range("A1").value
y = ws.range("B1").value

# Real-time location tracking
g = geocoder.ip('me')  # Get the current location using IP geolocation
lat, lng = g.latlng  # Get latitude and longitude

# Create a DataFrame with correct column names for st.map
location_data = pd.DataFrame({
    'LAT': [lat],
    'LON': [lng]
})

with col1:
    st.title(':red[current status:]')

    if x + y == 2:
        st.header(':red[Potential Threat Detected!]')
        st.subheader("Attention Needed")
        st.write("Distress Signal Detected in your Vicinity\n\n\n")
        st.divider()

        # Display 6 distress images when a threat is detected
        if distress_images:
            st.header(':red[Snapshots]')
            cols = st.columns(2)
            for i, img_path in enumerate(distress_images):
                with cols[i % 2]:
                    image = Image.open(img_path)
                    # Get file save time
                    timestamp = os.path.getmtime(img_path)
                    time_str = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                    st.image(image, width=200)
                    st.caption(f"Captured: {time_str}")

        # Display 4 weapon images if available
        if weapon_images:
            st.header(':red[Weapon]')
            cols = st.columns(2)
            for i, img_path in enumerate(weapon_images):
                with cols[i % 2]:
                    image = Image.open(img_path)
                    # Get file save time
                    timestamp = os.path.getmtime(img_path)
                    time_str = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                    st.image(image, width=200)
                    st.caption(f"Captured: {time_str}")

        # Display the generated GIF
        if os.path.exists(gif_path):
            st.header(":red[Playback]")
            st.image(gif_path)

    elif x + y == 1:
        st.header("New Alert Detected!!")
        st.divider()

    else:
        st.header(':yellow[No Attention Required]')

# Display map with the real-time location
st.header(':red[Location]')
st.map(location_data)

# Close workbook and quit Excel application
ws.book.close()
app.quit()






# import pandas as pd
# import plotly.express as px
# import streamlit as st
# import xlwings as xw
# from PIL import Image
# import glob
# import geocoder
# import time

# st.set_page_config(layout="wide")

# # Get last 6 distress images
# distress_images = sorted(glob.glob(
#     r'C:\distress_signal_using_cv-master\distress_signal_using_cv-master\distress_signal_using_cv1-main\data\frame*.jpg'))[-6:]

# # Get last 4 weapon images
# weapon_images = sorted(glob.glob(
#     r'C:\distress_signal_using_cv-master\distress_signal_using_cv-master\distress_signal_using_cv1-main\wep_img\wep_*.jpg'))[-4:]

# header_left, header_mid, header_right = st.columns([3, 1, 1], gap='small')

# with header_left:
#     st.title(':yellow[Police Dashboard]')

# filepath = r"C:\distress_signal_using_cv-master\distress_signal_using_cv-master\distress_signal_using_cv1-main\data.xlsx"

# col1, col2 = st.columns(2)

# # Open Excel file without showing the application
# app = xw.App(visible=False)
# ws = app.books.open(filepath).sheets['sheet']

# x = ws.range("A1").value
# y = ws.range("B1").value

# # Real-time location tracking
# g = geocoder.ip('me')  # Get the current location using IP geolocation
# lat, lng = g.latlng  # Get latitude and longitude

# # Create a DataFrame with correct column names for st.map
# location_data = pd.DataFrame({
#     'LAT': [lat],
#     'LON': [lng]
# })

# with col1:
#     st.title(':red[current status:]')

#     if x + y == 2:
#         st.header(':red[Potential Threat Detected!]')
#         st.subheader("Attention Needed")
#         st.write("Distress Signal Detected in your Vicinity\n\n\n")
#         st.divider()

#         # Display 6 distress images when a threat is detected
#         if distress_images:
#             st.header(':red[Snapshots]')
#             cols = st.columns(2)  # 2 columns to display the distress images horizontally
#             for i, img_path in enumerate(distress_images):
#                 with cols[i % 2]:  # Alternate between the two columns
#                     image = Image.open(img_path)
#                     st.image(image, width=200)

#         # Display 4 weapon images if available
#         if weapon_images:
#             st.header(':red[Weapon]')
#             cols = st.columns(2)  # 2 columns for weapon images horizontally
#             for i, img_path in enumerate(weapon_images):
#                 with cols[i % 2]:
#                     image = Image.open(img_path)
#                     st.image(image, width=200)

#     elif x + y == 1:
#         st.header("New Alert Detected!!")
#         st.divider()

#     else:
#         st.header(':yellow[No Attention Required]')

# # Display map with the real-time location
# st.map(location_data)

# # Close workbook and quit Excel application
# ws.book.close()
# app.quit()
