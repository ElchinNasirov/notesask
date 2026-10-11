import ollama

def llm_call(prompt: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
         # HIGHLIGHT FOR INTERVIEWS: Setting temperature to 0 makes the model deterministic
        options={
            "temperature": 0.0
        }
    )
    return response["message"]["content"]