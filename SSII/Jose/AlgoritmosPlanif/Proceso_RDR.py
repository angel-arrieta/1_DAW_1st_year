from CommonFuncs import read, casting, calculator, return_archive


def lectureRDR(tupler):
    Quan = tupler[(len(tupler)-1)][1]
    tupler.pop((len(tupler)-1))
    return tupler, Quan


def orderRDR(tupler, Qua):
    tydied = []
    while True:
        tupler = sorted(tupler, key=first)
        if len(tupler) == 0:
            break
        parallel = []
        wiper = []
        for task in tupler:
            division = task[1] - Qua
            if division > 0:
                another = []
                parts = []
                if len(task[0]) == 1:
                    parts.append(task[0])
                    parts.append("2")
                    letter = "".join(parts)
                elif len(task[0]) == 2:
                    parts.append(task[0][0])
                    parts.append(str(int(task[0][1]) + 1))
                    letter = "".join(parts)
                another.append(letter)
                task[1] = Qua
                another.append(division)
                time = 0
                for cycle in tupler:
                    if cycle[0] == tupler[0]:
                        time += cycle[1]
                        time += cycle[2]
                    else:
                        time += cycle[1]
                another.append(time)
                tupler.append(another)
                parallel.append(task)
                wiper.append(task)
            else:
                parallel.append(task)
                wiper.append(task)

        for task in parallel:
            tydied.append(task)
        for spot in wiper:
            tupler.remove(spot)

    return tydied


def first(tupler):
    return tupler[2]


if __name__ == "__main__":
    #Las ejecuciones tiene un ciclo de espera, de cuando entran
    #Da la falsa sensación de estar divididos en quantos de 6
    legible = casting(read("Process.RDR.txt"))
    readable, Quanto = lectureRDR(legible)
    ordered = orderRDR(readable, Quanto)
    executable = calculator(ordered)
    return_archive(executable)
