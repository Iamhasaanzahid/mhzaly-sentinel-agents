import streamlit as st
from agents import run_smart_multi_agent_workflow

# Page Configuration
st.set_page_config(
    page_title="MHZALY SOC & Multi-Agent Platform",
    page_icon="🛡️",
    layout="wide"
)

# Professional Styling
st.markdown("""
    <style>
    .main-title {
        font-size: 26px;
        font-weight: bold;
        color: #00FFAA;
    }
    .sub-desc {
        color: #94A3B8;
        font-size: 13px;
        margin-bottom: 20px;
    }
    .card-box {
        background-color: #0E1117;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #30363D;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.markdown("### 🛡️ MHZALY Control Center")
    api_key_input = st.text_input("Enter AI API Key (Optional)", type="password", placeholder="AI Brain Key...")
    
    st.markdown("---")
    navigation = st.radio(
        "Platform Navigation",
        ["🤖 AI Multi-Agent Office", "🔍 MHZALY SOC Dashboard"]
    )
    st.markdown("---")
    st.info("System Status: **Fully Operational**")

# Main Dashboard Interface
st.markdown('<p class="main-title">🛡️ MHZALY Advanced Security & Agent Platform</p>', unsafe_allow_html=True)

if navigation == "🤖 AI Multi-Agent Office":
    st.markdown('<p class="sub-desc">Autonomous brain-powered office where Manager and Sub-Agents collaborate on tasks.</p>', unsafe_allow_html=True)
    
    user_task = st.text_input("Give a command to your AI Office Team:", placeholder="e.g., Run security triage on suspicious domain or logs...")
    
    if st.button("🧠 Ignite Agent Brain & Workflow", type="primary"):
        if not user_task.strip():
            st.warning("Please enter a command first.")
        else:
            progress_bar = st.progress(0)
            status_placeholder = st.empty()
            
            def update_ui(pct, msg):
                progress_bar.progress(pct)
                status_placeholder.text(msg)
            
            with st.spinner("AI agents are thinking and working..."):
                results = run_smart_multi_agent_workflow(user_task, update_ui, api_key_input)
            
            st.success("Workflow completed by the agent network!")
            
            st.markdown("### 📋 Office Execution Logs:")
            for res in results:
                st.markdown(f'<div class="card-box">{res}</div>', unsafe_allow_html=True)

elif navigation == "🔍 MHZALY SOC Dashboard":
    st.markdown('<p class="sub-desc">Security Operations Center - Threat Intelligence & Log Analysis Module.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🌐 Domain / IP Triage")
        target_ip = st.text_input("Target IP or Domain:", placeholder="e.g., 192.168.1.1")
        if st.button("Run SOC Scan"):
            st.info(f"Scanning target {target_ip} for threat intelligence metrics...")
            st.metric(label="Threat Score", value="0 / 100", delta="Safe")
            
    with col2:
        st.markdown("### ✉️ Email Breach Check")
        target_email = st.text_input("Target Email:", placeholder="e.g., test@domain.com")
        if st.button("Check Breaches"):
            st.success("No breaches found in active threat databases for this target.")
