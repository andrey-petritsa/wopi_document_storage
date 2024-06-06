class StubDocumentFacade:
    def get_document(self, document_id):
        return {
            'content': b'binary_document',
            'id': 'file.txt',
            'size': len(b'binary_document')
        }

    def get_document_info(self, document_id):
        return {
            'BaseFileName': 'file.txt',
            'OwnerId': '1',
            'Size': 12252,
            'UserId': '1',
            'Version': '1',
        }

    def save_document(self, document):
        doc_id = document['id']
        self.last_called_method = f'save_document({doc_id})'