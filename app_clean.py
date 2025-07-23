import streamlit as st

st.set_page_config(
    page_title="Indian Employee Salary Prediction System",
    page_icon="🇮🇳",
    layout="wide"
)

# Indian themed styling
st.markdown('''
<style>
.main-header {
    font-size: 2.5rem;
    font-weight: bold;
    text-align: center;
    background: linear-gradient(90deg, #ff9933 0%, #ffffff 50%, #138808 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 2rem;
}
.prediction-box {
    background: linear-gradient(135deg, #ff9933 0%, #138808 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin: 2rem 0;
}
</style>
''', unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🇮🇳 Indian Employee Salary Prediction System</h1>', unsafe_allow_html=True)
st.markdown("### AI-powered salary classification for Indian job market")

def predict_salary(age, education, occupation, experience, hours, industry, city_tier):
    score = 0
    
    # Age scoring
    if 25 <= age <= 35: score += 20
    elif 35 < age <= 45: score += 25
    elif age > 45: score += 15
    else: score += 10
    
    # Education scoring
    education_scores = {
        "PhD/Doctorate": 35, "Master's Degree": 30, "Bachelor's Degree": 25,
        "Professional Certification": 22, "Diploma": 15, "12th Pass": 10, "10th Pass": 5
    }
    score += education_scores.get(education, 10)
    
    # Occupation scoring
    high_paying = ["Software Engineer/IT", "Management/Executive", "Healthcare Professional", "Banking/Finance"]
    if occupation in high_paying: score += 25
    else: score += 15
    
    # Experience scoring
    if experience >= 10: score += 25
    elif experience >= 5: score += 20
    elif experience >= 2: score += 15
    else: score += 5
    
    # Industry scoring
    top_industries = ["Information Technology", "Banking & Financial Services", "Consulting"]
    if industry in top_industries: score += 18
    else: score += 10
    
    # City tier scoring
    if "Tier 1" in city_tier: score += 15
    elif "Tier 2" in city_tier: score += 10
    else: score += 5
    
    confidence = min(max(score/120, 0.6), 0.95)
    return ">5 Lakhs" if score >= 70 else "≤5 Lakhs", confidence

# Main interface
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("👤 Personal Information")
    age = st.slider("Age", 18, 65, 28)
    gender = st.selectbox("Gender", ["Female", "Male"])
    
    # Improved relationship options as requested
    relationship = st.selectbox("Relationship Status", 
        ["Single", "Married", "Live-in Partner", "Prefer not to say"])
    
    # Major countries as requested
    country = st.selectbox("Native Country", [
        "India", "United States", "United Kingdom", "Canada", "Australia", 
        "Germany", "France", "Japan", "Singapore", "UAE", "Bangladesh", 
        "Pakistan", "Sri Lanka", "Nepal", "Other"
    ], index=0)
    
    st.subheader("💼 Professional Details")
    education = st.selectbox("Education Level", [
        "10th Pass", "12th Pass", "Diploma", "Bachelor's Degree", 
        "Master's Degree", "PhD/Doctorate", "Professional Certification"
    ], index=3)
    
    occupation = st.selectbox("Primary Occupation", [
        "Software Engineer/IT", "Management/Executive", "Sales Professional",
        "Teaching/Education", "Healthcare Professional", "Banking/Finance",
        "Manufacturing/Production", "Transportation/Logistics", 
        "Retail/Customer Service", "Other Services"
    ])
    
    # Custom profession input for "Other Services" as requested
    custom_profession = ""
    if occupation == "Other Services":
        st.markdown("**🔧 Please specify your profession:**")
        custom_profession = st.text_input("Enter your specific job role", 
            placeholder="e.g., Digital Marketing, Content Writing, Graphic Design")
        if custom_profession:
            st.success(f"✅ Recorded: {custom_profession}")

with col2:
    st.subheader("💰 Experience & Compensation")
    experience = st.slider("Years of Experience", 0, 40, 5)
    hours = st.slider("Hours per week", 20, 80, 45)
    
    industry = st.selectbox("Industry Sector", [
        "Information Technology", "Banking & Financial Services", 
        "Manufacturing", "Healthcare & Pharmaceuticals", "Education",
        "Government/Public Sector", "Retail & E-commerce", 
        "Consulting", "Telecommunications", "Other"
    ])
    
    city_tier = st.selectbox("City Tier", [
        "Tier 1 (Mumbai, Delhi, Bangalore, etc.)",
        "Tier 2 (Pune, Hyderabad, Chennai, etc.)",
        "Tier 3 (Smaller cities)",
        "Rural/Remote areas"
    ])
    
    st.subheader("🎯 Salary Prediction")
    
    if st.button("🚀 Predict My Salary", type="primary", use_container_width=True):
        result, confidence = predict_salary(age, education, occupation, experience, hours, industry, city_tier)
        
        if result == ">5 Lakhs":
            st.markdown(f'''
            <div class="prediction-box">
                <h2>💰 Higher Salary Range</h2>
                <h3>Predicted: ₹5+ Lakhs annually</h3>
                <p>Confidence: {confidence:.1%}</p>
                <p>🎉 Above average for Indian market!</p>
            </div>
            ''', unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown(f'''
            <div style="background: linear-gradient(135deg, #FF5722 0%, #FF9800 100%); 
                        color: white; padding: 2rem; border-radius: 15px; text-align: center;">
                <h2>📊 Standard Salary Range</h2>
                <h3>Predicted: ₹2-5 Lakhs annually</h3>
                <p>Confidence: {confidence:.1%}</p>
                <p>💪 Good foundation with growth potential!</p>
            </div>
            ''', unsafe_allow_html=True)

# Summary and tips
st.divider()
st.subheader("📊 Your Profile Summary")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Age", f"{age} years")
    st.metric("Education", education)
with col2:
    st.metric("Experience", f"{experience} years")
    st.metric("Work Hours", f"{hours}/week")
with col3:
    st.metric("Industry", industry.split()[0])
    st.metric("Location", city_tier.split()[0])

# Career tips
with st.expander("💡 Career Growth Tips"):
    st.markdown(f'''
    **Based on your profile ({age} years, {experience} years exp):**
    
    ✅ **Immediate Focus:**
    - Skill development in {industry.lower()}
    - Professional networking and certifications
    - Performance optimization in current role
    
    🚀 **Growth Strategy:**
    - Consider opportunities in Tier 1 cities (+30-40% salary)
    - Explore high-demand skills like AI/ML, Cloud, Data Science
    - Build leadership and communication skills
    
    💰 **Salary Enhancement:**
    - Job switching every 2-3 years (typical 30-50% increase)
    - Specialization in niche, high-demand areas
    - Consider startups for equity opportunities
    ''')

# Footer
st.markdown("---")
st.markdown('''
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🇮🇳 <strong>Indian Employee Salary Prediction System</strong></p>
    <p>Customized for Indian job market | Educational and guidance purposes</p>
</div>
''', unsafe_allow_html=True)
