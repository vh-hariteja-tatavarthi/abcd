import streamlit as st

# --- Page Configuration ---
# Sets the title that appears in the browser tab
st.set_page_config(
    page_title="A Message for You",
    page_icon="❤️"
)

# --- Main Page Content ---

# 1. Display the text
st.title("I love you! ❤️")
st.header("Just wanted you to know.")

# 2. Display an image
# You can use an image from a URL
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Heart_coraz%C3%B3n.svg/1200px-Heart_coraz%C3%B3n.svg.png"

st.image(
    image_url, 
    caption="With all my heart", 
    width=300  # You can adjust the width as needed
)

# You can also use a local image file:
# Make sure 'my_image.jpg' is in the same folder as your script
# try:
#     st.image("my_image.jpg", caption="My local image", width=300)
# except FileNotFoundError:
#     st.error("Local image file not found. Make sure 'my_image.jpg' is in the right folder.")
