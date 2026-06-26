from langchain_text_splitters import RecursiveCharacterTextSplitter

from models.document import DocumentPage
from models.chunk import DocumentChunk


class Chunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def chunk(
        self,
        pages: list[DocumentPage]
    ) -> list[DocumentChunk]:

        chunks = []

        counter = 0

        for page in pages:

            splits = self.splitter.split_text(page.text)

            for split in splits:

                counter += 1

                chunks.append(
                    DocumentChunk(
                        domain=page.domain,
                        document=page.document,
                        source=page.source,
                        page=page.page,
                        chunk_id=f"chunk_{counter}",
                        text=split
                    )
                )

        return chunks