import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Green Payroll Chatbot Demo", layout="centered")

st.title("💬 Green Payroll AI Chatbot Demo")
st.markdown("""
Welcome to the Green Payroll Virtual CS Agent demo. This is an example of a ChatBot that could be added to your website.  
Use this tool to experience real-time conversation about our payroll solutions, HR automation, and compliance services.
""")

# Display the ElevenLabs Convai widget using HTML injection
html_code = """
<div style="margin-top: 20px;">
    <elevenlabs-convai agent-id="agent_01jwscd0k4f78sy282bk6ya0rm"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
</div>
"""

# Inject raw HTML with increased height
components.html(html_code, height=600)

st.markdown("---")
st.subheader("🤖 What's This Demo For?")
st.write("""
This demo showcases how Green Payroll integrates conversational AI to:
- Answer common HR and payroll questions.
- Assist with onboarding new employees.
- Provide automated compliance insights.
- Support real-time interaction with clients.

To learn more, visit [greenpayroll.com](https://greenpayroll.com).
""")
