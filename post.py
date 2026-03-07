import smtplib
from email.mime.text import MIMEText
import random

# 블로그 이메일 (Blogger 이메일 게시 주소)
blog_email = "dlwnstkd11.blogpost@blogger.com"

# 글 제목 후보
titles = [
"AI 투자 전망 2026",
"비트코인 앞으로 어떻게 될까",
"AI 시대 돈 버는 방법",
"건강을 위한 최고의 영양제",
"요즘 뜨는 AI 직업 TOP5"
]

# 글 내용 후보
contents = [
"""
AI 시장은 빠르게 성장하고 있습니다.
많은 기업들이 인공지능 기술을 활용하고 있으며
앞으로 더 많은 투자 기회가 생길 것으로 예상됩니다.

특히 자동화 기술과 AI 서비스는 앞으로
경제 구조를 크게 바꿀 가능성이 있습니다.
""",

"""
비트코인은 여전히 많은 투자자들의 관심을 받고 있습니다.
최근 몇 년 동안 큰 변동성을 보였지만
장기적으로는 상승 가능성을 보는 전문가들도 많습니다.

투자를 할 때는 항상 리스크 관리가 중요합니다.
""",

"""
AI 시대에는 새로운 직업들이 계속 등장하고 있습니다.
AI 활용 능력이 중요한 경쟁력이 되고 있습니다.

특히 자동화와 데이터 분석 능력은
앞으로 많은 기업에서 필요로 할 것입니다.
""",

"""
건강을 위해 많은 사람들이 영양제를 찾고 있습니다.
비타민, 오메가3, 마그네슘 등은 꾸준히 인기 있는 영양제입니다.

하지만 개인 건강 상태에 맞는 제품을
선택하는 것이 가장 중요합니다.
""",

"""
최근 AI 기술이 발전하면서
많은 새로운 직업들이 등장하고 있습니다.

AI 개발자, 데이터 분석가, 자동화 전문가 등
미래 직업으로 주목받는 분야가 늘어나고 있습니다.
"""
]

# 랜덤으로 제목과 내용 선택
title = random.choice(titles)
content = random.choice(contents)

# 이메일 작성
msg = MIMEText(content)
msg["Subject"] = title
msg["From"] = "dlwnstkd11@gmail.com"
msg["To"] = blog_email

# Gmail SMTP 연결
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# Gmail 로그인 (앱 비밀번호)
server.login("dlwnstkd11@gmail.com", "zmwlpeskeoqwjvxr")

# 이메일 전송
server.sendmail("dlwnstkd11@gmail.com", blog_email, msg.as_string())

server.quit()

print("블로그 글 게시 완료")
