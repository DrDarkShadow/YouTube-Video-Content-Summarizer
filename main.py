import streamlit as st
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from youtube_transcript_api import YouTubeTranscriptApi
import re
import requests
from dotenv import load_dotenv
import os

# Set page config (must be the first Streamlit command)
st.set_page_config(page_title="YouTube Video Content Summarizer", page_icon="🎥", layout="wide")

load_dotenv()

# --- Sidebar Options ---
with st.sidebar:
    st.header("Options")
    summary_length = st.selectbox("Summary Length", ["Short", "Medium", "Long"])
    answer_type = st.selectbox("Answer Type", ["Bullet Points", "Paragraph"])

# --- Helper function to extract YouTube video ID ---
def extract_video_id(url):
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11})',
        r'(?:embed\/)([0-9A-Za-z_-]{11})',
        r'(?:watch\?v=)([0-9A-Za-z_-]{11})',
        r'youtu\.be\/([0-9A-Za-z_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

# --- Get transcript from YouTube video ---
def get_video_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([line['text'] for line in transcript])
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# --- Get video info ---
def get_video_info(url):
    video_id = extract_video_id(url)
    if not video_id:
        st.error("Invalid YouTube URL")
        return None, None
    try:
        oembed_data = requests.get(
            f"https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v={video_id}&format=json"
        ).json()
        transcript = get_video_transcript(video_id)
        if not transcript:
            return None, "Could not get transcript"
        return {
            "title": oembed_data.get('title', 'Unknown Title'),
            "author": oembed_data.get('author_name', 'Unknown Author'),
            "url": f'https://www.youtube.com/watch?v={video_id}'
        }, transcript
    except Exception as e:
        st.error("Error Extracting Video")
        return None, str(e)

# --- Generate summary using OpenAI ---
def get_summary(prompt):
    try:
        chat = AzureChatOpenAI(
            azure_deployment="gpt-4o",
            api_version="2023-09-01-preview",
            openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            temperature=0,
        )
        messages = [
            SystemMessage(content='You are a helpful AI assistant that provides concise summaries of YouTube video transcripts.'),
            HumanMessage(content=prompt)
        ]
        response = chat.invoke(messages)
        return response.content
    except Exception as e:
        st.error(f"Error generating summary: {e}")
        return None

# --- Streamlit UI Setup ---
st.title("YouTube Video Content Summarizer")

# --- Initialize session state ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- URL Input ---
url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")

# --- Process Video on Button Click ---
if st.button("Generate Summary"):
    if url:
        with st.spinner("Getting video content ..."):
            info, transcript = get_video_info(url)
            if info and transcript:
                # Create a prompt that includes sidebar options
                prompt = f"""
                    Please summarize the following YouTube video transcript:
                    Title: {info['title']}
                    Author: {info['author']}
                    Transcript: {transcript}
                    Format: {answer_type}
                    Summary Length: {summary_length}
                """
                summary = get_summary(prompt)
                if summary:
                    st.success("Summary generated successfully!")
                    # Show summary and video info at the top
                    st.markdown(f"### Content Summary\n{summary}")
                    st.markdown(f"**Title:** {info['title']}  \n**Author:** {info['author']}  \n**URL:** [Open in YouTube]({info['url']})")
                    
                    # Create tabs for download options
                    tab1, tab2 = st.tabs(["Download Summary", "Download Transcript"])
                    with tab1:
                        st.download_button(
                            label="Download Summary",
                            data=summary,
                            file_name=f"{info['title']}_summary.txt",
                            mime="text/plain"
                        )
                    with tab2:
                        st.download_button(
                            label="Download Transcript",
                            data=transcript,
                            file_name=f"{info['title']}_transcript.txt",
                            mime="text/plain"
                        )
                    
                    # Save to session history
                    st.session_state.history.append({
                        'title': info['title'],
                        'url': url,
                        'summary': summary,
                        'author': info['author'],
                        'transcript': transcript
                    })
    else:
        st.warning("Please enter a valid YouTube URL")


# --- Footer ---
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 0.9em;'>Made with ❤️</p>
""", unsafe_allow_html=True)
