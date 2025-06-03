import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Green Payroll Chatbot Demo", layout="centered")

st.title("💬 Green Payroll AI Chatbot Demo")

st.markdown("""
Welcome to the Green Payroll AI demo. This page showcases two live voice chatbots powered by ElevenLabs:

- ✅ Virtual Customer Service Assistant  
- 📞 Simulated Sales Prospect for pitch practice
""")

# Render both widgets in a single HTML block
html_code = """
<div style="margin-bottom: 40px;">
  <h3>👩‍💼 Virtual Customer Service Agent</h3>
  <p>This chatbot helps users get support with HR, payroll, onboarding, and compliance questions.</p>
  <elevenlabs-convai agent-id="agent_01jwscd0k4f78sy282bk6ya0rm"></elevenlabs-convai>
</div>

<hr style="margin: 40px 0;">

<div>
  <h3>📞 Demo Sales Prospect Chatbot</h3>
  <p>This voice AI simulates a busy decision-maker. You’ll need to pitch quickly and clearly — or they’ll end the call.<br>
  Great for cold call practice and objection handling.</p>
  <elevenlabs-convai agent-id="agent_01jwtqnwg7f8qtq0vg6yphp1jv"></elevenlabs-convai>
</div>

<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
"""

components.html(html_code, height=700)

# Footer
st.markdown("---")
st.subheader("💡 About This Demo")
st.write("""
This demo shows how Green Payroll leverages conversational AI for both customer support and sales training.  
Visit [greenpayroll.com](https://greenpayroll.com) to learn more.
""")
