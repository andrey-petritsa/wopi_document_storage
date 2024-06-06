import json
from http.server import HTTPServer, BaseHTTPRequestHandler

from libreoffice_server.document_facade import DocumentFacade
from libreoffice_server.document_facade_factory import DocumentFacadeFactory
from libreoffice_server.wopi_document_facade_adapter import WopiDocumentFacadeAdapter
from libreoffice_server.wopi_router import WopiRouter
from test.spy_document_storage import SpyDocumentStorage


class WebRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        wopi_router = WopiRouter()
        command = wopi_router.route(f'GET {self.path}')
        self.__handle_command(command)

    def do_POST(self):
        wopi_router = WopiRouter()
        command = wopi_router.route(f'POST {self.path}')
        self.__handle_command(command)

    def __handle_command(self, command):
        document_facade = DocumentFacadeFactory.create_document_facade()
        if command['name'] == 'get_file':
            file = document_facade.get_file(command['file_id'])
            self.send_response(200)
            self.send_header('content-type', 'application/octet-stream')
            self.send_header('Content-Disposition', f'attachment; filename=' + file['name'])
            self.send_header('Content-Length', file['size'])
            self.end_headers()
            self.wfile.write(file['content'])

        if command['name'] == 'get_file_info':
            file_info = document_facade.get_file_info(command['file_id'])
            bytes_file_info = json.dumps(file_info).encode()
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes_file_info)

        if command['name'] == 'put_file':
            file = {'id': command['file_id'], 'content': self.__read_document_content_from_body()}
            document_facade.put_file(file)
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'')

        if command['name'] == 'show_edit_page':
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            edit_page_bytes = open('editor.html', 'rb').read()
            self.wfile.write(edit_page_bytes)

        if command['name'] == 'null':
            self.send_response(404)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'not found')

    def __read_document_content_from_body(self):
        file_len = int(self.headers.get('Content-Length'))
        file = self.rfile.read(file_len)
        return file


def start_web_server():
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()


start_web_server()
