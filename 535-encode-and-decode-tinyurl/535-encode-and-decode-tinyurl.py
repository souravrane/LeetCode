class Codec:
    num = 0
    url = "http://tinyurl.com/"
    h = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        Codec.num += 1
        key = Codec.url + str(Codec.num)
        Codec.h[key] = longUrl
        return key
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return Codec.h[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
