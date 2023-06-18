from contextlib import suppress

with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)

# this context manager is reentrant(pointing inward.) .