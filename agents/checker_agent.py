import requests

def fact_check(text: str) -> str:
    prompt = f"Check this summary for bias or hallucination. Suggest improvements:\n\n{text}"
    response = requests.post("http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False})
    return response.json()["response"].strip()
