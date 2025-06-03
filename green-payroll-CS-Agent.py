import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Green Payroll Chatbot Demo", layout="wide")

st.title("💬 Green Payroll AI Chatbot Demo")

st.markdown("""
Experience how Green Payroll uses AI voice bots for:
- ✅ Customer support automation  
- 📞 Sales training and cold call simulation
""")

# Define the layout
html_code = """
<style>
@media (min-width: 768px) {
  .chatbot-row {
    display: flex;
    gap: 30px;
  }
  .chatbot-column {
    flex: 1;
  }
}
@media (max-width: 767px) {
  .chatbot-row {
    display: block;
  }
  .chatbot-column {
    margin-bottom: 30px;
  }
}
.chatbot-container {
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 12px;
  box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
  height: 650px;
}
</style>

<div class="chatbot-row">

  <div class="chatbot-column">
    <div class="chatbot-container">
      <h3>👩‍💼 Virtual Customer Service Agent</h3>
      <p>This chatbot helps users get support with HR, payroll, onboarding, and compliance.</p>
      <elevenlabs-convai agent-id="agent_01jwscd0k4f78sy282bk6ya0rm"></elevenlabs-convai>
    </div>
  </div>

  <div class="chatbot-column">
    <div class="chatbot-container">
      <h3>📞 Demo Sales Prospect Chatbot</h3>
      <p>Pretend you're cold calling a decision-maker. They're busy and skeptical — can you earn their time?</p>
      <elevenlabs-convai agent-id="agent_01jwtqnwg7f8qtq0vg6yphp1jv"></elevenlabs-convai>
    </div>
  </div>

</div>

<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
"""

# Display both widgets with shared script
components.html(html_code, height=700)

# About section
st.markdown("---")
st.subheader("💡 About This Demo")
st.write("""
This demo shows how Green Payroll integrates ElevenLabs' conversational AI to support:
- Customers looking for real-time answers
- Salespeople improving objection handling and live pitch skills

Visit [greenpayroll.com](https://greenpayroll.com) to learn more.
""")
