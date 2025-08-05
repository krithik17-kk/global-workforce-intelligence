import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI
import io
from datetime import datetime

# Load data
df = pd.read_csv("employees.csv")

# ------------- Streamlit App Config -------------
st.set_page_config(page_title="HR Analytics Dashboard", layout="wide", initial_sidebar_state="expanded")

# ------------- Sidebar Filters ------------------
st.sidebar.title("🔍 Filter Employees")
selected_country = st.sidebar.selectbox("🌍 Select Country", sorted(df["country"].unique()))
selected_dept = st.sidebar.multiselect("🏢 Department", options=sorted(df["dept"].unique()), default=df["dept"].unique())
show_attrition = st.sidebar.checkbox("❌ Show Only Attrited", value=False)

# Filter data
filtered_df = df[(df["country"] == selected_country) & (df["dept"].isin(selected_dept))]
if show_attrition:
    filtered_df = filtered_df[filtered_df["attrition"] == "Yes"]

# ------------- Header --------------------------
st.title("📊 HR Analytics Dashboard")
st.markdown(f"#### 🌍 Country: **{selected_country}**")
st.markdown("Analyze key HR metrics: attrition, engagement, performance, absenteeism, and salary trends.")

# ------------- KPIs ----------------------------
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("👥 Total Employees", len(filtered_df))
kpi2.metric("💰 Avg Salary", f"${filtered_df['salary'].mean():,.0f}")
kpi3.metric("📊 Avg Engagement", f"{filtered_df['engagement'].mean():.2f}")
kpi4.metric("⚠️ Attrition Rate", f"{(filtered_df['attrition'].value_counts(normalize=True).get('Yes', 0)*100):.1f}%")

st.markdown("---")

# ------------- Tabs -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Overview", 
    "📉 Performance", 
    "📌 Engagement", 
    "🤖 GenAI HR Insights", 
    "💬 Ask HR GenAI"
])

# ------------ Tab 1: Overview -------------------
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        dept_counts = filtered_df["dept"].value_counts().reset_index()
        dept_counts.columns = ["Department", "Count"]
        fig1 = px.bar(dept_counts, x="Department", y="Count", color="Department", title="Employee Distribution by Department")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.pie(filtered_df, names="perf_score", title="Performance Score Distribution")
        st.plotly_chart(fig2, use_container_width=True)

# ------------ Tab 2: Performance ----------------
with tab2:
    col3, col4 = st.columns(2)
    with col3:
        fig3 = px.histogram(filtered_df, x="perf_score", color="attrition", barmode="group", title="Attrition by Performance Score")
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        fig4 = px.box(filtered_df, x="dept", y="salary", color="dept", title="Salary Distribution by Department")
        st.plotly_chart(fig4, use_container_width=True)

# ------------ Tab 3: Engagement -----------------
with tab3:
    fig5 = px.scatter(filtered_df, x="engagement", y="absenteeism_days", size="salary", color="dept", hover_name="name", title="Engagement vs Absenteeism")
    st.plotly_chart(fig5, use_container_width=True)

# ------------ Tab 4: GenAI Insights -------------
client = OpenAI(api_key=st.secrets["openai_api_key"])

def generate_genai_summary(filtered_df):
    prompt = f"""
    You are an HR data analyst. Here's the data:
    - Total Employees: {len(filtered_df)}
    - Attrition Rate: {filtered_df['attrition'].value_counts(normalize=True).get('Yes', 0)*100:.2f}%
    - Avg Engagement: {filtered_df['engagement'].mean():.2f}
    - Avg Performance: {filtered_df['perf_score'].mean():.2f}

    Give 3 key insights around attrition, engagement, and performance.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

with tab4:
    st.subheader("🤖 GenAI-Style Workforce Insights")
    if st.button("🔍 Generate with GPT-4"):
        with st.spinner("Thinking like a real HR GenAI..."):
            summary = generate_genai_summary(filtered_df)
            st.markdown(summary)

# ------------ Summary CSV Download -------------
def generate_summary_csv(filtered_df):
    top_attr_dept = filtered_df[filtered_df["attrition"] == "Yes"]["dept"].value_counts().idxmax()
    high_eng_dept = filtered_df.groupby("dept")["engagement"].mean().idxmax()
    top_perf = ", ".join(filtered_df[filtered_df["perf_score"] == filtered_df["perf_score"].max()]["name"].values)

    summary = {
        "Total Employees": [len(filtered_df)],
        "Average Salary": [filtered_df['salary'].mean()],
        "Attrition Rate (%)": [filtered_df['attrition'].value_counts(normalize=True).get('Yes', 0)*100],
        "Highest Attrition Dept": [top_attr_dept],
        "Most Engaged Dept": [high_eng_dept],
        "Top Performer(s)": [top_perf],
    }
    return pd.DataFrame(summary)

st.markdown("### 📥 Download or Share")
col_a, col_b = st.columns(2)

with col_a:
    csv = generate_summary_csv(filtered_df).to_csv(index=False).encode('utf-8')
    st.download_button("📄 Download Summary Report (CSV)", data=csv, file_name=f'HR_Report_{datetime.today().date()}.csv', mime='text/csv')

with col_b:
    if st.button("📧 Simulate Email to HR"):
        st.success("✅ Report has been *emailed* to HR (simulated). Check your mailbox!")

# ------------ Tab 5: HR GenAI Assistant ----------
with tab5:
    st.subheader("💬 HR GenAI Assistant")
    st.markdown("Ask questions like:\n- *What is the average salary in Sales?*\n- *Which department has highest attrition?*")

    user_question = st.text_input("📨 Ask your HR Question:", placeholder="e.g., Who are the top performers in R&D?")

    if user_question:
        try:
            q = user_question.lower()

            if "salary" in q:
                avg_salary = filtered_df["salary"].mean()
                st.success(f"💰 The average salary is **${avg_salary:,.0f}**.")

            elif "attrition" in q:
                top_attr_dept = filtered_df[filtered_df['attrition'] == "Yes"]["dept"].value_counts().idxmax()
                st.success(f"⚠️ Highest attrition is in **{top_attr_dept}** department.")

            elif "top performer" in q or "highest performance" in q:
                top_performers = filtered_df[filtered_df["perf_score"] == filtered_df["perf_score"].max()]
                st.success(f"🏆 Top performer(s): {', '.join(top_performers['name'].values)}")

            elif "engagement" in q:
                most_engaged = filtered_df.groupby("dept")["engagement"].mean().idxmax()
                st.success(f"🔥 Most engaged department is **{most_engaged}**.")

            else:
                st.info("🤖 I'm still learning. Please ask about salary, performance, attrition, or engagement.")

        except Exception as e:
            st.error(f"GenAI could not process the query. ({e})")

# ------------ Footer ----------------------------
st.markdown("---")
st.markdown("© 2025 | Global Workforce Intelligence | Built with ❤️ using Streamlit + Plotly")
