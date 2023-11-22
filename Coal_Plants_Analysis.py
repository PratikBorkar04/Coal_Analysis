import streamlit as st

# Define the path to your image
image_path = 'coal_mine1.png'

# Display the image using the st.image function
image = st.image(image_path, use_column_width=True)

# Adjust the image width and height using CSS injection
st.markdown(
    f"""
    <style>
        img {{
            width: 70vw; /* Adjust the percentage width as needed */
            height: 35vh; /* Adjust the percentage height as needed */
            object-fit: contain;
        }}
        .centered {{
            text-align: center;
            margin-top: 20px; /* Adjust the top margin as needed */
        }}
    </style>
    """
, unsafe_allow_html=True)

# Set title
st.subheader("Coal Mine Analysis")

# Create two columns for select boxes
col1, col2 = st.columns(2)

Mine_list = ['Rajmahal Coal Mines', 'Raniganj Coalfield', 'Korba Coalfield', 'Talcher Coalfield', 'Singareni Collieries', 'Neyveli Lignite Corporation', 'Wardha Valley Coalfield', 'Margherita Coalfield','Jaintia Hills','Sohagpur Coalfield']
year_list = ['2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18','2018-19','2019-20','2020-21','2021-22']

# Dropdowns in separate columns
with col1:
    result1 = st.selectbox("**Select Mine Site**", Mine_list)

with col2:
    result2 = st.selectbox("**Select Financial Year**", year_list)


# Align the button in the middle
st.markdown("<div class='centered'> </div>", unsafe_allow_html=True)
button_col = st.columns([8, 8, 3])
with button_col[1]:
    st.button("Analyse", type="primary", help="Click to analyze", key="analyse_button")
