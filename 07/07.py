

def main():
    input_data = list(map(lambda row: [row[5], row[36]], read_input()))

    # Part 1

    # Include all nodes mentioned
    unique_nodes = list(set(
        list(map(lambda x: x[1], input_data)) +
        list(map(lambda x: x[0], input_data))
    ))

    # Create lookup for nodes
    nodes = {}
    for node in unique_nodes:
        nodes[node] = []

    # Add requirements
    for requirement, node in input_data:
        nodes[node].append(requirement)

    order = ''

    while len(nodes) > 0:
        without_requirements = list(filter(
            lambda x: len(x[1]) == 0,
            list(nodes.items())
        ))

        choice = min(without_requirements, key=lambda x: x[0])[0]
        order += choice
        for k, v in nodes.items():
            if choice in v:
                v.remove(choice)
        nodes.pop(choice)

    print(order)

    # Part 2

    worker_count = 5
    additional_time = 60

    # Create lookup for nodes
    nodes = {}
    for node in unique_nodes:
        nodes[node] = []

    # Add requirements
    for requirement, node in input_data:
        nodes[node].append(requirement)

    workers = [[] for i in range(worker_count)]
    time = 0
    while len(nodes) > 0 or len(list(filter(lambda x: len(x) > 0, workers))) > 0:
        # Complete work
        for worker in workers:
            if len(worker) > 0:
                if worker[1] == 0:
                    for k, v in nodes.items():
                        if worker[0] in v:
                            v.remove(worker[0])
                    worker.clear()

        # Check if there are free workers
        free_workers = list(filter(lambda x: len(x) == 0, workers))

        # For each worker, take some work
        for free_worker in free_workers:
            without_requirements = list(filter(
                lambda x: len(x[1]) == 0,
                list(nodes.items())
            ))

            # Check if there work to do
            if len(without_requirements) > 0:
                choice = min(without_requirements, key=lambda x: x[0])[0]
                nodes.pop(choice)

                # ord('A') = 65, A=1, B=2, C=3 seconds etc
                work_time = additional_time + ord(choice) - 64
                free_worker.append(choice)
                free_worker.append(work_time)

        # Advance time and reduce the worker's time left
        time += 1
        for worker in workers:
            if len(worker) > 0:
                worker[1] -= 1

    print(time - 1)


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
