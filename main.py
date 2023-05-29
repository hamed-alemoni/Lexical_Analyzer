final_state = False


def main():
    source = input('Enter a string : ') + '\0'
    state = start = 1
    while not final_state:
        for ch in source:

            if state == 1 or state == 2:
                start, state = first_dfa(ch, state, start)

            elif state == 3 or state == 4 or state == 5:
                start, state = second_dfa(ch, state, start)

            elif state == 6 or state == 7:
                start, state = third_dfa(ch, state, start)

            elif state == 8:
                start, state = forth_dfa(ch, state, start)



def first_dfa(ch: chr, state, start):
    global final_state

    ch_int = convert_to_integer(ch)

    if state == 1:
        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            state = 2
        else:
            start = fail(start)
            state = start

    elif state == 2:
        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch_int >= 0 and ch_int <= 9):
            state = 2
        elif ch == '' or ch == '\n' or ch == EOFError or ch == '\0':
            print('ID')
            state = 8
            final_state = True
        else:
            start = fail(start)
            state = start

    return start, state


def second_dfa(ch: chr, state, start):
    global final_state

    ch_int = convert_to_integer(ch)

    if state == 3:

        if ch_int >= 1 and ch_int <= 9:
            state = 4
        else:
            start = fail(start)
            state = start

    elif state == 4:

        if ch == '.':
            state = 5
        elif ch_int >= 0 and ch_int <= 9:
            state = 4
        else:
            start = fail(start)
            state = start

    elif state == 5:

        if ch_int >= 0 and ch_int <= 9:
            state = 5
        elif ch == '' or ch == '\n' or ch == EOFError or ch == '\0':
            print('REAL')
            state = 8
            final_state = True
        else:
            start = fail(start)
            state = start

    return start, state


def third_dfa(ch: chr, state, start):

    global final_state

    ch_int = convert_to_integer(ch)

    if state == 6:

        if ch_int >= 1 and ch_int <= 9:
            state = 7
        else:
            start = fail(start)
            state = start

    elif state == 7:

        if ch_int >= 0 and ch_int <= 9:
            state = 7
        elif ch == '' or ch == '\n' or ch == EOFError or ch == '\0':
            print('NUM')
            state = 8
            final_state = True
        else:
            print('print error in input stream')
            start = fail(start)
            state = start

    return start, state


def forth_dfa(ch: chr, state, start):
    if ch == '' or ch == '\n':
        state = 8
    elif ch == EOFError:
        exit(0)
    else:
        state = start = 1

    return start, state


def convert_to_integer(ch):
    try:
        ch = int(ch)
        return ch
    except Exception:
        return -1



# determine next DFA start state
def fail(start):

    if start == 1:
        next_start = 3
    elif start == 3:
        next_start = 6
    elif start == 6:
        next_start = 8

    return next_start

if __name__ == '__main__':
    main()
