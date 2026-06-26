from ingestion.parser import PDFParser
from ingestion.chunker import Chunker
from embeddings.embedder import Embedder
from vectorstore.indexer import Indexer


def main():
    parser = PDFParser("../../knowledge_base")
    pages = parser.parse()

    chunker = Chunker()
    chunks = chunker.chunk(pages)

    print(f"Pages  : {len(pages)}")
    print(f"Chunks : {len(chunks)}")

    embedder = Embedder()
    records = embedder.embed(chunks)

    indexer = Indexer()
    indexer.create_collection()
    indexer.index(records)

    print("\n✅ Everything completed successfully!")


if __name__ == "__main__":
    main()