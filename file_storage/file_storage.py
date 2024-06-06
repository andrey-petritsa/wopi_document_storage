class FileStorage:
    def __init__(self):
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def find_document_content_by_id(self, document_id):
        file = self.__find_file_by_document_id(document_id)
        return file['content']

    def __find_file_by_document_id(self, document_id):
        for file in self.files:
            if file['name'] == document_id:
                return file

        raise Exception(f'Документ {document_id} не найден в файловом хранилище')

    def find_document_info_by_id(self, document_id):
        file = self.__find_file_by_document_id(document_id)

        document_info = {
            'BaseFileName': file['name'],
            'OwnerId': 'admin',
            'Size': file['size'],
            'UserId': '1',
            'Version': '1',
            'UserCanWrite': True,
        }
        return document_info

    def save_document(self, document):
        doc_id = document['id']
        file = open(f'file_storage/{doc_id}', 'wb')
        file.write(document['content'])
        file.close()
