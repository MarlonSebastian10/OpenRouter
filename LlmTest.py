from openai import OpenAI

client = OpenAI(api_key='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',
                base_url='https://openrouter.ai/api/v1')

message = input("Cual es tu pregunta?: ")

prompt = (
    "Por favor, responde de manera clara y sin simbolos innecesarios."
    "Evita usar otros idiomas que no sea el castellano y escribe una respuesta concisa y directa."
    f"Pregunta del Usuario: {message}"
)

completion = client.chat.completions.create(
    model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(completion.choices[0].message.content)