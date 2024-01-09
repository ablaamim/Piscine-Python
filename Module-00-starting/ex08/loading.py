import sys
import os


def ft_tqdm(lst: range) -> None:
    '''show a progress bar implemented using an iterator & generator'''

    # print(os.get_terminal_size())
    term = os.get_terminal_size()

    length = term.columns - 40
    total = len(lst)

    i = 1
    for item in lst:
        a = i / total
        b = int(length * a)
        b = "█" * b
        sys.stdout.write(f'\r{a:4.0%}|{b.ljust(length, " ")}| {i}/{total}')
        sys.stdout.flush()
        i += 1
        yield item
