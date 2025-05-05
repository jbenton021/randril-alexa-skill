
import json
from atproto import Client
from atproto_client.namespaces.sync_ns import AppBskyFeedNamespace
from atproto_client.models.app.bsky.feed.search_posts import Params

def search_dril_posts(search_term: str):
    BLUESKY_HANDLE = "falldownbear.bsky.social"
    BLUESKY_APP_PASSWORD = "irto-zi4x-f4ax-26su"

    client = Client()
    client.login(BLUESKY_HANDLE, BLUESKY_APP_PASSWORD)

    ns = AppBskyFeedNamespace(client)

    resp = ns.search_posts(Params(author="dril.bsky.social", q=search_term))

    if resp:
        for post in resp.posts:
            if post.record.text:
                print(post.record.text)

if __name__ == "__main__":
    search_term = input("Input a search term: ")
    search_dril_posts(search_term)
