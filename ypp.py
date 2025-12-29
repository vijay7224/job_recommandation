import streamlit as st
import requests
import pandas as pd

# 🌐 Remotive API URL
API_URL = "https://remotive.com/api/remote-jobs"

# 🎨 Streamlit App UI setup
st.set_page_config(page_title="Job Search App", page_icon="💼", layout="wide")

st.title("Free Job Search App")
#st.write("Search remote or country-specific jobs using the Remotive Public API")

# 🧠 Job & Country Lists
job_titles = [
    "Data Scientist", "Machine Learning Engineer", "Artificial Intelligence Engineer",
    "Data Analyst", "Python Developer", "Full Stack Developer", "Backend Developer",
    "Frontend Developer", "Cloud Engineer", "DevOps Engineer", "Business Analyst",
    "Software Engineer", "Cyber Security Analyst", "Database Administrator",
    "Mobile App Developer"
]

countries = [
    "India", "United States", "United Kingdom", "Canada", "Australia", "Germany", "France",
    "Italy", "Spain", "Netherlands", "Brazil", "South Africa", "Singapore", "Japan", "China",
    "New Zealand", "Sweden", "Switzerland", "Ireland", "United Arab Emirates"
]

# 🎛️ User Input
job_title = st.selectbox("Select Job Title:", options=job_titles)
country_input = st.selectbox(" Select Country:", options=countries)
category = st.text_input("Optional: Enter Job Category (e.g. software-dev):", "")

# 🚀 Search Button
if st.button("Search Jobs"):
    with st.spinner("Fetching jobs... Please wait ⏳"):
        params = {}
        if job_title:
            params["search"] = job_title
        if category:
            params["category"] = category

        # Fetch API data
        response = requests.get(API_URL, params=params)
        data = response.json()

        if "jobs" in data and len(data["jobs"]) > 0:
            jobs = data["jobs"]

            # Filter jobs by country (if available)
            if country_input:
                jobs = [
                    j for j in jobs
                    if country_input.lower() in j["candidate_required_location"].lower()
                ]

            if len(jobs) == 0:
                st.warning("⚠️ No jobs found for your selection.")
            else:
                st.success(f"✅ Found {len(jobs)} jobs matching your search!")

                # 🧾 Display selected job fields
                for j in jobs[:10]:  # show top 10 results
                    st.markdown("---")
                    st.image(j.get("company_logo_url", "https://cdn-icons-png.flaticon.com/512/3135/3135768.png"), width=100)
                    st.subheader(j["title"])
                    st.write(f"**🏢 Company:** {j['company_name']}")
                    st.write(f"**💼 Category:** {j['category']}")
                    st.write(f"**🕒 Type:** {j['job_type']}")
                    st.write(f"**📅 Posted on:** {j['publication_date'][:10]}")
                    st.write(f"**🌍 Location:** {j['candidate_required_location']}")
                    st.write(f"**💰 Salary:** {j.get('salary', 'Not specified')}")
                    st.write(f"**🏷️ Tags:** {', '.join(j.get('tags', []))}")
                    st.markdown(f"[🔗 Apply Here]({j['url']})", unsafe_allow_html=True)

        else:
            st.warning("⚠️ No jobs found. Try a different keyword or category.")
