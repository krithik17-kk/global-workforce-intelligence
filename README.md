📊 Global Workforce Intelligence: HR Analytics Dashboard with GenAI Insights
A real-time, interactive HR analytics system built using Streamlit, Plotly, and OpenAI GPT, designed to empower HR professionals and business leaders with data-driven insights into workforce demographics, employee churn, diversity, compensation trends, and more — all hosted on the cloud.

🔍 Project Summary
This project transforms raw HR data into actionable insights using modern data visualization and GenAI-powered natural language summaries. It enables seamless HR reporting, DEI tracking, and attrition pattern detection, optimized for decision-makers and HR leadership.

🚀 Features
1. Dashboard Overview
Executive summary of key workforce metrics

Filters for Region, Department, Gender, and Tenure

2. Interactive Data Visualizations
Workforce Demographics (Pie Charts, Bar Charts)

Compensation Distribution (Boxplots, Histograms)

Employee Churn Trends

DEI metrics and regional analysis

3. GenAI-Powered Insights (LLM)
Natural language summary generation using OpenAI GPT

Dynamic narrative generation based on filtered dataset

Simplifies storytelling for HR leaders

4. Cloud-Ready Architecture
Deployable on Streamlit Cloud, Render, or Azure App Service

Secrets managed securely via .streamlit/secrets.toml (excluded from Git)

🛠 Tech Stack
Layer	Tools Used
Frontend UI	Streamlit, Plotly
Backend Logic	Python, Pandas
LLM Integration	OpenAI GPT
Cloud Hosting	Streamlit Community Cloud
Secrets Mgmt	.streamlit/secrets.toml (OpenAI API Key, optional GCP creds)
Version Control	Git + GitHub

📁 Project Structure
csharp
Copy
Edit
global-workforce-intelligence/
│
├── hr_analytics_app.py          # Main Streamlit app
├── data/
│   └── workforce_data.csv       # Cleaned HR dataset
├── .streamlit/
│   └── config.toml              # Streamlit UI customization
│   └── secrets.toml (excluded)  # API Keys for LLMs
├── credentials.json (excluded)  # GCP keys (optional, excluded)
├── requirements.txt             # Python dependencies
└── README.md                    # Project overview
📷 Sample Screenshots
Dashboard View	GenAI Summary

(Add screenshots after deployment.)

🔑 Environment Variables
Add your secrets in .streamlit/secrets.toml:

toml
Copy
Edit
# .streamlit/secrets.toml
openai_api_key = "sk-..."
▶️ Getting Started
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/krithik17-kk/global-workforce-intelligence.git
cd global-workforce-intelligence
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add API Keys (OpenAI, etc.)
bash
Copy
Edit
# .streamlit/secrets.toml
openai_api_key = "your_openai_key"
4. Run the App Locally
bash
Copy
Edit
streamlit run hr_analytics_app.py
☁️ Deploy to Cloud
You can deploy it using:

Streamlit Cloud

Render

Azure App Service (if needed)

Make sure to add your secrets.toml via Streamlit Cloud's dashboard UI.

📈 Use Cases
HR Executives: Quick pulse of workforce stats

Recruitment Teams: DEI hiring and churn visualization

CHROs: Data-backed decision-making

People Analysts: Drill-down employee insights

Campus Projects: Resume-ready data + AI + cloud showcase

✨ Highlight Skills
Data Analytics & Visualization

GenAI & OpenAI API Integration

Streamlit App Development

Cloud Hosting & Secrets Management

Real-World HR Data Use Case

📢 Acknowledgements
OpenAI for GPT

Streamlit

Publicly available synthetic HR datasets
