class PlaylistMemento:
    def __init__(self, playlist: list[str]):
        self._playlist = playlist

    def get_playlist(self):
        return self._playlist
