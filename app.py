import os
import json
import streamlit as st
from setup_graph import setup_graph
from retrieve import retrieve

UPLOAD_FOLDER = "uploaded_audios"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

st.title("📞 Topic Extraction from Contact Center Calls 🤝")

# File uploader for audio files
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

if uploaded_file is not None:
    audio_path = os.path.join(UPLOAD_FOLDER, "audio.mp3")
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.success(f"File {uploaded_file.name} saved successfully!")
    
    setup_graph("graph.yaml")
    # Show spinner while processing
    with st.spinner("Processing the audio file to extract topic..."):
        transcription, summary, topics_extracted = retrieve(audio_path)
    
    # Create tabs to display the results
    tab1, tab2, tab3 = st.tabs(["Transcripts", "Summary", "Topics Extracted"])

    with tab1:
        st.write("Transcribed Text:")
        st.write(str(transcription[0]['content'], 'utf-8'))

    with tab2:
        st.write("Summary:")
        st.write(str(summary[0]['content'], 'utf-8'))

    with tab3:
        st.write("Extracted Topics:")
        for topic in list(json.loads(topics_extracted[0]['content'].decode("utf-8")).values()):
            st.write(str(topic))

    st.success("Processing completed!")
    os.remove(audio_path)