# 打开网页，在cmd命令界面运行下面一段
# # streamlit run C:\Users\Tracy\Desktop\2024Winter\科研\01.20Python-oneleaf\一叶知秋.py [ARGUMENTS]

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px
import os
import time
import datetime
import base64
# import matplotlib.pyplot as plt
# os.chdir(r'C:\Users\Tracy\Desktop\2024Winter\科研\01.20Python-oneleaf') # 设定文件路径
# 设置页面配置
st.set_page_config(page_title="CX-copilot 1.0", page_icon="⭐", layout="wide")
# 通过 css样式隐藏主菜单和页脚
hide_menu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(hide_menu,unsafe_allow_html=True)
# st.balloons()

def main_bg(main_bg):
    main_bg_ext = "back.png"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
# 调用
main_bg('back.png')


with st.sidebar:
    # choose = option_menu("管理端", ["数据上传", "用户行为数据", "系统性能评估",
    #                                 "数据备份", "安全审计", "系统监控","AI启动项"],
    #                      icons=['cloud-upload', 'person lines fill', 'app-indicator', "boombox-fill",
    #                             'list-task', 'gear', 'bar-chart'],
    #                      menu_icon="list", default_index=0,
    #                      styles={
    #     "container": {"padding": "5!important", "background-color": "#dceef8"}, # 整体颜色
    #     "icon": {"color": "#0e427a", "font-size": "15px"}, # 图标颜色和大小设定
    #     "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#f1f1f2"}, # 图标旁文字大小和点击时颜色设定
    #     "nav-link-selected": {"background-color": "#4FC8DD"} # 点击后背景色
    # })
    choose = option_menu("管理端", ["用户行为数据", "系统性能评估",
                                "数据备份", "安全审计", "系统监控","AI启动项"],
                     icons=['person lines fill', 'app-indicator', "boombox-fill",
                            'list-task', 'gear', 'bar-chart'],
                     menu_icon="list", default_index=0,
                     styles={
    "container": {"padding": "5!important", "background-color": "#dceef8"}, # 整体颜色
    "icon": {"color": "#0e427a", "font-size": "15px"}, # 图标颜色和大小设定
    "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#f1f1f2"}, # 图标旁文字大小和点击时颜色设定
    "nav-link-selected": {"background-color": "#4FC8DD"} # 点击后背景色
})

## ==================================  数据监控与分析  ==========================================
# if choose == "数据上传":
#     ## file_uploader【文件上传】
#     uploaded_files = st.file_uploader("选择需上传的文件(包括试卷库、作业库、题库、PPT课件等)：", accept_multiple_files=True, type=["csv","xlsx","xls","ppt","docx","txt","mp4","mp3","pdf","png","jpg"])
#     for uploaded_file in uploaded_files:
#         df = pd.read_csv(uploaded_file,encoding='gbk')
#         st.write("文件名:", uploaded_file.name)
#         # latest_iteration1 = st.empty() ##  显示进度
#         # bar1 = st.progress(0)
#         # for i in range(100): # Update the progress bar with each iteration.
#         #     latest_iteration1.text(f'加载进度 {i + 1} %')
#         #     bar1.progress(i + 1)
#         #     time.sleep(0)
#         # st.success('数据导入成功！请检查并核对数据的完整性和真实性。')
#         with st.spinner('超星小助手正在努力加载中......'):
#             time.sleep(1)
#         st.dataframe(df)

if choose == "用户行为数据":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)
    selecte1 = option_menu(None, ["用户地区分布-条形图", "用户特征分布-饼图", "用户活跃度-折线图"],
                          icons=["bar-chart-fill", "pie-chart-fill", "graph-up"],
                          menu_icon="cast", default_index=0, orientation="horizontal",
                           styles={
                               "container": {"padding": "5!important", "background-color": "#dceef8"},  # 整体颜色
                               "icon": {"color": "#0e427a", "font-size": "15px"},  # 图标颜色和大小设定
                               "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#f1f1f2"},  # 图标旁文字大小和点击时颜色设定
                               "nav-link-selected": {"background-color": "#4FC8DD"}}
                           )
    if selecte1 == "用户地区分布-条形图":
        st.info('条形图直观地展示了用户在不同地区的分布情况，使得数据的对比一目了然。通过不同条形的长度，可以迅速识别出用户的主要聚集地和相对较少的地区，有助于企业制定针对性的市场策略。')
        col1, col2 = st.columns(2)
        with col1:
            st.image("用户分布地区.png",width=400)
        with col2:
            data = {"lat": [30.287459, 23.1301964, 37.082680, 32.385044, 32.041544,35.287459, 29.1301964, 29.082680, 28.385044, 38.041544,26.082680, 34.385044,
                            28.98027, 30.383508, 28.082638, 29.645862, 27.709894, 28.209069, 30.172116, 29.436911, 28.853205, 29.200223,
                            24.242989, 21.732496, 23.577451, 20.576244, 23.543893
                            ],
                     "lon": [120.153576, 113.2592945, 119.270721, 116.486671, 118.767413,108.287459, 106.1301964, 103.082680, 113.385044, 114.041544,106.082680, 113.385044,
                             120.242931,119.180264, 118.12986, 120.221176, 121.10337, 118.497655, 118.075477, 119.433523, 118.300163, 121.425484,
                             112.846329, 115.229495, 111.499595, 112.049019, 116.166661],
                     "City": ["Zhejiang", "Guangdong", "Shanxi", "Anhui", "Jiangsu","Shanxi", "Chongqin", "Sichuan", "Hunan", "Hebei","Guizhou", "Henan",
                              "Zhejiang","Zhejiang","Zhejiang","Zhejiang","Zhejiang","Zhejiang","Zhejiang","Zhejiang","Zhejiang","Zhejiang",
                              "Guangdong", "Guangdong", "Guangdong", "Guangdong", "Guangdong"]}
            df = pd.DataFrame(data)
            st.map(data=df)

    elif selecte1 == "用户特征分布-饼图":
        st.info('饼图以圆形为基础，通过划分不同的扇形区域来展示用户特征的分布情况。这种图表形式使得数据的占比关系非常清晰，便于快速了解各类用户特征的比例，为企业的用户分析和精准营销提供有力支持。')
        st.image("用户特征分布.png",width=900)

    elif selecte1 == "用户活跃度-折线图":
        st.info('折线图能够清晰地展示用户活跃度随时间的变化趋势，通过连线的起伏可以直观地看出活跃度的增减情况。这种图表形式有助于企业把握用户活跃度的变化规律，从而及时调整运营策略，提升用户留存和活跃度。')
        st.image("用户活跃度.png",width=600)


elif choose == "系统性能评估":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)
    selecte2 = option_menu(None, ["推荐效果评估","问答系统性能评估曲线"],icons=["pie-chart-fill","graph-up"],
                          menu_icon="cast", default_index=0, orientation="horizontal",
                           styles={
                               "container": {"padding": "5!important", "background-color": "#dceef8"},  # 整体颜色
                               "icon": {"color": "#0e427a", "font-size": "15px"},  # 图标颜色和大小设定
                               "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#f1f1f2"},  # 图标旁文字大小和点击时颜色设定
                               "nav-link-selected": {"background-color": "#4FC8DD"}}
                          )
    if selecte2 == "推荐效果评估":
        st.info('一个用于分析和展示系统推荐性能的核心功能，这有助于管理层精准掌握系统性能，为决策提供有力支持，推动系统持续优化发展')
        st.image("推荐效果评估.png",width=600)

    elif selecte2 == "问答系统性能评估曲线":
        st.info('智能问答系统性能检测：确保高效、准确的问答体验。让学习更便捷！')
        st.image("问答系统性能评估.png",width=500)


## ==================================  数据安全与运维保障服务  ==========================================
if choose == "数据备份":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)
    selecte3 = option_menu(None, ["配置选项", "高级选项", "更新备份数据"],icons=["bar-chart-fill", "pie-chart-fill", "graph-up"],
                          menu_icon="cast", default_index=0, orientation="horizontal",
                           styles={
                               "container": {"padding": "5!important", "background-color": "#dceef8"},  # 整体颜色
                               "icon": {"color": "#0e427a", "font-size": "15px"},  # 图标颜色和大小设定
                               "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#f1f1f2"},  # 图标旁文字大小和点击时颜色设定
                               "nav-link-selected": {"background-color": "#4FC8DD"}}
                          )
    if selecte3 == "配置选项":
        option2 = st.selectbox("数据源", ("数据库服务器", "文件服务器", "应用服务器"))
        option3 = st.selectbox("备份频率", ("每小时", "每日", "每周", "每月"))
        txt1 = st.text_area('请手动输入存储位置')
        txt2 = st.text_area('请手动输入备份任务名称')
        if st.button('确认'):
            st.subheader("**:blue[系统已更改配置！]**")
    elif selecte3 == "高级选项":
        option4 = st.selectbox("备份压缩", ("启用备份数据压缩","不启用"))
        option5 = st.selectbox("增量备份", ("启用增量备份","不启用"))
        option6 = st.selectbox("备份日志级别", ("详细",'标准',"简单"))
        txt3 = st.date_input("过期备份保留时间", datetime.date(2024, 4, 8))
    elif selecte3 == "更新备份数据":
        df = pd.DataFrame({'任务名称': ['任务1', '任务2', '任务3', '任务4'],
                           '数据源': ['数据库服务器', '文件服务器', '应用服务器', '数据库服务器'],
                           '备份频率': ['每小时', '每日', '每周', '每月'],
                           '备份状态': ['已完成', '进行中', '未开始', '已完成'],
                           '上次备份时间': ['2024-04-08 08:00', '2024-04-07 18:30', '-', '2024-03-30 22:00'],
                           '下次备份时间': ['2024-04-09 08:00', '2024-04-10 18:30', '2024-04-06 12:00', '2024-04-03 22:00']})
        df

if choose == "安全审计":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)
    selecte4 = option_menu(None, ["审计日志表","审计日志详细界面"],icons=["pie-chart-fill","graph-up"],
                          menu_icon="cast", default_index=0, orientation="horizontal",
                           styles={
                               "container": {"padding": "5!important", "background-color": "#dceef8"},  # 整体颜色
                               "icon": {"color": "#0e427a", "font-size": "15px"},  # 图标颜色和大小设定
                               "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#f1f1f2"},  # 图标旁文字大小和点击时颜色设定
                               "nav-link-selected": {"background-color": "#4FC8DD"}}
                          )
    if selecte4 == "审计日志表":
        st.info("审计日志表以直观、简洁的方式展示了审计数据的统计结果，用户可以迅速了解审计活动的整体情况，如用户的登录次数、登录时间等。这种图表形式有助于用户快速发现异常或风险点，为决策提供有力支持。")
        st.image("安全审计1.png",width=800)

    elif selecte4 == "审计日志详细界面":
        st.info("审计日志详细界面提供了审计事件的详细信息，包括事件发生的时间、操作人、操作内容等。这一界面设计使得用户可以深入了解每个审计事件的具体情况，为进一步的调查和分析提供了丰富的数据支持。")
        st.image("安全审计2.png",use_column_width=True)

if choose == "系统监控":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)
    selecte5 = option_menu(None, ["安全监控","服务监控","日志监控","性能监控"],icons=["pie-chart-fill","graph-up"],
                          menu_icon="cast", default_index=0, orientation="horizontal",
                           styles={
                               "container": {"padding": "5!important", "background-color": "#dceef8"},  # 整体颜色
                               "icon": {"color": "#0e427a", "font-size": "15px"},  # 图标颜色和大小设定
                               "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#f1f1f2"},  # 图标旁文字大小和点击时颜色设定
                               "nav-link-selected": {"background-color": "#4FC8DD"}}
                          )
    if selecte5 == "安全监控":
        st.info("安全监控是保障系统稳定运行的重要环节，通过实时监控网络流量、用户行为等，及时发现并阻止潜在的安全威胁。它能有效预防数据泄露、黑客攻击等风险，确保企业信息安全。")
        st.image("安全监控.png",use_column_width=True)
    elif selecte5 == "服务监控":
        st.info("服务监控是对企业关键业务服务进行持续追踪和管理的过程，确保服务的可用性、稳定性和性能。通过监控，企业可以迅速响应服务中断或性能下降等问题，保障用户体验和业务连续性。")
        st.image("服务监控.png",use_column_width=True)
    elif selecte5 == "日志监控":
        st.info("日志监控是对系统、应用等产生的日志信息进行收集、分析和管理的过程。通过监控日志，企业可以了解系统的运行状况、发现潜在问题，并为故障排查和性能优化提供有力支持。")
        st.image("日志监控.png",use_column_width=True)
    elif selecte5 == "性能监控":
        st.info("性能监控是对系统、应用等性能指标的持续测量和评估。它帮助企业了解系统的运行效率、资源使用情况等，为性能优化和容量规划提供依据。通过性能监控，企业可以确保系统在高负载下仍能保持稳定运行。")
        st.image("性能监控.png",use_column_width=True)


## ==================================  AI启动项  ==========================================
if choose == "AI启动项":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)
    genre = st.radio("请选择AI启动项类型？", ('创造力型', '平衡型', '保守型'))
    if genre == '创造力型':
        st.success('创造力型AI启动项强调创新和新颖性。这种启动项在构建实时推荐和智能问答系统时，注重生成独特且富有创意的内容。它可能通过深度学习和复杂的算法，从大量数据中挖掘出新颖的模式和关联，从而为用户提供与众不同的推荐或回答。这种启动项非常适合那些需要激发用户兴趣、提供个性化体验或推动创新的场景。')
        if st.button('确认'):
            st.subheader("**:blue[成功调整！系统已自动配置创造力模式]**")
    elif genre == '平衡型':
        st.info("平衡型AI启动项追求稳定性和可靠性的平衡。在构建实时推荐和智能问答系统时，它致力于在准确性和多样性之间找到最佳平衡点。这种启动项可能通过优化算法和模型，确保推荐和回答既符合用户需求，又具有足够的多样性，避免重复或过于单一的内容。平衡型AI启动项适用于那些需要稳定输出、满足广泛用户需求的场景。")
        if st.button('确认'):
            st.subheader("**:blue[成功调整！系统已自动配置平衡模式]**")
    elif genre == '保守型':
        st.warning("保守型AI启动项注重稳定性和风险控制。在构建实时推荐和智能问答系统时，它倾向于采用已经验证过的、成熟的技术和策略，以确保系统的稳定性和可靠性。这种启动项可能不太会尝试新的、未经验证的方法，而是更注重对现有功能的优化和完善。保守型AI启动项适用于那些对系统稳定性和安全性要求极高，或者对风险承受能力有限的场景。")
        if st.button('确认'):
            st.subheader("**:blue[成功调整！系统已自动配置保守模式]**")



