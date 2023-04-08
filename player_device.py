from commands import Command, CommandType


class PlayerDevice:
    commands: dict[CommandType, Command] = {}

    def add_command(self, command_type: CommandType, command: Command):
        self.commands[command_type] = command

    def execute(self, command_type: CommandType, *args):
        command = self.commands.get(command_type)
        if command:
            command.execute(args)
        else:
            print(f"Command {command_type} not found")
