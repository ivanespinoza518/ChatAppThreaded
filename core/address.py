class Address:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    def __str__(self):
        return f"addr={self.ip}, port={self.port}"
