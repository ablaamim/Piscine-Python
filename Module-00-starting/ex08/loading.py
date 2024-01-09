import sys
import os


def ft_tqdm(r: range) -> None:
    '''show a progress bar implemented using an iterator & generator'''

    terminal = os.get_terminal_size()
    # print(terminal)
    # print(terminal.columns)
    # print(terminal.lines)
    length = terminal.columns - 40
    total = len(r)

    i = 1
    for item in r:
        a = i / total  # ratio of progress
        b = int(length * a)  # number of █ to print
        b = "█" * b
        sys.stdout.write(f'\r{a:4.0%}|{b.ljust(length, " ")}| {i}/{total}')
        sys.stdout.flush()
        i += 1
        yield item

# if __name__ == '__main__':
#     for i in ft_tqdm(range(100000)):
#         pass
