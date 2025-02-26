# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")


# Get the current credentials
session = get_active_session()
my_dataframe = session.table("zenas_athleisure_db.products.catalog_for_website").select(col('color_or_style')).collect()

style_selected = st.selectbox('Pick a sweatsuit color or style:',my_dataframe)

if style_selected:
    #st.write(style_selected)
    selected_dataframe = session.table("zenas_athleisure_db.products.catalog_for_website").filter(col('color_or_style')==style_selected).collect()
    #st.dataframe(data=selected_dataframe,use_container_width=True)

    if selected_dataframe:
        data = selected_dataframe[0]
        st.image(data['FILE_URL'], caption=f"Our warm, comfortable, {style_selected} sweatsuit!", width=400)
        st.markdown(f"**Price:** :green[{data['PRICE']}]")
        st.markdown(f"**Sizes Available**: {data['SIZE_LIST']}")
        st.markdown(f"**{data['UPSELL_PRODUCT_DESC']}**")

    