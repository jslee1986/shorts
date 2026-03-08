import os
import requests
import json
import google.generativeai as genai

from moviepy.editor import TextClip, CompositeVideoClip

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


genai.configure(api_key=os.environ["GEMINI_API_KEY"])


def get_news():

    url = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"

    r = requests.get(url)

    items = r.text.split("<title>")[2:12]

    news = [i.split("</title>")[0] for i in items]

    return news


def summarize(news):

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
다음 뉴스들을 쇼츠 뉴스 영상용으로 작성하세요.

조건
- 뉴스 10개
- 자연스럽게 소개
- 각 뉴스는 2줄 설명

형식

안녕하세요.
어제 들어온 주요 뉴스 10가지를 빠르게 소개해드리겠습니다.

첫 번째 소식입니다.
내용 설명

다음 두 번째 소식입니다.
내용 설명

이런 형식으로 작성하세요.

뉴스 목록
{news}
"""

    res = model.generate_content(prompt)

    lines = res.text.split("\n")

    return [l for l in lines if l.strip() != ""]


def create_video(lines):

    clips = []

    for line in lines[:20]:

        txt = TextClip(
            line,
            fontsize=70,
            color="white",
            size=(1080,1920),
            method="caption"
        ).set_duration(3)

        clips.append(txt)

    final = CompositeVideoClip(clips)

    final.write_videofile("shorts.mp4", fps=30)


def upload_to_drive():

    creds = Credentials.from_service_account_info(
        json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]),
        scopes=["https://www.googleapis.com/auth/drive"]
    )

    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": "shorts_news.mp4",
        "parents": [os.environ["GDRIVE_FOLDER_ID"]]
    }

    media = MediaFileUpload("shorts.mp4", mimetype="video/mp4")

    service.files().create(
        body=file_metadata,
        media_body=media
    ).execute()


if __name__ == "__main__":

    news = get_news()

    lines = summarize(news)

    create_video(lines)

    upload_to_drive()
