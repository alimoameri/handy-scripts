#!/usr/bin/python3
import sys
import urllib.parse

def decode_url(encoded_url):
    """Decode a percent-encoded URL."""
    return urllib.parse.unquote(encoded_url)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ali.urldecoder.py <encoded_url>")
        sys.exit(1)

    encoded_url = sys.argv[1]
    decoded_url = decode_url(encoded_url)
    print(decoded_url)
