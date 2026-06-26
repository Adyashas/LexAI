from pathlib import Path
import fitz

from models.document import DocumentPage


class PDFParser:

    def __init__(self, knowledge_base_path: str):
        self.knowledge_base = Path(knowledge_base_path)

    def parse(self) -> list[DocumentPage]:

        documents = []

        # Loop through each domain folder
        for domain_folder in self.knowledge_base.iterdir():

            if not domain_folder.is_dir():
                continue

            domain = domain_folder.name

            # Read every PDF inside the domain
            for pdf_file in domain_folder.glob("*.pdf"):

                print(f"Reading: {pdf_file.name}")

                pdf = fitz.open(pdf_file)

                for page_number, page in enumerate(pdf, start=1):

                    text = page.get_text()

                    if text.strip():

                        documents.append(
                            DocumentPage(
                                domain=domain,
                                document=pdf_file.name,
                                source=str(pdf_file),
                                page=page_number,
                                text=text.strip()
                            )
                        )

                pdf.close()

        return documents