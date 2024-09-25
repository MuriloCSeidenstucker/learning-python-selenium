from src.access_anvisa_domain import AnvisaDomain
from src.pdf_manager import PDFManager


def load_config():
    pdf_manager = PDFManager()
    anvisa_domain = AnvisaDomain(pdf_manager)

    return (pdf_manager, anvisa_domain)
