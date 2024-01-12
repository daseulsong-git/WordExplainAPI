from fastapi import FastAPI, HTTPException
import openai

app = FastAPI()

# OpenAI API 키 설정
openai.api_key = ""

@app.get("/explain/{word}")
async def explain_word(word: str):
    # ChatGPT에 질문을 물어봅니다.
    prompt = f"Explain the word '{word}'."

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # 또는 사용 가능한 다른 엔진 선택
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # API 응답에서 답변 추출
        answer = response.choices[0].text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # 응답 반환
    return {"word": word, "explanation": answer}
