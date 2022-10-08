from util import Frontier, Node
from scraper import Web_Scraper
from collections import deque

def find_shortest_path(source, target):
    used = set()
    frontier = deque()
    for i in find_neighbors(source):
        frontier.append(Node(i, Node(source, None)))
        used.add(source)
    
    while frontier:
        node = frontier.popleft()
        if node.state == target:
            return find_results(node)
        else:
            neighbors = find_neighbors(node.state)
            for neighbor in neighbors:
                if neighbor not in used:
                    frontier.append(Node(neighbor, node))
                    used.add(neighbor)
    return None

def find_neighbors(source):
    base_url = 'https://en.wikipedia.org/wiki/'
    return Web_Scraper.get_links(base_url + source)

def find_results(node):
    path = []
    path.append(node.state)
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    
    return path[::-1]


source = input('From? ')
target = input('To? ')

path = find_shortest_path(source, target)

print(path)