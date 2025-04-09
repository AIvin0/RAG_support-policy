# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv
from langchain_upstage import UpstageDocumentParseLoader
from langchain_teddynote import logging

# API KEY 정보로드
load_dotenv()

# LangSmith 추적을 설정합니다. https://smith.langchain.com


# 프로젝트 이름을 입력합니다.
logging.langsmith("CH07-DocumentLoader")



# 파일 경로
file_path = ".\data\중소벤처기업 지원사업_샘플.pdf"

layzer = UpstageDocumentParseLoader(
            file_path,
            split='page',
            output_format='html',
           )

docs = layzer.load()

for doc in docs[:3]:
    print(doc)
