from typing import Any, Dict, List, Optional, Union

def merge_book_state(old_state: Optional[BookState], new_data: Union[BookState, dict]) -> BookState:
    if old_state is None:
        return BookState(**new_data) if isinstance(new_data, dict) else new_data
    curr_data = old_state.model_dump()
    updates = new_data if isinstance(new_data, dict) else new_data.model_dump(exclude_unset=True)
    if "about_the_book" in updates and updates["about_the_book"]:
        if curr_data["about_the_book"] is None:
            curr_data["about_the_book"] = updates["about_the_book"]
        else:
            curr_data["about_the_book"].update(updates["about_the_book"])
    if "chapter_outline" in updates and updates["chapter_outline"]:
        curr_outline = {item["chapter_number"]: item for item in (curr_data["chapter_outline"] or [])}
        for item in updates["chapter_outline"]:
            curr_outline[item["chapter_number"]] = item
        curr_data["chapter_outline"] = [curr_outline[k] for k in sorted(curr_outline.keys())]
    if "chapter_analyses" in updates and updates["chapter_analyses"]:
        curr_analyses = {item["chapter_number"]: item for item in (curr_data["chapter_analyses"] or [])}
        for item in updates["chapter_analyses"]:
            curr_analyses[item["chapter_number"]] = item        
        curr_data["chapter_analyses"] = [curr_analyses[k] for k in sorted(curr_analyses.keys())]
    return BookState(**curr_data)