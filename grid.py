import streamlit as st
import numpy as np

# Constants
GRID_SIZE = 40
BLOCK_SIZE = 20

# Initialize grid
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

def draw_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 1:
                st.markdown(f'<div style="width: {BLOCK_SIZE}px; height: {BLOCK_SIZE}px; background-color: black; display: inline-block;"></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="width: {BLOCK_SIZE}px; height: {BLOCK_SIZE}px; background-color: white; display: inline-block;"></div>', unsafe_allow_html=True)
        st.write("")

def save_grid():
    np.savetxt('grid_matrix.txt', grid, fmt='%d')
    st.success("Grid matrix saved successfully!")

def main():
    st.title("Grid Painter")

    st.write("Click on the grid cells to paint them black.")

    draw_grid()

    st.write("Click the button below to save the grid matrix.")

    if st.button("Save Grid Matrix"):
        save_grid()

if __name__ == "__main__":
    main()
