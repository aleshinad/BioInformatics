# list for lines in P.fa
p = []
# open P.fa and read lines in cycle, removing new line character
with open('P.fa', 'r') as f:
    for line in f:
        p.append(line.strip())

# list for lines in T.fa
t = []
# open T.fa and read lines in cycle, removing new line character
with open('T.fa', 'r') as f:
    for line in f:
        t.append(line.strip())


# prefix function
def prefix(s):
    prefix_list = [0] * len(s)
    j = 0
    i = 1

    while i < len(s):
        if s[j] != s[i]:
            if j > 0:
                j = prefix_list[j - 1]
            else:  # j == 0
                i += 1
        else:  # s[j] == s[i]
            prefix_list[i] = j + 1
            i += 1
            j += 1

    return prefix_list


def kmp(sub, s):

    i = 0
    j = 0
    prefix_sub = prefix(sub)

    while i < len(s):
        if sub[j] == s[i]:
            i += 1
            j += 1

            if j == len(sub):
                return i - len(sub) + 1

        elif j > 0:
            j = prefix_sub[j-1]
        else:
            i += 1

    return -1


if __name__ == '__main__':

    index = kmp(p[0], t[0])
    print(index)


