from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int

    def print(self, indent=""):
        print(f"{indent}{self.name} {self.size}")


@dataclass
class Directory:
    name: str
    parent: Directory
    size: int = 0
    files: dict[str, File] = field(default_factory=dict)
    directories: dict[str, Directory] = field(default_factory=dict)

    def get_dir(self, name):
        return self.directories[name]

    def add_dir(self, name):
        self.directories[name] = Directory(name=name, parent=self)

    def add_file(self, name, size):
        self.files[name] = File(name=name, size=size)

    def num_children(self):
        return len(self.files) + len(self.directories)

    def compute_size(self):
        self.size = sum(file.size for file in self.files.values()) + sum(
            directory.compute_size() for directory in self.directories.values()
        )

        return self.size

    def get_sizes(self):
        return [self.size] + [
            size
            for directory in self.directories.values()
            for size in directory.get_sizes()
        ]

    def print(self, indent=""):
        print(f"{indent}{self.name}/ (tot = {self.size})")
        if self.num_children() == 0:
            print(f"{indent + '    '}-- No children --")
            return

        for file in self.files.values():
            file.print(indent + "    ")

        for name, directory in self.directories.items():
            directory.print(indent + "    ")


class FS:
    def __init__(self, fname):
        self.path = []
        self.root = Directory(name="", parent=None)
        self.cwd = self.root

        with open(fname) as fp:
            commands = fp.readlines()

        self.parse_commands(commands[1:])

    def parse_commands(self, commands):
        for line in commands:
            tokens = line.split()
            if tokens[0] == "$":
                self.do_command(tokens[1:])
            else:
                self.add_structure(tokens)

    def do_command(self, tokens):
        if tokens[0] == "ls":
            return

        if tokens[1] == "..":
            self.cwd = self.cwd.parent
        else:
            self.cwd = self.cwd.get_dir(tokens[1])

    def add_structure(self, tokens):
        comm, name = tokens
        if comm == "dir":
            self.cwd.add_dir(name)
        else:
            self.cwd.add_file(name, int(comm))

    def compute_sizes(self):
        return self.root.compute_size()

    def get_sizes(self):
        return self.root.get_sizes()

    def print(self):
        self.root.print()


fs = FS("day07.txt")
root_size = fs.compute_sizes()
sizes = fs.get_sizes()
fs.print()

print(f"Part 1: {sum(size for size in sizes if size <= 100000)}")

print(f"Part 2: {min(size for size in sizes if size >= root_size - 40000000)}")
