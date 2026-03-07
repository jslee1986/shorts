from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json

blog_id = "942916794791779939"

# access token 파일 읽기
with open("token.json") as f:
    token_data = json.load(f)

creds = Credentials(
    token=token_data["access_token"]
)

service = build("blogger", "v3", credentials=creds)

post = {
    "title": "자동 블로그 테스트",
    "content": "<h2>자동 업로드 성공</h2><p>GitHub 자동 포스팅 테스트</p>"
}

service.posts().insert(
    blogId=blog_id,
    body=post,
    isDraft=False
).execute()

print("업로드 완료")
