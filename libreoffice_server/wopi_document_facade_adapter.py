import re


class WopiDocumentFacadeAdapter:
    def __init__(self, document_facade):
        self.__document_facade = document_facade

    def get_file_info(self, file_id):
        return self.__document_facade.get_document_info(file_id)

    def get_file(self, file_id):
        document = self.__document_facade.get_document(file_id)

        file = {
            'content': document['content'],
            'name': document['id'],
            'size': document['size']
        }
        return file

    def put_file(self, file):
        return self.__document_facade.save_document(file)
