from enum import Enum
from os.path import exists

import sys


class Command(Enum):
    CREATE = 'CREATE'
    DELETE = 'DELETE'
    LIST = 'LIST'
    MOVE = 'MOVE'


class Node:

    def __init__(self, name) -> None:
        self.name = name
        self.children = {}

    def is_empty(self):
        return len(self.children) == 0

    def add_child(self, child_name):
        child = Node(child_name)
        self.children[child_name] = child

    def add_child_node(self, child_node):
        self.children[child_node.name] = child_node

    def has_child(self, child_name):
        return child_name in self.children

    def get_child(self, child_name):
        return self.children[child_name]

    def remove_child(self, child_name):
        child = self.children[child_name]
        del self.children[child_name]
        return child

    def print_content(self, space_count):
        children_keys = list(self.children.keys())
        children_keys.sort()
        for child in children_keys:
            current = self.children[child]
            print('{}{}'.format(' ' * space_count, current.name))
            if not current.is_empty():
                current.print_content(space_count + 2)


def main(file_name):
    root = Node('')
    lines = read_input(file_name)
    for line in lines:
        line = line.strip()
        print(line)
        tokens = line.split(' ')
        if tokens[0] == Command.CREATE.value:
            create_directory(root, tokens[1])
        elif tokens[0] == Command.MOVE.value:
            move_directory(root, tokens[1], tokens[2])
        elif tokens[0] == Command.LIST.value:
            list_directories(root)
        elif tokens[0] == Command.DELETE.value:
            delete_directory(root, tokens[1])
        else:
            print('Unknown command: {}'.format(tokens[0]))


def read_input(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines


def delete_directory(root, path):
    tokens = path.split('/')
    current = root
    traversed = []
    while tokens:
        next_dir = tokens.pop(0)
        traversed.append(next_dir)
        if current.has_child(next_dir):
            if len(tokens) == 0:
                current.remove_child(next_dir)
            else:
                current = current.get_child(next_dir)
        else:
            print('Cannot delete {} - {} does not exist'.format(path, '/'.join(traversed)))
            break


def move_directory(root, source_path, destination_path):
    tokens = source_path.split('/')
    current = root
    source, source_parent = None, None
    traversed = []
    while tokens:
        next_dir = tokens.pop(0)
        traversed.append(next_dir)
        if current.has_child(next_dir):
            if len(tokens) == 0:
                source_parent = current
                source = current.get_child(next_dir)
            else:
                current = current.get_child(next_dir)
        else:
            print('Cannot move {} - {} does not exist'.format(source_path, '/'.join(traversed)))
            break

    tokens = destination_path.split('/')
    current = root
    traversed = []
    while tokens:
        next_dir = tokens.pop(0)
        traversed.append(next_dir)
        if current.has_child(next_dir):
            current = current.get_child(next_dir)
            if len(tokens) == 0:
                if not current.has_child(source.name):
                    current.add_child_node(source)
                    source_parent.remove_child(source.name)
                else:
                    print('Cannot move {} to {}, there is already another directory with the same name'.format(source_path, destination_path))
        else:
            print('Cannot move {} - {} does not exist'.format(destination_path, '/'.join(traversed)))
            break


def create_directory(root, path):
    tokens = path.split('/')
    current = root
    traversed = []
    while tokens:
        next_dir = tokens.pop(0)
        traversed.append(next_dir)
        if len(tokens) + 1 > 1:
            if current.has_child(next_dir):
                current = current.get_child(next_dir)
            else:
                print('Cannot create {} - {} does not exist'.format(path, '/'.join(traversed)))
                break
        else:
            if current.has_child(next_dir):
                print('Cannot create {}, directory already exists'.format(path))
            else:
                current.add_child(next_dir)


def list_directories(base_dir):
    base_dir.print_content(0)


if __name__ == '__main__':
    input_file = 'input.txt'  # Default value
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if exists(input_file):
        main(input_file)
    else:
        raise Exception('Input file "{}" does not exist'.format(input_file))
