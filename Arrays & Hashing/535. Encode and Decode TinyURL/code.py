class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodedMap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.encodeMap:
            return self.encodeMap[logUrl]
        shortUrl = self.base + str(len(self.encodeMap)+1)
        self.encodeMap[longUrl] = shortUrl
        self.decodedMap[shortUrl] = longUrl
        return shortUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodedMap[shortUrl] 
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))