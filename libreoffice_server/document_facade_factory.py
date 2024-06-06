from file_storage.file_storage import FileStorage
from libreoffice_server.document_facade import DocumentFacade
from libreoffice_server.wopi_document_facade_adapter import WopiDocumentFacadeAdapter
from test.spy_document_storage import SpyDocumentStorage


class DocumentFacadeFactory:
    @staticmethod
    def create_document_facade():
        storage = FileStorage()
        storage.add_file(DocumentFacadeFactory.read_test_docx_file())

        return WopiDocumentFacadeAdapter(DocumentFacade(storage))

    @staticmethod
    def read_test_docx_file():
        with open('file_storage/test.docx', 'rb') as file:
            content = file.read()
            file = {
                'content': content,
                'size': len(content),
                'name': 'test.docx'
            }
        return file


