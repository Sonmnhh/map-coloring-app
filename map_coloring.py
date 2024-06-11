#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
from constraint import Problem, AllDifferentConstraint
from PIL import Image, ImageDraw

# Define the provinces and their positions
provinces = {
    "A1": (0, 0), "A2": (1, 0), "A3": (2, 0), "A4": (3, 0),
    "B1": (0, 1), "B2": (1, 1), "B3": (2, 1), "B4": (3, 1),
    "C1": (0, 2), "C2": (1, 2), "C3": (2, 2), "C4": (3, 2),
    "D1": (0, 3), "D2": (1, 3), "D3": (2, 3), "D4": (3, 3),
}

# Define the size of each cell
cell_size = 100

# Define adjacency constraints
adjacencies = [
    ("A1", "A2"), ("A2", "A3"), ("A3", "A4"),
    ("B1", "B2"), ("B2", "B3"), ("B3", "B4"),
    ("C1", "C2"), ("C2", "C3"), ("C3", "C4"),
    ("D1", "D2"), ("D2", "D3"), ("D3", "D4"),
    ("A1", "B1"), ("A2", "B2"), ("A3", "B3"), ("A4", "B4"),
    ("B1", "C1"), ("B2", "C2"), ("B3", "C3"), ("B4", "C4"),
    ("C1", "D1"), ("C2", "D2"), ("C3", "D3"), ("C4", "D4"),
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




