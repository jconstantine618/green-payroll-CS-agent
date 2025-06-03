import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Green Payroll Chatbot Demo", layout="wide")

st.title("💬 Green Payroll AI Chatbot Demo")

st.markdown("""
This demo shows how Green Payroll can use conversational AI for both **customer service** and **sales training**.  
Try both chatbots below:
""")

# Inject custom CSS and HTML for responsive layout
html_code = """
<style>
.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 20px;
}
.chatbox {
    flex: 1 1 48%;
    min-width: 300px;
    height: 600px;
    border: 1px solid #ccc;
    padding: 10px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.05);
    border-radius: 10px;
}
</style>

<div class="container">
  <div class="chatbox">
    <h3>👩‍💼 Virtual Customer Service Agent</h3>
    <p>This chatbot helps users get support with HR, payroll, onboarding, and compliance questions.</p>
    <elevenlabs-convai agent-id="agent_01jwscd0k4f78sy282bk6ya0rm"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
  </div>
  
  <div class="chatbox">
    <h3>📞 Demo Sales Prospect Chatbot</h3>
    <p>Pitch your services to this AI sales prospect. They act busy and skeptical — win them over or they’ll say no.</p>
    <elevenlabs-convai agent-id="agent_01jwtqnwg7f8qtq0vg6yphp1jv"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
  </div>
</div>
"""

components.html(html_code, height=700)

st.markdown("---")
st.subheader("💡 About This Demo")
st.write("""
This page demonstrates how Green Payroll can leverage voice AI for both **customer interaction** and **sales simulation** using ElevenLabs and chatbot technology.
""")
