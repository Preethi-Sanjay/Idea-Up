
import streamlit as st
from chains import build_chain

# Page configuration
st.set_page_config(
    page_title="Idea-Up ",
    page_icon="💡",
    layout="centered"
)

# Application heading
st.title("💡 Idea- Up ")
st.subheader("Turn real-world problems into startup ideas")

st.write(
    "Describe a problem you have noticed. "
    "Idea-Up will generate a startup idea, product features, "
    "and a practical MVP development plan."
)

# Create the chain once and reuse it
@st.cache_resource
def get_chain():
    return build_chain()


# User input
problem = st.text_area(
    "Describe the problem you want to solve",
    placeholder=(
        "Example: College students struggle to find "
        "teammates with complementary skills for hackathons."
    ),
    height=140
)

# Generate button
if st.button("🚀 Generate Startup Blueprint", type="primary"):

    if not problem.strip():
        st.warning("Please enter a problem first.")

    else:
        try:
            with st.spinner(
                "Generating your startup blueprint... "
                "This may take a little while."
            ):
                chain = get_chain()

                result = chain.invoke({
                    "problem": problem.strip()
                })

            
            st.success("Your startup blueprint is ready!")

            st.header("💡 1. Startup Idea")
            st.markdown(result["idea"])

            st.divider()

            st.header("⚙️ 2. Product Features")
            st.markdown(result["features"])

            st.divider()

            st.header("🚀 3. MVP Development Plan")
            st.markdown(result["mvp"])

            st.caption(
                "AI-generated suggestions. Validate your idea "
                "with potential users before investing in it."
            )

        except Exception as e:
            st.error(
                "Something went wrong. Check that Ollama "
                "is running and qwen3:4b is installed."
            )
            st.exception(e)
