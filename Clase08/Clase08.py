import ollama as ol

request = ol.chat(
    model="llama3.2" ,
    messages=[
        {
            "role": "system",
            "content": "Habla como un experto en motos y mecánica, y responde a las preguntas de manera clara y concisa."
        },
        {
            "role": "user",
            "content": "La ns 200 es una buena mota para principiantes?"
            
        }
    ]
)

print(request)

