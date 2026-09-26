import ollama as ol
import gradio as gr

def recomendar_libro(genero):
    # Crear un prompt para recomendar un libro basado en el género proporcionado
    prompt = f"Recomiéndame un libro del género {genero}."

    system_prompt = """
    Habla como un experto en libros y literatura, y responde a las preguntas de manera clara y concisa. 

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
                "content": "recomiéndame un libro del género {genero}."
                
            }
        ]
    )

    return request ["message"]["content"]

with gr.Blocks() as app:
    gr.Markdown("<h1 style='text-align: center;'>Recomendador de Libros</h1>")
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Selecciona un género")
            genero = gr.Dropdown(
                label="Género",
                choices=["Ficción", "No Ficción", "Misterio", "Romance", "Ciencia Ficción", "Fantasía"]
            )
            boton = gr.Button("Recomendar libro", variant="primary")
        with gr.Column():
            gr.Markdown("## Libro recomendado")
            recomendacion = gr.Textbox(label="Libro recomendado")

    # Conectar el botón a la función de recomendación
    boton.click(recomendar_libro, inputs=[genero], outputs=[recomendacion])


app.launch()
