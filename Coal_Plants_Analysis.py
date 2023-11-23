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

button_col = st.columns([2, 8, 3])
with button_col[1]:
    if st.button("Analyse", type="primary", help="Click to analyze", key="analyse_button"):
        if result1 == "Financial Analysis" and result2 == 'All (2012-22)':
            # Chart 1: Coal Production
            st.subheader('**Coal Production**')
            st.write('During 2021-22 up to Dec.22 actual Raw Coal Production is 607.295 Million Tonnes against the Annual production Target of 911.00 MT')
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
            st.write('During 2021-22 up to Dec.22 actual Raw Coal dispatched is 637.241 MT against the Annual Target of 911.00 MT.')
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
        if result1 == "Raniganj Coalfield" and result2 == '2021-22':
            image1 = st.image('raniganj.png', use_column_width=True)
            st.write(
                """
                **Coal Mining Plant Name:** Raniganj Coalfield\n
                **Origin:** 1774\n
                **Open-pit/Underground:** Open-pit\n
                **Produce:** Bituminous coal/non-coking coal\n
                **GCV:** Moderate\n
                **Production Rate/day:** 136k tonnes/day\n
                **Production Rate/week:** 952,000 tonnes/week\n
                **Production Rate/month:** 4,080,000 tonnes/month\n
                **Production Rate/year:** 49,640,000 tonnes/year\n
                **Revenue (in million INR):** 248200 million\n
                **Maintenance Cost:** 58550 million INR/year\n
                **Area:** 443.50 km^2\n
                **Coal Reserves:** 49.17 billion tonnes\n
                **Annual Turnover:** ₹12,076.17 crore (US$1.5 billion)\n
                **Profit before:** ₹1,897.18 crore (US$240 million)\n
                **Operating Mines:** 98\n
                **Underground Mines:** 77\n
                **Open Pit:** 21\n
                **Major Problem:** Coal fire\n
                **Mined By:** 90% [ Eastern Coalfield Limited (ECL)] a subsidiary of Coal India Limited (CIL) and a small area is mined by Bharat Coking Coal Limited (BCCL)\n
                **Grade Type:** G3\n
                **Size:** 250\n
                **Fixed Carbon:** 78\n
                **Ash Content:** 8\n
                **Depth:** 325\n
                **Deposits:** Specially for export market\n
                **Government/Private:** Private
                """
            )
    
