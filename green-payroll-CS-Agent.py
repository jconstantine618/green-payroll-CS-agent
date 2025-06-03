import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Green Payroll Chatbot Demo", layout="centered")

st.title("💬 Green Payroll AI Chatbot Demo")

st.markdown("""
Welcome to the Green Payroll AI demo. This page showcases two live voice chatbots powered by ElevenLabs:

- ✅ Virtual Customer Service Assistant
- 📞 Simulated Sales Prospect for pitch practice
""")

# First chatbot: Customer Service
st.header("👩‍💼 Virtual Customer Service Agent")
st.markdown("""
This chatbot helps users get support with HR, payroll, onboarding, and compliance questions.
""")

cs_widget = """
<div style="margin-top: 10px;">
    <elevenlabs-convai agent-id="agent_01jwscd0k4f78sy282bk6ya0rm"></elevenlabs-convai>
</div>
"""

components.html(cs_widget, height=300)

# Add subtle spacing between the widgets
st.markdown("---")

# Second chatbot: Sales Prospect Simulation
st.header("📞 Demo Sales Prospect Chatbot")
st.markdown("""
This voice AI simulates a busy decision-maker. You’ll need to pitch quickly and clearly — or they’ll end the call. Great for cold call practice and objection handling.
""")

sales_widget = """
<div style="margin-top: 10px;">
    <elevenlabs-convai agent-id="agent_01jwtqnwg7f8qtq0vg6yphp1jv"></elevenlabs-convai>
</div>

<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
"""

components.html(sales_widget, height=300)

# Footer
st.markdown("---")
st.subheader("💡 About This Demo")
st.write("""
This demo shows how Green Payroll leverages conversational AI for support and sales.  
Visit [greenpayroll.com](https://greenpayroll.com) to learn more.
""")
