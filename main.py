import streamlit as st
import requests

# --- Cấu hình trang ---
st.set_page_config(page_title="🌍 Country Flags", layout="wide")

st.title("🌍 World Flags Gallery")

# --- Tải dữ liệu từ REST Countries API ---
@st.cache_data
def load_country_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("❌ Không tải được dữ liệu quốc gia")
        return []

# --- Lấy dữ liệu ---
countries = load_country_data()

# --- Tìm kiếm ---
search = st.text_input("🔍 Tìm kiếm quốc gia...", "").lower()

# --- Hiển thị cờ các nước ---
cols = st.columns(3)
count = 0
for country in sorted(countries, key=lambda c: c["name"]["common"]):
    name = country["name"]["common"]
    iso = country["cca2"]
    flag_url = country["flags"]["png"]
    region = country.get("region", "Unknown")

    if search in name.lower():
        with cols[count % 3]:
            st.image(flag_url, width=150, caption=name)
            st.markdown(f"**ISO:** `{iso}`")
            st.markdown(f"**Region:** {region}")
        count += 1

if count == 0:
    st.info("Không tìm thấy quốc gia nào.")







