import unittest

from libreoffice_server.stub_wopi import StubWopi


class TestWopi(unittest.TestCase):
    def setUp(self):
        self.wopi = StubWopi()


    def test_check_file_info(self):
        file_id = 'any-file-id'
        file_info = self.wopi.check_file_info(file_id)

        expected = {
            'BaseFileName': 'file.txt',
            'OwnerId': '1',
            'Size': 12252,
            'UserId': '1',
            'Version': '1',
        }
        self.assertEqual(expected, file_info)

    def test_get_file(self):
        file_id = 'any-file-id'
        file = self.wopi.get_file(file_id)

        self.assertEqual(b'binary-content', file)

    def test_put_file(self):
        file_id = 'any-file-id'
        file_content = b'binary_file_content'
        self.wopi.put_file(file_id, file_content)

        self.assertTrue(self.wopi.is_put_file_called)
