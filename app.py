import streamlit as st
import leafmap.foliumap as leafmap

def main():
    st.set_page_config(layout="wide")
    
    st.title("Leafmap Map App")
    
    # Create map object
    m = leafmap.Map()
    
    # Initial markers
    locations = {
        "Tokyo": [35.6895, 139.6917],
        "Osaka": [34.6937, 135.5023],
        "Sapporo": [43.0621, 141.3544]
    }
    
    for city, coords in locations.items():
        m.add_marker(coords, popup=city)
    
    # Display map
    m.to_streamlit()
    
    # User input to add markers
    st.sidebar.header("Add Marker")
    lat = st.sidebar.number_input("Latitude", value=35.0, format="%.6f")
    lon = st.sidebar.number_input("Longitude", value=139.0, format="%.6f")
    label = st.sidebar.text_input("Label", "New Location")
    
    if st.sidebar.button("Add Marker"):
        m.add_marker([lat, lon], popup=label)
        st.experimental_rerun()
    
if __name__ == "__main__":
    main()

