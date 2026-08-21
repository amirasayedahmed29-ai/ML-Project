import streamlit as st
import requests

st.title("🏠 House Price Prediction App")
st.write("أدخل تفاصيل الشقة للحصول على السعر المتوقع:")

area_sqft = st.number_input("المساحة (قدم مربع):", min_value=100.0, value=1200.0, step=50.0)
bhk = st.number_input("عدد الغرف (BHK):", min_value=1, value=2, step=1)
bathroom_clean = st.number_input("عدد الحمامات:", min_value=1, value=2, step=1)
floor_clean = st.number_input("الطابق:", min_value=0, value=3, step=1)
furnishing_code = st.selectbox("حالة الفرش (0: غير مفروش, 1: نصف مفروش, 2: مفروش بالكامل):", [0, 1, 2])
is_top_location = st.selectbox("هل الموقع مميز؟ (0: لا, 1: نعم):", [0, 1])

if st.button("توقع السعر 💰"):
    payload = {
        "area_sqft": area_sqft,
        "bhk": bhk,
        "bathroom_clean": bathroom_clean,
        "floor_clean": floor_clean,
        "furnishing_code": furnishing_code,
        "is_top_location": is_top_location
    }
    
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"السعر المتوقع: {result['predicted_price']:,}")
        else:
            st.error("حدث خطأ أثناء التواصل مع السيرفر!")
    except Exception as e:
        st.error("تأكد من أن سيرفر FastAPI (main.py) شغال في الخلفية!")