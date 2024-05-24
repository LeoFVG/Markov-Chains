import random
import time
import os

graph = {
    "HELLO": {"GOODBYE": 0.5, "HELLO": 0.75}, # HELLO has a 50% chance of making a GOODBYE and a 75% chance of making another hello
    "GOODBYE": {"HELLO": 0.5, "GOODBYE": 0.2} # GOODBYE has a 50% chance of making a HELLO and a 20% chance of making a GOODBYE
}

def move(node: str, graph: dict[str: dict[str: float]]) -> str:
    try:
        weights = list(graph[node].values())
        edges = list(graph[node].keys())
        return random.choices(edges, weights)[0]
    except KeyError:
        print(f"Selected node [{node}] is not in graph")
        return KeyError

def markov_chain_sim(selected_node: str, sleep: float = 0) -> None:
    try:
        while True:
            selected_node = move(selected_node, graph)
            if selected_node == KeyError:
                break
            else:
                print(selected_node, end="\n")
                time.sleep(sleep)
    except Exception as e:
        print(e)
        raise e


selected_node = "HELLO" #start simulation from the HELLO node
markov_chain_sim(selected_node, sleep=0.1)
