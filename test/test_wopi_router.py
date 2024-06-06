import unittest

from libreoffice_server.wopi_router import WopiRouter


class TestWopiRoute(unittest.TestCase):
    def setUp(self):
        self.wopi_router = WopiRouter()


    def test_route_get_document_info(self):
        expected_command = {'name': 'get_file_info', 'file_id': 'file.txt'}
        self.assertEqual(expected_command, self.wopi_router.route('GET /wopi/files/file.txt?access_token=test&access_token_ttl=0'))


    def test_route_get_document(self):
        expected_command = {'name': 'get_file', 'file_id': 'file.txt'}
        self.assertEqual(expected_command, self.wopi_router.route('GET /wopi/files/file.txt/contents?access_token=test&access_token_ttl=0'))

    def test_route_save_document(self):
        expected_command = {'name': 'put_file', 'file_id': 'file.txt'}
        self.assertEqual(expected_command, self.wopi_router.route('POST /wopi/files/file.txt/contents?access_token=test&access_token_ttl=0'))

    def test_route_edit_page(self):
        expected_command = {'name': 'show_edit_page', 'file_id': 'file.txt'}
        self.assertEqual(expected_command, self.wopi_router.route('GET /edit/file.txt?access_token=test&access_token_ttl=0'))
