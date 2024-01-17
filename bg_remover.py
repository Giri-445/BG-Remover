import streamlit as st
from rembg import remove
from PIL import Image
def removebg(img):
    input=Image.open(img)
    return remove(input)

def main():
    st.title("Background Remover App")
    up_file=st.file_uploader("Choose an image to remove the Backgrounnd",type=["jpg","jpeg","png"])
    if up_file is not None:
        st.image(up_file,caption="Uploaded Image")
        st.write("Removing...")
        result=removebg(up_file)
        st.image(result,caption="Final_Image")

if __name__=='__main__':
    main()
