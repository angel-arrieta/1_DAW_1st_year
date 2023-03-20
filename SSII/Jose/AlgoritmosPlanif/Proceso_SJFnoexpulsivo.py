from CommonFuncs import read, casting, calculator, return_archive


def organizer(tupler):
    tupler = sorted(tupler, key=turn_n_lapse)
    ordered = []
    ordered.append(tupler.pop(0))
    while True:
        if len(tupler) == 0:
            break
        parallel = []
        wiper = []
        x = len(ordered)-1
        for task in tupler:
            if x == 0:
                begin = 1
                last = ordered[x][1] + ordered[x][2]
            else:
                for n in range(begin, len(ordered)):
                    last += ordered[n][2]
                    if n == (len(ordered)-1) and begin < len(ordered):
                        begin = last
            if task[2] <= last:
                parallel.append(task)
                wiper.append(task)
            elif task[2] > last:
                if len(tupler) == 1:
                    parallel.append(task)
                    wiper.append(task)
                break
        parallel.sort(key=lapse)
        for task in parallel:
            ordered.append(task)
        for spot in wiper:
            tupler.remove(spot)
    return ordered


def turn_n_lapse(tupler):
    return tupler[2], tupler[1]


def lapse(tupler):
    return tupler[1]


if __name__ == "__main__":
    readable = casting(read("Process.FIFO.txt"))
    organized = organizer(readable)
    executable = calculator(organized)
    return_archive(executable)
