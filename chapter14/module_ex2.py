'''
파일명: module_ex2.py

이메일 발송 모듈(smtp 라이브러리)
'''
import smtplib
from email.mime.multipart import MIMEMultipart  # 이메일 내용 작성을 위한 import
from email.mime.text import MIMEText

# 이메일 발신 정보
sender = "ggolre90@gmail.com"  # 메일 보내는 사람 아이디
password = "thzk gzto nmvv nphz"  # 메일 보내는 사람의 패스워드

# 이메일 수신 정보
receiver = "hyuniverse.dev@gmail.com"  # 메일 받는 사람

# 이메일 내용 구성
subject = "[파이썬-2] smtp 라이브러리를 활용한 메일 발송하기"
body = "이 메일은 파이썬의 smtp 내장 라이브러리를 활용하여 발송된 메일입니다."

# 메일 발송 준비
message = MIMEMultipart()
message["From"] = sender  # 보내는 사람 데이터
message["To"] = receiver  # 받는 사람 데이터
message["Subject"] = subject  # 이메일 제목
mime_text = MIMEText(body, 'plain')  # 이메일 본문 형식
message.attach(mime_text)

# Gmail의 SMTP 서버에 연결
#   SMTP_SSL: 보안 소켓 계층을 사용해서 SMTP 서버에 연결
#   stmp.gmail.com: Gmail 서버 도메인
#   465: Gmail에서 허용한 통로(표준 포트 번호)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
    print(f"이메일을 성공적으로 발송했습니다. (발신자:{sender}) / 수신자:{receiver}")
