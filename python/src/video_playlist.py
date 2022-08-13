"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, playlist_name: str):
        self.playlist_name = playlist_name
        self.videos = []
    
    # @property
    # def playlist_name(self) -> str:
    #     """Returns the name of a playlist."""
    #     return self._playlist_name
