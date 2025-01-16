import http.client

class HttpConnection:
    def httpRequest(self) -> str:
        connection = http.client.HTTPConnection("www.example.com")
        connection.request("GET", "/")
        response = connection.getresponse()
        results = response.read().decode()
        connection.close()
        return results