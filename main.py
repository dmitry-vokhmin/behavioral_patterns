from commands import (
    PlayCommand,
    PauseCommand,
    VolumeUpCommand,
    VolumeDownCommand,
    CommandType,
    AddPlaylistCommand,
    SavePlaylistCommand,
    RestorePlaylistCommand,
    ShuffleCommand
)
from player_device import PlayerDevice
from player import PlayerApplication
from user import User

if __name__ == '__main__':
    player_device = PlayerDevice()

    player_app = PlayerApplication()
    play_command = PlayCommand(player_app)
    pause_command = PauseCommand(player_app)
    volume_up_command = VolumeUpCommand(player_app)
    volume_down_command = VolumeDownCommand(player_app)
    add_playlist_command = AddPlaylistCommand(player_app)
    save_playlist_command = SavePlaylistCommand(player_app)
    restore_playlist_command = RestorePlaylistCommand(player_app)
    shuffle_command = ShuffleCommand(player_app)

    player_device.add_command(CommandType.PLAY, play_command)
    player_device.add_command(CommandType.PAUSE, pause_command)
    player_device.add_command(CommandType.VOLUME_UP, volume_up_command)
    player_device.add_command(CommandType.VOLUME_DOWN, volume_down_command)
    player_device.add_command(CommandType.ADD_TO_PLAYLIST, add_playlist_command)
    player_device.add_command(CommandType.SAVE_PLAYLIST, save_playlist_command)
    player_device.add_command(CommandType.RESTORE_PLAYLIST, restore_playlist_command)
    player_device.add_command(CommandType.SHUFFLE, shuffle_command)

    user = User('John')
    player_app.register(user)

    player_device.execute(CommandType.PLAY, 'song')
    player_device.execute(CommandType.ADD_TO_PLAYLIST, 'song')
    player_device.execute(CommandType.ADD_TO_PLAYLIST, 'song2')
    player_device.execute(CommandType.SAVE_PLAYLIST, 'playlist')
    player_device.execute(CommandType.ADD_TO_PLAYLIST, 'song3')
    print(player_app.playlist)
    player_device.execute(CommandType.RESTORE_PLAYLIST, 'playlist')
    print(player_app.playlist)
    player_device.execute(CommandType.SHUFFLE)
