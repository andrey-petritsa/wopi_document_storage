import unittest

from libreoffice_server.wopi_document_facade_adapter import WopiDocumentFacadeAdapter
from test.stub_document_facade import StubDocumentFacade


class TestWopiDocumentFacadeAdapter(unittest.TestCase):
    def setUp(self):
        self.stub_facade = StubDocumentFacade()
        self.wopi_document_facade = WopiDocumentFacadeAdapter(self.stub_facade)

    def test_get_file_info(self):
        expected_file_info = {
            'BaseFileName': 'file.txt',
            'OwnerId': '1',
            'Size': 12252,
            'UserId': '1',
            'Version': '1',
        }
        self.assertEqual(expected_file_info, self.wopi_document_facade.get_file_info('stub-file-id'))

    def test_get_file(self):
        expected_file = {
            'content': b'binary_document',
            'name': 'file.txt',
            'size': 15,
        }
        self.assertEqual(expected_file, self.wopi_document_facade.get_file('stub-file-id'))

    def test_put_file(self):
        file = {'id': 'stub-file-id', 'content': b'binary_document'}
        self.wopi_document_facade.put_file(file)
        self.assertEqual('save_document(stub-file-id)', self.stub_facade.last_called_method)
