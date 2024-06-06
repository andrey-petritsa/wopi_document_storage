class WopiRouter:
    def route(self, request):
        command = {
            'name': 'null',
            'file_id': 'null',
        }

        if 'GET /wopi/files/' in request:
            command['name'] = 'get_file_info'
            left_part = request.split('?')[0]
            command['file_id'] = left_part.split('/')[-1]

        if 'GET /wopi/files/' in request and '/contents' in request:
            command['name'] = 'get_file'
            left_part = request.split('?')[0]
            command['file_id'] = left_part.split('/')[-2]

        if 'POST /wopi/files/' in request and '/contents' in request:
            command['name'] = 'put_file'
            left_part = request.split('?')[0]
            command['file_id'] = left_part.split('/')[-2]

        if 'GET /edit' in request:
            command['name'] = 'show_edit_page'
            left_part = request.split('?')[0]
            command['file_id'] = left_part.split('/')[-1]

        return command

