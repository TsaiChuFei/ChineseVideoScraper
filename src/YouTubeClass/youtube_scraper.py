### OOP:
# Libraries needed for object oriented programming
from pydantic import (
BaseModel,
HttpUrl,
DirectoryPath,
model_validator,
field_validator
)

from pydantic.dataclasses import dataclass

from typing import (
ClassVar,
Optional,
List

)

### Library needed to download YouTube videos
from pytubefix import (
Playlist,
YouTube
)

### Library needed for connecting to website
import requests

class my_youtube_scraper(BaseModel):
    # ================================================================================================
    #  ** Initializations **
    # This class downloads Chinese videos and playlists using the pytubefix library
    # ================================================================================================

    video_url: Optional[HttpUrl] = None
    playlist_url: Optional[HttpUrl] = None

    @model_validator(mode = "before")
    def check_input(cls, values):
        a, b = values.get('video_url'), values.get("playlist_url")
        if (a is None and b is None) or (b is not None and a is not None):
            raise(ValueError("You must provide either video_url or playlist_url"))
        return values

    def download(self) -> List[YouTube]:
        if self.video_url:
            return self.load_video(str(self.video_url))
        else:
            return self.load_playlist(str(self.playlist_url))


    def load_playlist(self, value: str) -> List[YouTube]:
        playlist = Playlist(value)
        videos = []
        for video_url in playlist.video_urls:
            try:
                videos.append(YouTube(video_url))
            except Exception as e:
                # Videos that cant be loaded, won't interrupt the process.
                print(f"Following video couldn't be loaded: {video_url}")
        return videos

    def load_video(self, value: str) -> List[YouTube]:
        return [YouTube(value)]








