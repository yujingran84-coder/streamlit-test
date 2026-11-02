import streamlit as st
##用户通过点击不同的选项卡来切换展示的内容
tab1,tab2,tab3=st.tabs(["性别","联系方式","喜好水果"])
with tab1:
    gender = st.radio("你的性别是什么？",
                      ["男性", "女性", "跨性别"],
                      index=None)
    if gender:
        st.write(f"你选择的性别是{gender}")
with tab2:
    contact = st.selectbox("你希望通过什么方式联系?",
                           ["电话", "邮件", "微信", "QQ", "其他"])
    st.write(f"好的，我们会通过{contact}联系您")

with tab3:
    fruits = st.multiselect("你喜欢的水果是什么？",
                            ["苹果", "香蕉", "橙子", "梨子", "西瓜"])
    for fruit in fruits:
        st.write(f"你选择的水果是{fruit}")
##折叠展开组件
with st.expander("身高信息"):
    height = st.slider("你的身高是多少厘米？", value=170,
                       min_value=100, max_value=200, step=1)
    st.write(f"你的身高是{height}厘米")

##侧边栏
with st.sidebar:
    gender = st.radio("你的性别是什么？",
                      ["男性", "女性", "跨性别"],
                      index=None)
# 多列布局
column1, column2, column3 = st.columns([1, 2, 1])

with column1:
    st.divider()
    contact = st.selectbox(
        "你希望通过什么方式联系？",
        ["电话", "邮件", "微信", "QQ", "其他"],
        key="contact_column1"
    )
    st.write(f"好的，我们会通过{contact}联系您")

with column2:
    st.divider()
    fruits = st.multiselect(
        "你喜欢的水果是什么？",
        ["苹果", "香蕉", "橙子", "梨子", "西瓜"],
        key="fruits_column2"
    )
    for fruit in fruits:
        st.write(f"你选择的水果是{fruit}")

with column3:
    st.divider()
    height = st.slider(
        "你的身高是多少厘米？",
        value=170,
        min_value=100,
        max_value=200,
        step=1,
        key="height_column3"
    )
    st.write(f"你的身高是{height}厘米")