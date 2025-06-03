import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Green Payroll Chatbot Demo", layout="centered")

st.title("💬 Green Payroll AI Chatbot Demo")

# Customer Service Chatbot Section
st.header("👩‍💼 Virtual Customer Service Agent")
st.markdown("""
Welcome to the Green Payroll Virtual CS Agent demo. This is an example of a ChatBot that could be added to your website.  
Use this tool to experience real-time conversation about our payroll solutions, HR automation, and compliance services.
Welcome to the **Green Payroll Virtual CS Agent** demo.  
This is an example of a chatbot that could be embedded on your website to support customers in real time.

Use it to:
- Answer common HR and payroll questions
- Assist with employee onboarding
- Offer automated compliance guidance
""")

# Display the ElevenLabs Convai widget using HTML injection
html_code = """
cs_widget = """
<div style="margin-top: 20px;">
    <elevenlabs-convai agent-id="agent_01jwscd0k4f78sy282bk6ya0rm"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
</div>
"""

# Inject raw HTML with increased height
components.html(html_code, height=600)
components.html(cs_widget, height=600)

st.markdown("---")

# Sales Prospect Chatbot Section
st.header("📞 Demo Sales Prospect Chatbot")
st.markdown("""
This is a **Sales Prospect Simulation Bot**.  
Call this AI agent and **practice your sales pitch** — they act as a **busy, skeptical decision-maker**.  
If you can't clearly articulate value quickly, they will tell you they’re not interested.

Great for:
- Roleplaying cold call scenarios  
- Testing your pitch under pressure  
- Practicing objection handling
""")

sales_widget = """
<div style="margin-top: 20px;">
    <elevenlabs-convai agent-id="agent_01jwtqnwg7f8qtq0vg6yphp1jv"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
</div>
"""

components.html(sales_widget, height=600)

st.markdown("---")
st.subheader("🤖 What's This Demo For?")
st.subheader("💡 About This Demo")
st.write("""
This demo showcases how Green Payroll integrates conversational AI to:
- Answer common HR and payroll questions.
- Assist with onboarding new employees.
- Provide automated compliance insights.
- Support real-time interaction with clients.Add commentMore actions
This demo showcases how Green Payroll and ElevenLabs voice AI can be integrated into real-world workflows — for both **customer support** and **sales training**.

To learn more, visit [greenpayroll.com](https://greenpayroll.com).
""")
