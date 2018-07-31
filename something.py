import requests
import pycurl
from urlparse import urljoin
from fame.core.module import ProcessingModule

class something(ProcessingModule):
    name = "something"

    config = [
        {
            'name': 'IP',
            'type': 'str',
            'default': 'https://127.0.0.1',
            'description': "IP of something machine"
        }
        ]

    def each(self, target):
        f = open("/tmp/file.txt","w")
        f.write("run")
        f.close()
        return True

