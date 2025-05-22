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