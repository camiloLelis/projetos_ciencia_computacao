def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    cont = 0
    if target_time is None:
        return None
    for period in permanence_period:
        entrySystem, exitSystem = period
        if type(entrySystem) != int or type(exitSystem) != int:
            return None
        if target_time >= entrySystem and target_time <= exitSystem:
            cont += 1

    return cont


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

print(study_schedule(permanence_period, 5))
