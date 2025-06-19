

import os
from atproto import Client
from atproto_client.namespaces.sync_ns import AppBskyFeedNamespace
from atproto_client.models.app.bsky.feed.search_posts import Params
from atproto.exceptions import AtProtocolError
from dotenv import load_dotenv



import os
from dotenv import load_dotenv
from atproto import Client, AtProtocolError
from atproto_client.namespaces.sync_ns import AppBskyFeedNamespace
from atproto_client.models.app.bsky.feed.search_posts import Params

_client = None
_ns = None

def _initialize_client():
    
    global _client, _ns
    
    if _client is None:
        load_dotenv()
        
        BLUESKY_HANDLE = os.getenv("BLUESKY_HANDLE")
        BLUESKY_APP_PASSWORD = os.getenv("BLUESKY_APP_PASSWORD")
        
        _client = Client()
        
        try:
            _client.login(BLUESKY_HANDLE, BLUESKY_APP_PASSWORD)
            _ns = AppBskyFeedNamespace(_client)
            print("Successfully logged in to Bluesky")
        except (ValueError, AtProtocolError) as e:
            print(f"Login failed: {e}")
            _client = None
            _ns = None
            raise

def search_dril_posts(search_term: str):
    """Search for posts by dril containing the search term."""
    if _client is None:
        _initialize_client()
    
    if _ns is None:
        print("Client not initialized")
        return
    
    try:
        resp = _ns.search_posts(Params(author="dril.bsky.social", q=search_term))
    except AtProtocolError:
        print("Search failed")
        return
    
    if resp:
        for post in resp.posts:
            if post.record.text:
                print(post.record.text)

if __name__ == "__main__":
    search_term = input("Input a search term: ")
    search_dril_posts(search_term)
