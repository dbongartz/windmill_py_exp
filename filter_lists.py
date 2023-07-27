# Tasks
# 1. Filter a list of Things based on multiple criteria
# 2. Fold a list of Things based on a criteria => maximum of each point
# 3. Plot a tuple of filtered_things with folded_thing
# 4. Repeat for different filter critera
#
# (5. Optimization: Can take a list of filter criteria)

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Thing:
    values: List[int] = []
    name: str = ""


thing1 = Thing(values=[1, 2, 3, 4, 5], name="t1")
thing2 = Thing(values=[1, 4, 3, 4, 5], name="t2")
thing3 = Thing(values=[1, 1, 5, 4, 5], name="t1")
thing4 = Thing(values=[1, 2, 3, 7, 5], name="t3")


def filter_thing(things: List[Thing], name_critera: str) -> List[Thing]:
    result: List[Thing] = []

    for thing in things:
        if thing.name == name_critera:
            result.append(thing)

    return result


def fold_max_thing(things: List[Thing]) -> Thing:
    result: Thing = Thing(values=[], name="cluster")
    # fold to max

    # result.values.append(max())

    return result


def plot_tuple_things(tuple_thing: Tuple[List[Thing], Thing]):
    plot_list_of_things(tuple_thing[1])
    plot_list_of_things(tuple_thing[0])


things = [thing1, thing2, thing4, thing4]

criteras = ["t1", "t2", "t3"]

# fn
grouped_things = list()

for cr in criteras:
    grouped_things.append(filter_thing(things=things, name_critera=cr))

# fn
grouped_cluster = list()

for group in grouped_cluster:
    grouped_cluster.append(fold_max_thing(group))

# fn
for grouped_cluster, grouped_things in zip(grouped_things, grouped_cluster):
    plot_tuple_things((grouped_things, grouped_cluster))
