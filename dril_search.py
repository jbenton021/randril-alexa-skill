

import os
from atproto import Client
from atproto_client.namespaces.sync_ns import AppBskyFeedNamespace
from atproto_client.models.app.bsky.feed.search_posts import Params
from atproto.exceptions import AtProtocolError
from dotenv import load_dotenv



def search_dril_posts(search_term: str):
    load_dotenv()

    BLUESKY_HANDLE = os.getenv("BLUESKY_HANDLE")
    BLUESKY_APP_PASSWORD = os.getenv("BLUESKY_APP_PASSWORD")

    client = Client()

    try:
        client.login(BLUESKY_HANDLE, BLUESKY_APP_PASSWORD)
    except (ValueError, AtProtocolError):
        print("Login failed")
        return

    ns = AppBskyFeedNamespace(client)

    try:
        resp = ns.search_posts(Params(author="dril.bsky.social", q=search_term))
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
