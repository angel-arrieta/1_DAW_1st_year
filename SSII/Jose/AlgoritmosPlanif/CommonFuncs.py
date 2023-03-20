def read(fichero):
    try:
        exist = open("executed.txt")
        exist.close()
        import os
        os.remove("executed.txt")
        raise FileNotFoundError
    except FileNotFoundError:
        tupler = []
        with open(fichero) as process:
            listed = process.readlines()
            for arrange in listed:
                stripped = arrange.rstrip("\n")
                tupler.append(stripped.split(" "))
            process.close()
            tupler.pop(0)
        return tupler


def casting(listed):
    assign = []
    import re
    for tuples in listed:
        bind = []
        for data in tuples:
            if re.match("[0-9]", data) is None:
                bind.append(data)
            elif re.match("[0-9]", data) is not None:
                cast = int(data)
                bind.append(cast)
        assign.append(bind)
    return assign


def calculator(tuples):
    listed = []
    will_begin = 0
    for tasks in tuples:
        put = []
        process = tasks[0]
        put.append(process)
        if will_begin != 0:
            begin = will_begin
        elif will_begin == 0:
            begin = will_begin + tasks[2]
        put.append(begin)
        end = begin + tasks[1]
        put.append(end)
        listed.append(put)
        will_begin = end + 1
    return listed


def return_archive(calculated_matrix):
    with open("executed.txt", "x") as new:
        for cycle in calculated_matrix:
            new.write(f"Proceso {cycle[0]}: entra en el ciclo {cycle[1]} y sale en el ciclo {cycle[2]}\n")
        new.close()
        return print("Fichero creado con el resultado (executed.txt)")
