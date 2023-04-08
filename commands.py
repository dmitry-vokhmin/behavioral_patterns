from abc import ABC, abstractmethod
from enum import StrEnum

from player import PlayerApplication


class CommandType(StrEnum):
    PLAY = 'play'
    PAUSE = 'pause'
    VOLUME_UP = 'volume_up'
    VOLUME_DOWN = 'volume_down'
    ADD_TO_PLAYLIST = 'add_to_playlist'
    SAVE_PLAYLIST = 'save_playlist'
    RESTORE_PLAYLIST = 'restore_playlist'
    SHUFFLE = 'shuffle'


class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass


class PlayCommand(Command):
    def __init__(self, player_app: PlayerApplication):
        self.player_app = player_app

    def execute(self, *args):
        self.player_app.play(args[0])


class PauseCommand(Command):
    def __init__(self, player_app: PlayerApplication):
        self.player_app = player_app

    def execute(self, *args):
        self.player_app.pause(args[0])


class VolumeUpCommand(Command):
    def __init__(self, player_app: PlayerApplication):
        self.player_app = player_app

    def execute(self, *args):
        self.player_app.volume_up(args[0])


class VolumeDownCommand(Command):
    def __init__(self, player_app: PlayerApplication):
        self.player_app = player_app

    def execute(self, *args):
        self.player_app.volume_down(args[0])


class AddPlaylistCommand(Command):
    def __init__(self, player_app: PlayerApplication):
        self.player_app = player_app

    def execute(self, *args):
        self.player_app.add_to_playlist(args[0])


class SavePlaylistCommand(Command):
    def __init__(self, player_app: PlayerApplication):
        self.player_app = player_app

    def execute(self, *args):
        self.player_app.save_playlist(args[0])


class RestorePlaylistCommand(Command):
    def __init__(self, player_app: PlayerApplication):
        self.player_app = player_app

    def execute(self, *args):
        self.player_app.restore_playlist(args[0])


class ShuffleCommand(Command):
    def __init__(self, player_app: PlayerApplication):
        self.player_app = player_app

    def execute(self, *args):
        self.player_app.shuffle()
