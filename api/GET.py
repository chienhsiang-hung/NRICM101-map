from http.server import BaseHTTPRequestHandler
import pymongo
import os
from bson.json_util import dumps

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    client = pymongo.MongoClient( os.environ['MONGODB_URI'] )
    db = client['NRICM101-map']
    col = db['source']

    print(dumps(list(col.find()), ensure_ascii=False).encode('utf8').decode())

    # self.send_response(200)
    # self.send_header('Content-type', 'text/html')
    # self.end_headers()
    


    # self.wfile.write(html.encode('utf-8'))

    return
    