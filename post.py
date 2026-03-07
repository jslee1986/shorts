import smtplib
from email.mime.text import MIMEText
import random

blog_email = "dlwnstkd11.blogpost@blogger.com"

titles = [
"AI 투자 전망",
"비트코인 2026 전망",
"건강에 좋은 영양제 추천",
"AI 시대 돈 버는 방법"
]

contents = [
"AI 시장은 빠르게 성장하고 있습니다. 앞으로 투자 기회가 많아질 것으로 보입니다.",
"비트코인은 여전히 많은 투자자들의 관심을 받고 있습니다.",
"건강을 위해 많은 사람들이 영양제를 찾고 있습니다.",
"AI 시대에는 새로운 직업과 수익 모델이 등장하고 있습니다."
]

title = random.choice(titles)
content = random.choice(contents)

msg = MIMEText(content)
msg["Subject"] = title
msg["From"] = "yourgmail@gmail.com"
msg["To"] = blog_email

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("yourgmail@gmail.com", "앱비밀번호")
server.sendmail("yourgmail@gmail.com", blog_email, msg.as_string())
server.quit()

print("블로그 글 게시 완료")
