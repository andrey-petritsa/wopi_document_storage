class SpyDocumentStorage:
    def __init__(self):
        content = b'binary document content'

        self.file = {
            'name': 'test.txt',
            'content': content,
            'size': len(content)
        }

    def find_document_content_by_id(self, document_id):
        self.last_called_method = f'find_document_content_by_id({document_id})'
        return self.file['content']

    def find_document_info_by_id(self, document_id):
        self.last_called_method = f'find_document_info_by_id({document_id})'
        document_info = {
            'BaseFileName': self.file['name'],
            'OwnerId': 'admin',
            'Size': self.file['size'],
            'UserId': '1',
            'Version': '1',
            'UserCanWrite': True,
        }
        return document_info

    def save_document(self, document):
        doc_id = document['id']
        self.last_called_method = f'save_document({doc_id})'