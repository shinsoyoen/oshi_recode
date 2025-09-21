import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 불러오기
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API 키를 .env 파일에 설정해야 합니다.")

# Gemini API 설정
genai.configure(api_key=api_key)

# 모델 생성 및 사용
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content("인공지능에 대해 한 문장으로 설명하세요.")

print(response.text)