import random

from memento import PlaylistMemento
from observer import Subject


class PlaylistIterator:
    def __init__(self, playlist: list[str]):
        self._playlist = playlist
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._playlist):
            song = self._playlist[self._index]
            self._index += 1
            return song
        raise StopIteration


class PlayerApplication(Subject):
    playlist: list[str] = []
    history: dict[str, PlaylistMemento] = {}
    _observers = []

    def play(self, song: str):
        print(f"Playing {song}")
        self.notify(f"Playing {song}")

    def pause(self, song: str):
        print(f"Pausing {song}")
        self.notify(f"Pausing {song}")

    def volume_up(self, song: str):
        print(f"Volume up {song}")
        self.notify(f"Volume up {song}")

    def volume_down(self, song: str):
        print(f"Volume down {song}")
        self.notify(f"Volume down {song}")

    def add_to_playlist(self, song: str):
        self.playlist.append(song)
        print(f"Added {song} to playlist")
        self.notify(f"Added {song} to playlist")

    def save_playlist(self, playlist_name: str):
        memento = PlaylistMemento(self.playlist.copy())
        self.history[playlist_name] = memento
        print("Saving play list to disk")
        self.notify("Saving play list to disk")

    def restore_playlist(self, playlist_name: str):
        self.playlist = self.history[playlist_name].get_playlist()
        print("Restoring playlist from disk")
        self.notify("Restoring playlist from disk")

    def shuffle(self):
        print("Shuffling playlist")
        playlist = list(PlaylistIterator(self.playlist))
        random.shuffle(playlist)
        print("Shuffled playlist first song is: ", playlist[0])
        self.notify("Shuffled playlist first song is: ", playlist[0])

    def register(self, observer):
        self._observers.append(observer)

    def unregister(self, observer):
        self._observers.remove(observer)

    def notify(self, *args):
        for observer in self._observers:
            observer.update(*args)
