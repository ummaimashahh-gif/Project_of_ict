import streamlit as st

# --- Page Config & Styling ---
st.set_page_config(page_title="Mechanical Converter", layout="centered")

# --- Student Information (Header) ---
st.title("Mechanical Unit Converter & Material Density Checker")
st.subheader("Student Details")
st.markdown(f"""
**Name:** Umaima Gillani  
**Roll Number:** 25 ME 164
""")
st.divider()

# --- Sidebar Navigation ---
option = st.sidebar.selectbox("Select Function", ["Unit Converter", "Material Density Checker"])

if option == "Unit Converter":
    st.header("⚙️ Mechanical Unit Converter")
    
    category = st.selectbox("Select Category", ["Pressure", "Force", "Temperature"])
    
    col1, col2 = st.columns(2)
    
    if category == "Pressure":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["Pascal (Pa)", "Bar", "PSI"])
        with col2:
            # Conversion Logic
            conversions = {
                "Pascal (Pa)": 1,
                "Bar": 100000,
                "PSI": 6894.76
            }
            result = val * (conversions[unit_from] / 1.0) # Normalized to Pa
            st.metric("Result in Pascals (Pa)", f"{result:,.2f}")

    elif category == "Force":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["Newton (N)", "Kilonewton (kN)", "Pound-force (lbf)"])
        with col2:
            conversions = {"Newton (N)": 1, "Kilonewton (kN)": 1000, "Pound-force (lbf)": 4.44822}
            result = val * conversions[unit_from]
            st.metric("Result in Newtons (N)", f"{result:,.2f}")

    elif category == "Temperature":
        with col1:
            temp = st.number_input("Enter Celsius (°C)", value=0.0)
        with col2:
            st.metric("Fahrenheit (°F)", f"{(temp * 9/5) + 32:.2f}")
            st.metric("Kelvin (K)", f"{temp + 273.15:.2f}")

elif option == "Material Density Checker":
    st.header("🏗️ Material Density Checker")
    st.write("Find the density of common engineering materials.")
    
    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Titanium": 4506,
        "Cast Iron": 7200,
        "Concrete": 2400
    }
    
    selected_material = st.selectbox("Choose a Material", list(materials.keys()))
    density = materials[selected_material]
    
    st.info(f"The density of **{selected_material}** is approximately **{density} kg/m³**.")
    
    # Simple Mass Calculator
    st.write("---")
    st.subheader("Mass Calculator")
    volume = st.number_input("Enter Volume (m³)", value=1.0)
    mass = density * volume
    st.success(f"Estimated Mass: {mass:,.2f} kg")

st.sidebar.write("---")
st.sidebar.caption("Mechanical Engineering Tool v1.0")
