#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
from constraint import Problem, AllDifferentConstraint
from PIL import Image, ImageDraw

# Define the provinces and their positions
provinces = {
    "LaiChau": (0, 0), "DienBien": (1, 0), "SonLa": (2, 0), "HoaBinh": (3, 0),
    "HaNoi": (0, 1), "HaiPhong": (1, 1), "QuangNinh": (2, 1), "LangSon": (3, 1),
    "BacKan": (0, 2), "ThaiNguyen": (1, 2), "PhuTho": (2, 2), "YenBai": (3, 2),
    "LaoCai": (0, 3), "TuyenQuang": (1, 3), "HaGiang": (2, 3), "VinhPhuc": (3, 3),
}

# Define the size of each cell
cell_size = 100

# Define adjacency constraints
adjacencies = [
    ("LaiChau", "DienBien"), ("LaiChau", "SonLa"),
    ("DienBien", "SonLa"),
    ("SonLa", "HoaBinh"), ("SonLa", "LaiChau"), ("SonLa", "DienBien"),
    ("HoaBinh", "HaNoi"), ("HoaBinh", "SonLa"),
    ("HaNoi", "HoaBinh"), ("HaNoi", "HaiPhong"), ("HaNoi", "ThaiNguyen"),
    ("HaiPhong", "HaNoi"), ("HaiPhong", "QuangNinh"),
    ("QuangNinh", "HaiPhong"), ("QuangNinh", "LangSon"),
    ("LangSon", "QuangNinh"), ("LangSon", "BacKan"),
    ("BacKan", "LangSon"), ("BacKan", "ThaiNguyen"),
    ("ThaiNguyen", "BacKan"), ("ThaiNguyen", "HaNoi"),
    ("PhuTho", "ThaiNguyen"), ("PhuTho", "YenBai"),
    ("YenBai", "PhuTho"), ("YenBai", "LaoCai"),
    ("LaoCai", "YenBai"), ("LaoCai", "TuyenQuang"),
    ("TuyenQuang", "LaoCai"), ("TuyenQuang", "HaGiang"),
    ("HaGiang", "TuyenQuang"), ("HaGiang", "VinhPhuc"),
    ("VinhPhuc", "HaGiang"), ("VinhPhuc", "LangSon")
]

# Initialize the colors for the provinces
colors = {province: "white" for province in provinces.keys()}
color_options = ["white", "red", "green", "blue", "yellow"]

def draw_map(provinces, colors):
    # Create a blank image
    img = Image.new("RGB", (4 * cell_size, 4 * cell_size), "white")
    draw = ImageDraw.Draw(img)
    
    for province, (x, y) in provinces.items():
        color = colors[province]
        top_left = (x * cell_size, y * cell_size)
        bottom_right = ((x + 1) * cell_size, (y + 1) * cell_size)
        draw.rectangle([top_left, bottom_right], fill=color, outline="black")
        draw.text((x * cell_size + 10, y * cell_size + 10), province, fill="black")
    
    return img

def check_validity(colors, adjacencies):
    for province1, province2 in adjacencies:
        if colors[province1] != "white" and colors[province1] == colors[province2]:
            return False
    return True





# In[16]:


st.title("Map Coloring Game")

# User inputs for coloring provinces
for province in provinces.keys():
    colors[province] = st.selectbox(f"Select color for {province}", color_options, index=color_options.index(colors[province]))

# Draw the map with the selected colors
map_image = draw_map(provinces, colors)
st.image(map_image, caption="Color the map")

# Check if the current coloring is valid
if check_validity(colors, adjacencies):
    st.success("Great job! No adjacent provinces share the same color.")
else:
    st.error("Oops! Some adjacent provinces share the same color.")

if st.button("Reset Colors"):
    colors = {province: "white" for province in provinces.keys()}

# In[ ]:




