import unittest

from libreoffice_server.document_facade import DocumentFacade
from test.spy_document_storage import SpyDocumentStorage


class TestDocument(unittest.TestCase):
    def setUp(self):
        self.document_storage = SpyDocumentStorage()
        self.facade = DocumentFacade(self.document_storage)

    def test_get_document(self):
        self.facade.get_document('stub-document-id')
        self.assertEqual("find_document_content_by_id(stub-document-id)", self.document_storage.last_called_method)

    def test_get_document_info(self):
        document_info = self.facade.get_document_info('stub-document-id')
        self.assertEqual('find_document_info_by_id(stub-document-id)', self.document_storage.last_called_method)
        self.assertEqual(23, document_info['Size'])

    def test_save_document(self):
        document = {
            'id': 'stub-document-id',
            'content': b'binary-document-content'
        }
        self.facade.save_document(document)

        self.assertEqual('save_document(stub-document-id)', self.document_storage.last_called_method)