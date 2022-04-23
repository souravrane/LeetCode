class Codec:
    counter = 0
    
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap:
            Codec.counter += 1
            shortUrl = self.base + str(Codec.counter)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))