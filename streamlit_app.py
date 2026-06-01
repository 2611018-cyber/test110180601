import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="홍길동의 포트폴리오",
    page_icon="👋",
    layout="centered"
)

# 2. 헤더 섹션 (이름 및 프로필 사진)
st.title("👋 안녕하세요, 홍길동입니다!")
st.subheader("성장을 추구하는 대화형 AI 개발자")

# 프로필 이미지와 환영 인사를 가로로 배치
col1, col2 = st.columns([1, 2])

with col1:
    # 본인의 사진 URL이나 로컬 이미지 경로를 넣으세요.
    # 샘플 이미지가 없으면 기본 아바타로 대체됩니다.
    st.image("https://via.placeholder.com/150", caption="홍길동", use_container_width=True)

with col2:
    st.write(
        """
        데이터와 코딩으로 세상의 문제를 해결하는 것에 흥미가 있습니다. 
        현재 파이썬과 스트림릿을 활용한 웹 대시보드 개발 및 AI 모델 서빙에 관심이 많습니다.
        
        * 📍 **위치:** 대한민국 서울
        * ✉️ **이메일:** email@example.com
        """
    )

st.markdown("---")

# 3. 보유 기술 (Skills)
st.header("🛠️ Tech Skills")

# 탭을 나누어 기술 스택 정리
tab1, tab2, tab3 = st.tabs(["Languages", "Frameworks", "Tools"])

with tab1:
    st.write("**Python**, **JavaScript**, **SQL**")
    st.progress(0.9, text="Python 숙련도 (90%)")
    st.progress(0.7, text="JavaScript 숙련도 (70%)")

with tab2:
    st.write("**Streamlit**, **FastAPI**, **React**")

with tab3:
    st.write("**Git/GitHub**, **Docker**, **AWS**")

st.markdown("---")

# 4. 프로젝트 경험 (Projects)
st.header("🚀 Projects")

# 프로젝트 1
with st.expander("1. 스트림릿 기반 데이터 시각화 대시보드 (2026)"):
    st.write("**설명:** 공공 데이터를 활용해 사용자가 쉽게 실시간 트렌드를 파악할 수 있는 대시보드 구축")
    st.write("**사용 기술:** Python, Streamlit, Pandas, Plotly")
    st.caption("[GitHub 링크 바로가기](https://github.com)")

# 프로젝트 2
with st.expander("2. AI 기반 챗봇 서비스 개발 (2025)"):
    st.write("**설명:** LLM API를 연동하여 사용자의 질문에 똑똑하게 답변하는 웹 서비스")
    st.write("**사용 기술:** Python, FastAPI, OpenAI API")
    st.caption("[GitHub 링크 바로가기](https://github.com)")

st.markdown("---")

# 5. 연락처 및 링크 (Contact)
st.header("📫 Contact")
st.write("저와 더 많은 이야기를 나누고 싶다면 아래 링크를 확인해주세요!")

# 가로로 버튼 배치
link_col1, link_col2, link_col3 = st.columns(3)
with link_col1:
    st.link_button("📂 GitHub", "https://github.com")
with link_col2:
    st.link_button("📝 Blog", "https://velog.io")
with link_col3:
    st.link_button("💼 LinkedIn", "https://linkedin.com")

# 푸터
st.caption("© 2026. Hong Gildong all rights reserved.")