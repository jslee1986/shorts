from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/blogger']

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES)

creds = flow.run_console()

service = build('blogger', 'v3', credentials=creds)

blog_id = "여기에블로그ID"

title = "자동 블로그 테스트"
content = "<h2>자동 블로그 글</h2><p>이 글은 자동으로 업로드됩니다.</p>"

post = {
    "title": title,
    "content": content
}

service.posts().insert(
    blogId=blog_id,
    body=post,
    isDraft=False
).execute()

print("업로드 완료")
