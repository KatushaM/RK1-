from operator import itemgetter

class micr:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class comp:
    def __init__(self, id, name, power, id_micr):
        self.id = id
        self.name = name
        self.power = power
        self.id_micr = id_micr


class micr_comp:
    def __init__(self, id_micr, id_comp):
        self.id_comp = id_comp
        self.id_micr = id_micr


micrs = [
    micr(1, "intel"),
    micr(2, 'intel 5'),
    micr(3, 'intel 4'),
    micr(44, 'intel 2'),
    micr(55, 'intel 9'),
]

comps = [
    comp(1, 'mac', 2000, 1),
    comp(2, 'hp', 3000, 2),
    comp(3, 'asus', 5000, 3),
    comp(4, 'asus 2', 4000, 3),
    comp(5, 'asus 3', 6000, 3),
]

micrs_comps = [
    micr_comp(1, 1),
    micr_comp(2, 2),
    micr_comp(3, 3),
    micr_comp(44, 1),
    micr_comp(55, 2),
    micr_comp(3, 4),
    micr_comp(3, 5),
]


def func_1(one_to_many):
    return [(comp_name, micr_name) for comp_name, _, micr_name in one_to_many if comp_name[0] == 'a']


def func_2(one_to_many):
    micrs_power = [(m_name, c_power) for _, c_power, m_name in one_to_many]
    res = sorted(micrs_power, key=itemgetter(1), reverse=False)
    unique_result = []
    temp = ''
    for mc_name, mc_power in res:
        if mc_name != temp:
            unique_result.append((mc_name, mc_power))
            temp = mc_name
    return unique_result


def func_3(many_to_many):
    return sorted(many_to_many, key=itemgetter(1))


def main():
    one_to_many = [(c.name, c.power, m.name)
                   for m in micrs
                   for c in comps
                   if c.id_micr == m.id]

    many_to_many_temp = [(m.name, mc.id_micr, mc.id_comp)
                         for m in micrs
                         for mc in micrs_comps
                         if m.id == mc.id_micr]

    many_to_many = [(c.name, c.power, micr_name)
                    for micr_name, id_micr, id_comp in many_to_many_temp
                    for c in comps if c.id == id_comp]

    print('Задание 1:')
    for comp_name, micr_name in func_1(one_to_many):
        print(comp_name, micr_name)

    print('\nЗадание 2:')
    for mc_name, mc_power in func_2(one_to_many):
        print(mc_name, mc_power)

    print('\nЗадание 3:')
    for item in func_3(many_to_many):
        print(item)

if __name__ == '__main__':
    main()
