import streamlit as st
import pandas as pd
import altair as alt

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
    </style>
    """,
    unsafe_allow_html=True
)

# Set title
st.subheader("Coal Mine Analysis")

# Create two columns for select boxes
col1, col2 = st.columns(2)

Mine_list = [
    "Financial Analysis", 'Rajmahal Coal Mines', 'Raniganj Coalfield', 'Korba Coalfield', 
    'Talcher Coalfield', 'Singareni Collieries', 'Neyveli Lignite Corporation', 
    'Wardha Valley Coalfield', 'Margherita Coalfield', 'Jaintia Hills', 'Sohagpur Coalfield'
]

year_list = [
    'All (2012-22)', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', 
    '2018-19', '2019-20', '2020-21', '2021-22'
]

# Dropdowns in separate columns
with col1:
    result1 = st.selectbox("**Select Mine Site**", Mine_list)

with col2:
    result2 = st.selectbox("**Select Financial Year**", year_list)

# Align the button in the middle
st.markdown("<div class='centered'> </div>", unsafe_allow_html=True)

button_col = st.columns([8, 8, 3])
with button_col[1]:
    if st.button("Analyse", type="primary", help="Click to analyze", key="analyse_button"):
        if result1 == "Financial Analysis" and result2 == 'All (2012-22)':
            # Chart 1: Coal Production
            st.subheader('**Coal Production**')
            st.write('During 2021-22 up to Dec.22 actual Raw Coal Production is 607.295 Million Tonnes against the
Annual production Target of 911.00 MT')
            source_production = pd.DataFrame({
                'Year': ['2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22'],
                'Glance': [556, 565, 609, 639, 657, 675, 732, 728, 730, 716]  # Assuming 'Glance' is quantitative
            })

            bar_chart_production = alt.Chart(source_production).mark_bar().encode(
                x='Year:O',  # Categorical variable on x-axis
                y='Glance:Q'  # Quantitative variable on y-axis
            ).properties(
                width=600,  # Set the width of the chart
                height=400  # Set the height of the chart
            )

            st.altair_chart(bar_chart_production, use_container_width=True)

            # Chart 2: Coal Dispatch
            st.subheader('**Coal Dispatch**')
            st.write('During 2021-22 up to Dec.22 actual Raw Coal dispatched is 637.241 MT against the Annual Target of 911.00
MT.')
            source_dispatch = pd.DataFrame({
                'Year': ['2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22'],
                'Dispatch': [567, 572, 603, 632, 645, 690, 732, 707, 690, 819]  # Assuming 'Glance' is quantitative
            })

            bar_chart_dispatch = alt.Chart(source_dispatch).mark_bar().encode(
                x='Year:O',  # Categorical variable on x-axis
                y='Dispatch:Q'  # Quantitative variable on y-axis
            ).properties(
                width=600,  # Set the width of the chart
                height=400  # Set the height of the chart
            )

            st.altair_chart(bar_chart_dispatch, use_container_width=True)
