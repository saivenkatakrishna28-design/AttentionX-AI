import os
import tempfile
from pathlib import Path

import pandas as pd
import streamlit as st

from engine.config import settings
from engine.pipeline import run_pipeline
from engine.utils import ensure_dir

st.set_page_config(
    page_title="AttentionX AI",
    page_icon="🎬",
    layout="wide",
)

ensure_dir("outputs")

st.markdown(
    """
    <style>
    .main-title {font-size: 2.4rem; font-weight: 800; margin-bottom: 0.2rem;}
    .sub-title {font-size: 1.05rem; color: #666; margin-bottom: 1rem;}
    .metric-box {padding: 1rem; border-radius: 14px; background: rgba(120,120,120,0.08);}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">AttentionX AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Automated content repurposing engine for educators, mentors, and creators.</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Settings")
    max_highlights = st.slider("Max highlights", 1, 5, settings.max_highlights)
    clip_duration = st.slider("Clip duration (seconds)", 20, 60, settings.clip_duration)
    padding_before = st.slider("Padding before peak", 2, 15, settings.padding_before)
    padding_after = st.slider("Padding after peak", 5, 20, settings.padding_after)
    st.caption("Tip: Use a 3 to 20 minute video for the best demo.")

uploaded = st.file_uploader("Upload a long-form video", type=["mp4", "mov", "mkv", "avi", "webm"])

col1, col2, col3 = st.columns(3)
col1.metric("Max highlights", max_highlights)
col2.metric("Clip duration", f"{clip_duration}s")
col3.metric("Mode", "Demo-ready AI pipeline")

if uploaded:
    with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded.name).suffix) as tmp:
        tmp.write(uploaded.read())
        input_video = tmp.name

    st.video(input_video)

    if st.button("Generate Shorts", type="primary"):
        with st.spinner("Processing video and generating highlights..."):
            result = run_pipeline(
                video_path=input_video,
                output_dir="outputs",
                max_highlights=max_highlights,
                clip_duration=clip_duration,
                padding_before=padding_before,
                padding_after=padding_after,
            )

        st.success("Processing complete")

        highlights = pd.DataFrame(result["highlights"])
        if not highlights.empty:
            st.subheader("Top Highlights")
            st.dataframe(highlights, use_container_width=True)

        st.subheader("Generated Assets")
        for path in result["generated_files"]:
            p = Path(path)
            with open(p, "rb") as f:
                st.download_button(
                    label=f"Download {p.name}",
                    data=f,
                    file_name=p.name,
                    mime="application/octet-stream",
                )

        st.subheader("Hook Suggestions")
        for item in result["hooks"]:
            st.markdown(f"- **{item['title']}**")

        st.subheader("Notes")
        st.info(
            "If FFmpeg or some heavy dependencies are missing on your system, the transcript "
            "and ranking parts will still demonstrate the workflow for the hackathon demo."
        )
else:
    st.info("Upload a video to generate AI-picked shorts.")
