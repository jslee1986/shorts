def summarize(news):

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
다음 뉴스들을 쇼츠 뉴스 영상용으로 작성하세요.

조건
- 뉴스 10개
- 자연스러운 뉴스 진행 스타일
- 시작 멘트 포함
- 각 뉴스는 2~3줄 설명

형식

안녕하세요.
어제 들어온 주요 뉴스 10가지를 빠르게 소개해드리겠습니다.

첫 번째 소식입니다.
내용 설명

다음 두 번째 소식입니다.
내용 설명

세 번째 소식입니다.
내용 설명

이런 형식으로 작성하세요.

뉴스 목록
{news}
"""

    res = model.generate_content(prompt)

    lines = res.text.split("\n")

    return [l for l in lines if l.strip()!=""]
