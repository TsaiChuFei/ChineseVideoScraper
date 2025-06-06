### Python Libraries
from arrow.util import validate_ordinal
from pydantic import (
BaseModel,
HttpUrl,
ValidationError)

import pytest


### Libraries made by developer
from src.YouTubeClass.youtube_scraper import my_youtube_scraper

def test_youtube_scraper_video_input():
    user_data = {"video_url": "https://youtu.be/74FYkI9Z2_E?feature=shared"}
    youtube = my_youtube_scraper(**user_data)
    assert youtube.video_url == HttpUrl("https://youtu.be/74FYkI9Z2_E?feature=shared")

def test_invalid_video_url():
    url = "hahhaa"
    with pytest.raises(ValidationError) as exc_info:
        my_youtube_scraper(video_url = url)

def test_invalid_playlist_url():
    url = "hahhaa"
    with pytest.raises(ValidationError) as exc_info:
        my_youtube_scraper(playlist_url = url)


def test_youtube_scraper_playlist_input():
    url = "https://youtube.com/playlist?list=PLngFSf6XKRPhtjNMSjb5GQka-7wSO_WvL&si=leooXIiqeJTdC8TR"
    youtube = my_youtube_scraper(playlist_url = url)
    assert youtube.playlist_url == HttpUrl(url)


def test_youtube_scraper_playlist():
    url = "https://youtube.com/playlist?list=PLngFSf6XKRPhtjNMSjb5GQka-7wSO_WvL&si=leooXIiqeJTdC8TR"
    youtube = my_youtube_scraper(playlist_url = url)

    expected_video_count = 3
    assert len(youtube.download()) == expected_video_count

    expected_titles = ["一起慶祝雙十節：我們的台灣故事",
                       "台灣最強女鬼陳守娘！背後又是怎樣的故事？ @Mr.希爾",
                       "【封面故事搶先看】誰讓台灣回收神話幻滅 English Subtitle Available"
                       ]
    observed_titles = [i.title for i in youtube.download()]
    assert expected_titles == observed_titles

def test_youtube_scraper_video():
    url = "https://youtu.be/8CK2Igi94PE?si=XKP7v1EJmmLk8NF5"
    youtube = my_youtube_scraper(video_url = url).download()
    expected_title = "【封面故事搶先看】誰讓台灣回收神話幻滅 English Subtitle Available"
    observed_title = youtube[0].title
    assert expected_title == observed_title

