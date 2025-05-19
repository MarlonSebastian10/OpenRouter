from fastapi import APIRouter
from openai import OpenAI

from interfaces.chatinterfaces import ChatCompletionResponse, InputMessage

router = APIRouter()

client = OpenAI(api_key='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',
                base_url='https://openrouter.ai/api/v1')

@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("message "+ data["message"])

    message = "Por favor responde de manera concreta, clara y siempre en castellano, español. "
    try:
        completion: ChatCompletionResponse = client.chat.completions.create(
            model="google/gemma-3-1b-it:free",
            messages=[
                {
                    "role": "system", "content": "Eres un asistente de IA que responde preguntas en español de forma clara y breve."
                },
                {
                    "role": "user",
                    "content": message + "Responde a esta pregunta: " +data["message"]
                }
            ]
        )
        print("Response "+ completion.choices[0].message.content)
        return {"Response":  completion.choices[0].message.content}
    except Exception as e:
        print(f"Error: {e}")
        return {"Error": str(e)}
    

