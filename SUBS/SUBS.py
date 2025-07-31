# Finding a Motif in DNA


def get_the_sequence(file_loc):
    with open(file_loc, "r") as file:
        lines = file.readlines()
    s_list = lines[0].split()
    t_list = lines[1].split()
    s = "".join(s_list)
    t = "".join(t_list)
    print(type(s))
    positions = []

    for i in range(len(s) - len(t)):
        search = s.find(t, i)
        if search > 0:
            positions.append(search)

    unique = []
    [unique.append(val) for val in positions if val not in unique]

    final_ans = []
    for x in unique:
        final_ans.append(x + 1)

    print(final_ans)


get_the_sequence("SUBS/rosalind_subs.txt")
