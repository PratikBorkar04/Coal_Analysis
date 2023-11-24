import streamlit as st
import pandas as pd
import altair as alt

# Define the path to your image
image_path = 'coal_mine.png'

# Display the image using the st.image function
image = st.image(image_path, use_column_width=True)

# Adjust the image width and height using CSS injection
st.markdown(
    f"""
    <style>
        img {{
            width: 80vw; /* Adjust the percentage width as needed */
            height: 45vh; /* Adjust the percentage height as needed */
            object-fit: contain;
        }}
        .stImage > img {{
            width: 100% !important;
            height: auto !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.subheader("India Coal Financial Analysis")

List1 = ["Production Rate", "Import Statistics", "Export Statistics","Production Rate + Import + Export"]

List2 = ["FY (2015-22)"]

col11, col12 = st.columns(2)

with col11:
    result11 = st.selectbox("**Select Insights**", List1)

with col12:
    result12 = st.selectbox("**Select Year**", List2)

button_col = st.columns([2, 8, 3])
with button_col[1]:
    if st.button("Discover", type="primary", help="Click to analyze", key="analyse") :
        if result11 == "Production Rate" and result12 == 'FY (2015-22)':
            st.subheader('**Production Rate**')
            source_dispatch1 = pd.DataFrame({
                'Year': ['2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22'],
                'Produce': [620, 645, 690, 732, 707, 690, 780]  # Assuming 'Glance' is quantitative
            })

            bar_chart_dispatch = alt.Chart(source_dispatch1).mark_bar(color='#FF6347').encode(
                x='Year:O',  # Categorical variable on x-axis
                y='Produce:Q'  # Quantitative variable on y-axis
            ).properties(
                width=600,  # Set the width of the chart
                height=400  # Set the height of the chart
            )

            st.altair_chart(bar_chart_dispatch, use_container_width=True)

        if result11 == "Import Statistics" and result12 == 'FY (2015-22)':
            st.subheader('**Import Statistics**')
            source_dispatch2 = pd.DataFrame({
                'Year': ['2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22'],
                'Import': [250, 210, 180, 190, 240, 260, 170]  # Assuming 'Glance' is quantitative
            })

            bar_chart_dispatch = alt.Chart(source_dispatch2).mark_bar(color='#1589C4').encode(
                x='Year:O',  # Categorical variable on x-axis
                y='Import:Q'  # Quantitative variable on y-axis
            ).properties(
                width=600,  # Set the width of the chart
                height=400  # Set the height of the chart
            )

            st.altair_chart(bar_chart_dispatch, use_container_width=True)
        
        if result11 == "Export Statistics" and result12 == 'FY (2015-22)':
            st.subheader('**Export Statistics**')
            source_dispatch3 = pd.DataFrame({
                'Year': ['2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22'],
                'Import': [260, 300, 280, 290, 140, 160, 370]  # Assuming 'Glance' is quantitative
            })

            bar_chart_dispatch = alt.Chart(source_dispatch3).mark_bar(color='#5CACEE').encode(
                x='Year:O',  # Categorical variable on x-axis
                y='Import:Q'  # Quantitative variable on y-axis
            ).properties(
                width=600,  # Set the width of the chart
                height=400  # Set the height of the chart
            )

            st.altair_chart(bar_chart_dispatch, use_container_width=True)

        if result11 == "Production Rate + Import + Export" and result12 == 'FY (2015-22)':
            source_dispatch1 = pd.DataFrame({
                'Year': ['2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22'],
                'Produce': [620, 645, 690, 732, 707, 690, 780]  # Assuming 'Glance' is quantitative
            })

            # Data for Export Statistics
            source_dispatch2 = pd.DataFrame({
                'Year': ['2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22'],
                'Export': [250, 210, 180, 190, 240, 260, 170]  # Assuming 'Glance' is quantitative
            })

            # Data for Import Statistics
            source_dispatch3 = pd.DataFrame({
                'Year': ['2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22'],
                'Import': [260, 300, 280, 290, 140, 160, 370]  # Assuming 'Glance' is quantitative
            })  

            # Concatenate the three dataframes
            combined_data = pd.concat([source_dispatch1, source_dispatch2, source_dispatch3], ignore_index=True)

            # Melt the dataframe to plot all three categories in the same graph
            melted_data = combined_data.melt(id_vars='Year', var_name='Category', value_name='Production + Import + Export')

            # Create the combined pivot graph
            pivot_chart = alt.Chart(melted_data).mark_bar().encode(
                x='Year:N',
                y='Production + Import + Export:Q',
                color='Category:N'
            ).properties(
                width=600,
                height=400
            )
            st.altair_chart(pivot_chart, use_container_width=True)


# Set title
st.subheader("Coal Mine Analysis")

# Create two columns for select boxes
col1, col2 = st.columns(2)

Mine_list = [
    "Mine Analysis", 'Raniganj Coalfield', 'Rajmahal Coal Mines', 'Korba Coalfield',
    'Talcher Coalfield', 'Singareni Collieries', 'Neyveli Lignite Corporation',
    'Wardha Valley Coalfield', 'Margherita Coalfield', 'Jaintia Hills', 'Sohagpur Coalfield'
]

year_list = [
    'All (2012-22)', '2021-22', '2020-21', '2019-20', '2018-19', '2017-18', '2016-17', '2015-16', '2014-15',
    '2013-14', '2012-13'
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
        if result1 == "Mine Analysis" and result2 == 'All (2012-22)':
            # Chart 1: Coal Production
            st.subheader('**Mine Coal Production Rate**')
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
            st.subheader('**Mine Coal Dispatch Rate**')
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
            st.subheader('Raniganj Coalfield')
            coal_info = {
    'Attribute': ['Coal Mining Plant Name', 'Origin', 'Open-pit/Underground', 'Produce', 'GCV',
                  'Area', 'Coal Reserves', 'Operating Mines', 'Underground Mines', 'Open Pit',
                  'Major Problem', 'Mined By', 'Grade Type', 'Size', 'Fixed Carbon',
                  'Ash Content', 'Depth', 'Deposits', 'Government/Private'],
    'Value': ['Raniganj Coalfield', '1774', 'Open-pit', 'Bituminous coal/non-coking coal', 'Moderate',
              '443.50 km^2', '49.17 billion tonnes', '98', '77', '21', 'Coal fire',
              '90% [Eastern Coalfield Limited (ECL)] a subsidiary of Coal India Limited (CIL) and a small area is mined by Bharat Coking Coal Limited (BCCL)',
              'G3', '250', '78', '8', '325', 'Specially for export market', 'Private']}

            # Creating a DataFrame from the coal information
            coal_df = pd.DataFrame(coal_info)

            # Displaying the information in table format
            st.write(
    f"""
    <div style="overflow-x:auto; max-height: 400px;">
        {coal_df.to_html(classes='data', header=True, index=False)}
    </div>
    """,
    unsafe_allow_html=True
)
            st.write("\n")
            st.write("\n")

            production_data = {
                'Production Type': ['Per Day', 'Per Week', 'Per Month', 'Per Year'],
                'Production Rate': [13600, 95200, 40800, 496400]
            }

# Creating a DataFrame from the dummy data
            production_df = pd.DataFrame(production_data)

            # Creating a bar chart using Altair
            bar_chart = alt.Chart(production_df).mark_bar().encode(
                x='Production Type',
                y='Production Rate',
                color=alt.value('Orange'),  # Setting a constant color for all bars
                tooltip=['Production Rate']
            ).properties(
                width=400,
                title='Production Rates'
)

            st.altair_chart(bar_chart)

            production_rate_info = {
    'Production Type': ['Production Rate/day', 'Production Rate/week', 'Production Rate/month', 'Production Rate/year'],
    'Production Rate': ['136k tonnes/day', '952,000 tonnes/week', '4,080,000 tonnes/month', '49,640,000 tonnes/year']}

            # Creating a DataFrame from the production rate information
            production_rate_df = pd.DataFrame(production_rate_info)

            # Displaying the information in table format
            st.table(production_rate_df.style.set_table_attributes("style='width:1200px;'"))
            
            financial_data = {
            'Category': ['Revenue', 'Maintenance Cost', 'Annual Turnover', 'Profit Before'],
            'Amount': [248200, 58550, 12076.17, 1897.18]
            }

            # Creating a DataFrame from the financial data
            financial_df = pd.DataFrame(financial_data)

            # Creating a bar chart using Altair
            bar_chart = alt.Chart(financial_df).mark_bar().encode(
            x='Category',
            y='Amount',
            color=alt.value('Purple'),  # Setting a constant color for all bars
            tooltip=['Amount']
            ).properties(
            width=400,
            title='Financial Overview'
            )

            st.altair_chart(bar_chart)
            financial_info = {
                'Attribute': ['Revenue (in million INR)', 'Maintenance Cost', 'Annual Turnover', 'Profit before'],
                'Value': ['248200 million', '58550 million INR/year', '₹12,076.17 crore (US1.5 billion)', '₹1,897.18 crore (US240 million)']
            }

            # Creating a DataFrame from the financial information
            financial_df = pd.DataFrame(financial_info)

            # Displaying the information in a table format
            st.table(financial_df.style.set_table_attributes("style='width:1200px;'"))
