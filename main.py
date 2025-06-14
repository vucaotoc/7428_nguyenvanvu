import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

# Giao diện login
st.title("🔐 Đăng nhập để xem cờ quốc gia")

with st.form("login_form", clear_on_submit=False):
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    submit_btn = st.form_submit_button("Đăng nhập")

# Xử lý đăng nhập
if submit_btn:
    if username == "admin" and password == "1234":
        st.session_state["authenticated"] = True
        st.success("Đăng nhập thành công! 👉 Chuyển sang tab Flags")
    else:
        st.error("Tên đăng nhập hoặc mật khẩu không đúng.")

# Nếu đã đăng nhập, hiển thị thông báo
if st.session_state.get("authenticated", False):
    st.info("✅ Bạn đã đăng nhập. Chuyển sang menu **Flags** để xem cờ.")
