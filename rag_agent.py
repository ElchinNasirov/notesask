from document_search import search_best_matching_note
from llm_client import llm_call 

# RAG Agent that answers questions based on the best matching note
def run_rag_agent(user_question: str) -> str:

    # Search for the best matching note
    search_result = search_best_matching_note(user_question)

    # If no match was found, return a message
    if search_result is None:
        return "not in the notes"

    file_name, file_text = search_result

    ai_instructions = (
        "Instructions:\n"
        "1. Answer in one short line, using only the note.\n"
        "2. If the exact answer is not explicitly mentioned in the note text, reply exactly with: not in the notes\n\n"
        f"FILE TEXT:\n{file_text}\n\n"
        f"QUESTION: {user_question}"
    )

    ai_responce = llm_call(ai_instructions)
    return f"{file_name}\n{ai_responce}"