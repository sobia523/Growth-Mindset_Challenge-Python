import streamlit as st

# Set the title of the app
st.set_page_config(page_title="growth mindset project")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Empower Your Growth Journey!")
st.write("Embrace challenges, learn from every setback, and unlock your fullest potential. This app empowers you to cultivate a growth mindset through insightful reflections, daily challenges, and rewarding achievements!")

st.header("Today's Growth Mindset Quote")
st.write("Your mindset determines your success — think big, grow bigger.")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe Your Challenge you're facing:")

if user_input:
    st.success(f"You're facing: {user_input} keep moving forward toward your goals.")
else:
    st.warning("Tell us about your challenge to get started!")


st.header("Reflect on Your Learning")
reflection = st.text_area("Write your outcome here:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences fosters growth. Share your challenges to learn and evolve!")


st.header("Celebrate Your Wins!")
acheivment = st.text_input("Share something you've recently accomplished:")

if acheivment:
    st.success(f"Amazing! You achieved: {acheivment}")
else:
    st.info("Big or small, every acheivement counts! Share one now.")


st.write("- - -")
st.write("In every challenge, there is a hidden opportunity to learn, grow, and become stronger than ever before.")