'''
파일명: email_service.py
'''

import smtplib
from email.mime.multipart import MIMEMultipart  # 이메일 내용 작성을 위한 import
from email.mime.text import MIMEText
import time

from chapter98.application.lotto_service import store_numbers


def send_lotto_numbers(email: str):  # receiver 파라미터 추가
    strftime = time.strftime("%Y-%m-%d")
    numbers = store_numbers()
    template = get_template(numbers, strftime)
    send_email(email, "GUI 구현한 이메일 발송 기능", template)


def send_email(receiver: str, subject: str, body: str):
    # 이메일 발신 정보
    sender = "ggolre90@gmail.com"
    password = "thzk gzto nmvv nphz"

    # 메일 발송 준비
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    mime_text = MIMEText(body, 'html')
    message.attach(mime_text)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
            print(f"이메일을 성공적으로 발송했습니다. (발신자:{sender}) / 수신자:{receiver}")
    except Exception as e:
        print(e)


def get_template(numbers: list, current_date: str):
    # HTML은 웹 페이지의 구조를 정의한 마크업 언어이다.
    # 예를 들어, 텍스트, 이미지, 링크 등을 웹 페이지에 추가할 수 있게 해준다.

    # CSS는 웹 페이지의 "디자인"을 담당한다. HTML로 구성된 웹 페이지의 외관을 꾸미고 디자인 해준다.
    return f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>행운의 로또 번호</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{
            margin: 0;
            padding: 20px;
            font-family: 'Noto Sans KR', sans-serif;
            background-color: #f0f0f0;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        .container {{
            max-width: 600px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            text-align: center;
        }}
        .header {{
            background-color: #7957d4;
            color: white;
            padding: 20px 0;
            font-weight: 700;
            font-size: 24px;
        }}
        .title {{
            font-size: 24px;
            font-weight: 700;
            color: #333;
            margin: 20px 0;
        }}
        .description {{
            font-size: 16px;
            color: #666;
            margin-bottom: 20px;
        }}
        .lotto-numbers {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            padding: 10px;
        }}
        .lotto-number {{
            width: 50px;
            height: 50px;
            border-radius: 50%;
            text-align: center;
            line-height: 50px;
            font-size: 18px;
            font-weight: 700;
            color: white;
            margin: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }}
        .info-box {{
            background-color: #f9f9f9;
            border-left: 5px solid #7957d4;
            margin: 20px;
            padding: 20px;
            text-align: left;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #7957d4;
            color: white;
            border-radius: 25px;
            text-decoration: none;
            font-weight: 600;
            margin-bottom: 20px;
            transition: background-color 0.3s;
        }}
        .button:hover {{
            background-color: #6842c2;
        }}
        .footer {{
            font-size: 13px;
            color: #999;
            padding: 20px 0;
            background-color: #f1f1f1;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">오늘의 행운</div>
        <h1 class="title">행운의 번호가 도착했어요</h1>
        <p class="description">이번 주 특별히 선정된 로또 번호입니다</p>

        <!-- 로또 번호 섹션 -->
        <div class="lotto-numbers">
            {''.join(f'<div class="lotto-number" style="background-color: {"#fbc400" if number <= 10 else "#69c8f2" if number <= 20 else "#ff7272" if number <= 30 else "#aaaaaa" if number <= 40 else "#b0d840"};">{number}</div>' for number in numbers)}
        </div>

        <div style="font-size: 14px; color: #555; background-color: #f5f5f5; border-radius: 30px; padding: 10px 20px; display: inline-block; margin: 0 auto;">
            {current_date}
        </div>

        <div class="info-box">
            <h3 style="font-size: 16px; font-weight: 700; color: #7957d4; margin-top: 0; margin-bottom: 10px;">
                ℹ️ 번호 선택 알고리즘
            </h3>
            <p>오늘의 행운은 최첨단 AI 알고리즘을 활용하여 과거 당첨 패턴을 분석하고 최적의 번호 조합을 제안합니다. 물론, 실제 당첨을 보장하지는 않지만 행운을 기원합니다!</p>
        </div>

        <a href="http://localhost:8000/" class="button">🏠 서비스로 돌아가기</a>

        <div class="footer">
            <p>&copy; 오늘의 행운. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
"""


if __name__ == "__main__":
    template = get_template([1, 2, 3, 4, 5, 6], "2025-04-13")
    send_email("hyuniverse.dev@gmail.com", "이메일 탬플릿 사용하기", template)
