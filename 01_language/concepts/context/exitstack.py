from contextlib import ExitStack

filenames = []
with ExitStack() as stack:
    file_objects = [stack.enter_context(open(filename))
        for filename in filenames]