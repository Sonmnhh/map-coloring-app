#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
from constraint import Problem, AllDifferentConstraint

def solve_map_coloring():
    # List of 10 provinces in Northern Vietnam
    provinces = ["LaiChau", "DienBien", "SonLa", "HoaBinh", "HaNoi", "HaiPhong", 
                 "QuangNinh", "LangSon", "BacKan", "ThaiNguyen"]

    # Define the problem
    problem = Problem()

    # Add variables with their respective domains (colors)
    colors = ["Red", "Green", "Blue", "Yellow"]
    for province in provinces:
        problem.addVariable(province, colors)

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
        ("ThaiNguyen", "BacKan"), ("ThaiNguyen", "HaNoi")
    ]

    # Add constraints for adjacent regions
    for (province1, province2) in adjacencies:
        problem.addConstraint(AllDifferentConstraint(), [province1, province2])

    # Solve the problem
    solutions = problem.getSolutions()
    
    # Return the first solution for simplicity
    return solutions[0] if solutions else {}



# In[16]:


def main():
    st.title('Map Coloring Problem')
    
    solution = solve_map_coloring()
    
    if solution:
        st.write("Here is a solution to the map coloring problem:")
        for province, color in solution.items():
            st.write(f"{province}: {color}")
            st.markdown(f"<div style='background-color: {color}; padding: 5px; margin: 5px; border: 1px solid black;'>{province}</div>", unsafe_allow_html=True)
    else:
        st.write("No solution found.")

if __name__ == "__main__":
    main()


# In[ ]:




