from pathlib import Path


def load_knowledge():
    """Load information from our knowledge base."""
    file_path = Path("data/knowledge.txt")
    return file_path.read_text(encoding="utf-8")


def create_prompt(question, context):
    """Create a prompt using the retrieved context."""
    return f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""


if __name__ == "__main__":
    context = load_knowledge()

    question = "What is RAG?"

    prompt = create_prompt(question, context)

    print("----- RAG Prompt -----")
    print(prompt)
