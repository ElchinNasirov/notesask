# NotesAsk

Simple RAG pipeline. Answers a question from a folder of markdown notes. Python picks the file. Llama 3.2 answers from that file only. If no note matches, the reply is "not in the notes."

No paid API. No web search. Ollama runs llama3.2 on the same machine.

## Run

uv run python ask.py
uv run python check.py

Requires Ollama running and `ollama pull llama3.2`.

## Files

- notes/ — three sample notes
- document_search.py — picks the note with the most shared words
- llm_client.py — one local model call
- rag_agent.py — citation from code, answer from the model
- agent_evaluator.py — five saved questions, pass or fail
- ask.py — one-question demo

## Check

Latest run: 3/5.

- Ollama model question passed.
- JobFit rank was in the note, and the model said it was not.
- France correctly refused, but the reply still named a file. The check does not catch that yet.
- "Scores drift" was in jobfit.md. The model quoted a different sentence.

The file choice is more stable than the answer. The next fix is the check, not a longer prompt.