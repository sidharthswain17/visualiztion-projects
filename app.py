# import streamlit as st
# import pandas as pd
# import plotly.express as px

# india_df=pd.read_csv(r"india.csv")
# list_of_states=india_df['State'].unique().tolist()
# list_of_states.insert(0,'Overal India')


# st.sidebar.title("India's DATA")
# selected_state=st.sidebar.selectbox('Select a state',list_of_states)
# primary=selected_state=st.sidebar.selectbox('Select primary parameter',list(india_df.columns[6:]))
# secondary=selected_state=st.sidebar.selectbox('Select secondary parameter',list(india_df.columns[6:]))

# plot=st.sidebar.button('PLOT')

# if plot:
#     if selected_state=='Overal India':
#         fig=px.scatter_mapbox(india_df,lat='Latitude',lon='Longitude',mapbox_style="carto-positron")
#         st.plotly_chart(fig,use_container_width=True)
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
india_df = pd.read_csv("india.csv")
st.set_page_config(layout='wide')
# Create list of states with 'Overall India'
list_of_states = india_df['State'].unique().tolist()
list_of_states.insert(0, 'Overall India')  # Fixed spelling

# Sidebar UI
st.sidebar.title("India's DATA")
selected_state = st.sidebar.selectbox('Select a state', list_of_states)

# Dropdowns for primary and secondary parameters
primary = st.sidebar.selectbox('Select primary parameter', list(india_df.columns[6:]))
secondary = st.sidebar.selectbox('Select secondary parameter', list(india_df.columns[6:]))

# Plot button
plot = st.sidebar.button('PLOT')

# If 'PLOT' button is clicked
if plot:
    if selected_state == 'Overall India':
       st.markdown("### 🎯 Map Interpretation Guide:")
       st.markdown("✅ **Size** represents **Primary Parameter** 📏")  
       st.markdown("🎨 **Color** represents **Secondary Parameter** 🌈")  
       fig = px.scatter_mapbox(india_df, lat="Latitude", lon="Longitude", size=primary, color=secondary,color_continuous_scale="Viridis", zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='District')
       st.plotly_chart(fig, use_container_width=True)

    else:
        st.markdown("### 🎯 Map Interpretation Guide:")
        st.markdown("✅ **Size** represents **Primary Parameter** 📏")  
        st.markdown("🎨 **Color** represents **Secondary Parameter** 🌈")  
        state_df=india_df.query(f"State=='{selected_state}'")  
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, color_continuous_scale="Viridis",zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True) 
