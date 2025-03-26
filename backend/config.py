import json


class Config:
    host = "127.0.0.1"
    port = 5000
    web_path = "web"

    def load(self):
        f = open("config.json", "r")
        _config = json.loads(f.read())
        f.close()
        self.host = _config["host"]
        self.port = _config["port"]
        self.web_path = _config["web_path"]
