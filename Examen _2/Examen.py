import ollama as ol
import gradio as gr

def recomendar_juego(genero):
    
    f"Recomiéndame un juego del género {genero}."

    system_prompt = """
    Habla como un experto en juegos de video, y responde a las preguntas de manera clara y concisa en español,la cantidad de recomendaciones solo puede ser 3 y la respuesta debe ser solo el nombre de los juegos nada mas. 

    """
 
    request = ol.chat(
        model="llama3.2" ,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": "recomiéndame un juego del género {genero}."
                
            }
        ]
    )

    return request ["message"]["content"]

with gr.Blocks() as app:
    gr.Markdown("<h1 style='text-align: center;'>Recomendador de Juegos</h1>")
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Selecciona un género")
            genero = gr.Textbox(
                label="Género",
                placeholder="Escribe el género del juego en que estas interesado"
            )
            boton = gr.Button("Recomendar juego", variant="primary")
        with gr.Column():
            gr.Markdown("## Juego recomendado")
            recomendacion = gr.Textbox(label="Juego recomendado")

    
    boton.click(recomendar_juego, inputs=[genero], outputs=[recomendacion])


app.launch() 