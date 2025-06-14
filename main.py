import streamlit as st

# Cấu hình page
st.set_page_config(page_title="Login Page", layout="centered")

# CSS
st.markdown("""
    <style>
    .login-container {
        background-color: #f9f9f9;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
        width: 350px;
        margin: auto;
        margin-top: 100px;
        text-align: center;
    }
    .login-container h2 {
        margin-bottom: 20px;
        color: #333;
    }
    .login-container input[type="text"],
    .login-container input[type="password"] {
        width: 100%;
        padding: 10px;
        margin: 8px 0 16px;
        border: 1px solid #ccc;
        border-radius: 8px;
    }
    .login-container button {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        width: 100%;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-weight: bold;
    }
    .login-container button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# HTML + Streamlit input fields
st.markdown('<div class="login-container">', unsafe_allow_html=True)
st.markdown('<h2>🔐 Login</h2>', unsafe_allow_html=True)
st.markdown('<a href="#" >xin chào</a>', unsafe_allow_html=True)
st.markdown('<img src="https://api.vietqr.io/image/970416-LOCPHAT000329929-yyJhr6n.jpg?accountName=NGUYEN%20VAN%20VU&amount=65000&addInfo=123456" />', unsafe_allow_html=True)
# Inputs từ Streamlit
username = st.text_input("", placeholder="Username")
password = st.text_input("", type="password", placeholder="Password")
login = st.button("Login")

# Logic xác thực
if login:
    if username == "admin" and password == "1234":
        st.success("✅ Đăng nhập thành công!")
        st.balloons()
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Sai tên đăng nhập hoặc mật khẩu.")

st.markdown("</div>", unsafe_allow_html=True)
