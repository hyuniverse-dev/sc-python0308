'''
파일명: email_service.py
'''

import smtplib
from email.mime.multipart import MIMEMultipart  # 이메일 내용 작성을 위한 import
from email.mime.text import MIMEText


def send_email(receiver: str, subject: str, body: str):
    # 이메일 발신 정보
    sender = "ggolre90@gmail.com"
    password = "thzk gzto nmvv nphz"

    # 메일 발송 준비
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    mime_text = MIMEText(body, 'plain')
    message.attach(mime_text)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
            print(f"이메일을 성공적으로 발송했습니다. (발신자:{sender}) / 수신자:{receiver}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    send_email("hyuniverse.dev@gmail.com", "테스트 메일", "테시트 본문")
