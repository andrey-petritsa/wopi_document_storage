class DocumentFacade:
    def __init__(self, document_storage):
        self.__document_storage = document_storage

    def get_document(self, document_id):
        document_content = self.__document_storage.find_document_content_by_id(document_id)
        document = {
            'content': document_content,
            'id': document_id,
            'size': len(document_content),
        }
        return document

    def get_document_info(self, document_id):
        return self.__document_storage.find_document_info_by_id(document_id)

    def save_document(self, document):
        return self.__document_storage.save_document(document)
