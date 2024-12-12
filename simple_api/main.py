from fastapi import FastAPI

# FastAPI Instance 생성
app = FastAPI()


# Path Operation 생성 : Path는 domain 명 제외하고 / 로 시작하는 URL 부분
# Operation은 GET, POST, PUT/PATCH, DELETE 등의 HTTP 메소드
# Path Operation 에 따른 수행 함수 생성
@app.get(
    "/",
    summary="간단한 API",
    tags=["simple"],
    # description="매우 간단한 API"
)
async def root():
    """
    docstring 으로도 swagger 에서 description을 남겨놓을 수 있다. (markdown 형식)

    - 내용 1
    - 내용 2
    """
    return {"message": "Hello World"}
