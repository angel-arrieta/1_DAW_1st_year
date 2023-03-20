from CommonFuncs import read, casting, calculator, return_archive


def first(tupler):
    return tupler[2]


if __name__ == "__main__":
    readable = casting(read("Process.FIFO.txt"))
    organized = sorted(readable, key=first)
    executable = calculator(organized)
    return_archive(executable)
