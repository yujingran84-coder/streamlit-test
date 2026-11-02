import streamlit as st
import pandas as pd
st.title("我的个人网站💡")

"## 早上好！"

a=329*3
[11,22,33,44]

st.image("./下载.jfif",width=200)

df=pd.DataFrame({"学号":["01","02","03"],
            "成绩":[92,67,70],
            "班级":["二班","一班","三班"]})
st.dataframe(df)
st.divider()
st.table(df)