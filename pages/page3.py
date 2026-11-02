import streamlit as st
##侧边栏
with st.sidebar:
    gender = st.radio("你的性别是什么？",
                      ["男性", "女性", "跨性别"],
                      index=None)

##单选按钮
gender = st.radio("你的性别是什么？",
                      ["男性", "女性", "跨性别"],
                      index=None)
if gender:
    st.write(f"你选择的性别是{gender}")

#单选框
st.divider()
contact=st.selectbox("你希望通过什么方式联系?",
             ["电话","邮件","微信","QQ","其他"])
st.write(f"好的，我们会通过{contact}联系您")

#多选框
st.divider()
fruits=st.multiselect("你喜欢的水果是什么？",
               ["苹果","香蕉","橙子","梨子","西瓜"])
for fruit in fruits:
    st.write(f"你选择的水果是{fruit}")

#滑块
st.divider()
height=st.slider("你的身高是多少厘米？",value=170,
          min_value=100,max_value=200,step=1)
st.write(f"你的身高是{height}厘米")

#文件上传器
st.divider()
uploaded_file=st.file_uploader("上传文件",type=["png","jpg","jpeg"])
if uploaded_file:
    st.write(f"你上传的文件是{uploaded_file.name}")
    st.write(f"文件内容如下：{uploaded_file.read()}")
