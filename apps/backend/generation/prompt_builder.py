from generation.prompts import SYSTEM_PROMPT


class PromptBuilder:

    def build(
        self,
        question: str,
        chunks
    ) -> str:

        context = ""

        for i, chunk in enumerate(chunks, start=1):

            context += f"""
SOURCE {i}

Document: {chunk.payload['document']}
Page: {chunk.payload['page']}
Domain: {chunk.payload['domain']}

Content:
{chunk.payload['text']}

--------------------------------------
"""

        return f"""
{SYSTEM_PROMPT}

LEGAL CONTEXT

{context}

USER QUESTION

{question}

ANSWER
"""