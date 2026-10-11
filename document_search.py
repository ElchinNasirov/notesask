from pathlib import Path

NOTES_FOLDER = Path("notes")


def search_best_matching_note(user_query: str) -> tuple[str, str] | None:
    query_words = set(user_query.lower().split())

    best_file_name = ""
    best_file_content = ""
    highest_match_score = 0

    for file_path in NOTES_FOLDER.glob("*.md"):
        file_content = file_path.read_text()

        # Calculate the number of words in the file that are also in the query
        match_score = len(query_words & set(file_content.lower().split()))

        # If the match score is higher than the current highest match score, update the best file name and content
        if match_score > highest_match_score:
            highest_match_score = match_score
            best_file_name = file_path.name
            best_file_content = file_content

    # If no match was found, return None   
    if highest_match_score == 0:
        return None
    
    # Return the best file name and content
    return best_file_name, best_file_content
