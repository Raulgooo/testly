from langchain import 
from backend.app.graph.models import ProcessState
from backend.app import gemini_logic

#First node, get the book file from google cloud storage and put it into the state
async def get_book_node(state: ProcessState):
    get_book_result = gemini_logic.get_book(book_name=state.book_name)
    return {state.book_name: get_book_result}

async def book_outline_node(state: ProcessState):
    gemini = structured_llm.invoke("")
    

