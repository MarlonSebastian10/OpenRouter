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