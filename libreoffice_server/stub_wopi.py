class StubWopi:
    def check_file_info(self, file_id):
        self.last_check_file_info_file_id = file_id

        return {
            'BaseFileName': 'file.txt',
            'OwnerId': '1',
            'Size': 12252,
            'UserId': '1',
            'Version': '1',
        }

    def get_file(self, file_id):
        return b'binary-content'

    def put_file(self, file_id, file_content):
        self.is_put_file_called = True