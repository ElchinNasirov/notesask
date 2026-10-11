from rag_agent import run_rag_agent

EVAL_TEST_CASES = [
    ("Which model does Ollama run here?", "ollama.md", "llama3.2"),
    ("Does JobFit print a rank?", "jobfit.md", "yes"),
    ("What should NotesAsk do if the fact is missing?", "notesask.md", "say so"),
    ("What is the capital of France?", None, "not in the notes"),
    ("What happens to scores between runs?", "jobfit.md", "drift"),
]

def check_agent_acuracy(agent_reply: str, expected_file: str | None, expected_keyword: str) -> bool:
    reply_lowercase = agent_reply.lower()

    # Rule 1: The expected keyword must be in the answer
    if expected_keyword not in reply_lowercase:
        return False

    # Rule 2: If no file was supposed to be found
    if expected_file is None:
        return "not in the notes" in reply_lowercase

    # Rule 3: The correct filename must be printed in the answer
    return expected_file in agent_reply

if __name__ == "__main__":
    passed_tests_count = 0

    for question, expectde_file, expected_keyword in EVAL_TEST_CASES:
        agent_reply = run_rag_agent(question)

        is_correct = check_agent_acuracy(agent_reply, expectde_file, expected_keyword)
        passed_tests_count += int(is_correct)

        status_label= "PASS" if is_correct else "FAIL"
        clean_reply_log = agent_reply.replace("\n", " | ")
        print(f"[{status_label}] {clean_reply_log}")

    print(f"\nFinal Score: {passed_tests_count}/{len(EVAL_TEST_CASES)} tests passed.")
