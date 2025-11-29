import streamlit as st

# --- 1. Basic Setup and Title ---
st.set_page_config(page_title="ClauseEase AI Demo")
st.title("⚖️ ClauseEase AI Explainer Demo")
st.caption("Ask a legal question or paste a contract clause for simplification.")

# --- 2. Initialize Chat History ---
# We store the conversation history in Streamlit's session state.
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add an initial greeting from the AI
    st.session_state.messages.append({"role": "assistant", 
                                      "content": "Hello! I am ClauseEase AI. Upload a document or ask me to explain a legal concept."})

# --- 3. Display Chat History ---
# Loop through the messages and display them in the chat format
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 4. Handle New User Input ---
# This widget is at the bottom of the page
if prompt := st.chat_input("Ask ClauseEase a question..."):
    # 4a. Add user's message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 4b. Display the user's message immediately
    with st.chat_message("user"):
        st.markdown(prompt)

    # 4c. Generate AI Response (Dummy Logic)
    with st.chat_message("assistant"):
        
        # --- Dummy AI Logic for Demonstration ---
        if "contract" in prompt.lower() or "clause" in prompt.lower() or "agreement" in prompt.lower():
            # Mock response showing the simplification feature
            response = """
            **Simplified Explanation:**
            The phrase you provided means: "If any part of this agreement is found to be invalid, the rest of the agreement remains legally binding."
            
            This is a standard **severability clause**, designed to ensure the entire contract doesn't fail due to one faulty section.
            """
        elif "hello" in prompt.lower() or "hi" in prompt.lower():
            response = "Hello! I'm ready to simplify your legal documents. What do you need clarified?"
        else:
            # A default response
            response = f"I've received your query about '{prompt[:30]}...'. In a full version, I would now run our specialized legal NLP and LLM to provide you with a plain-language answer."
        # --- End Dummy AI Logic ---
        
        st.markdown(response)

        # 4d. Add AI's response to the chat history
        st.session_state.messages.append({"role": "assistant", "content": response})