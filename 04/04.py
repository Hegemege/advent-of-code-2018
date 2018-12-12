

def main():
    input_data = sorted(read_input(), key=lambda row: row.split(']')[0])
    schedules = {}
    current_schedule = []
    fell_asleep = 0
    for row in input_data:
        timestamp, action = row.split('] ')
        timestamp = int(timestamp.split(':')[-1])
        # If a new guard begins their shift
        if action[0] == 'G':
            guard_id = int(action.split('#')[1].split(' ')[0])
            if guard_id not in schedules:
                schedules[guard_id] = [0 for i in range(60)]
            current_schedule = schedules[guard_id]
        elif action[0] == 'f':
            fell_asleep = timestamp
        elif action[0] == 'w':
            woke_up = timestamp
            for i in range(woke_up - fell_asleep):
                current_schedule[fell_asleep + i] += 1

    # Part 1

    sleepiest_guard = [(k, schedules[k]) for k in sorted(
        schedules,
        key=lambda key: sum(schedules[key]),
        reverse=True)][0]
    print(sleepiest_guard[0] * max(
        enumerate(sleepiest_guard[1]),
        key=lambda x: x[1])[0])

    # Part 2

    sleepiest_guard_2 = [(k, schedules[k]) for k in sorted(
        schedules,
        key=lambda key: max(schedules[key]),
        reverse=True)][0]
    print(sleepiest_guard_2[0] * max(
        enumerate(sleepiest_guard_2[1]),
        key=lambda x: x[1])[0])


def read_input():
    '''Read the file and remove trailing new line characters'''
    f = open('input.txt', 'r')
    data = list(map(lambda x: x[:-1], f.readlines()))
    f.close()
    return data


if __name__ == '__main__':
    main()
