

async def structured_call(prompt: str):
    gemini = structured_llm.invoke(prompt)
    return gemini