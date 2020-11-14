import numpy as np
from collections import deque


def rotate(r):
    r = deque(r)
    r.rotate(-1)
    return list(r)


def build(r, s):
    n = [0] * 16
    for i in range(0, 16):
        n[i] = r[i] if r[i] != -1 else s[i]
    return n


def calc(r1, r2, r3, r4, r5):
    state = np.array([r1, r2, r3, r4, r5])
    tot = np.sum(state, axis=0)
    return (len(set(tot)) == 1) and tot[0] == 50


def main():
    ring0 = [8, -1, 8, -1, 16, -1, 19, -1, 8, -1, 17, -1, 6, -1, 6, -1]
    shadow0 = [6, 18, 8, 17, 4, 20, 4, 14, 4, 5, 1, 14, 10, 17, 10, 5]
    ring1 = [10, -1, 14, -1, 11, -1, 8, -1, 12, -1, 11, -1, 3, -1, 8, -1]
    shadow1 = [20, 8, 19, 10, 15, 20, 12, 20, 13, 13, 0, 22, 19, 10, 0, 5]
    ring2 = [0, -1, 11, -1, 8, -1, 8, -1, 8, -1, 10, -1, 11, -1, 10, -1]
    shadow2 = [1, 24, 8, 10, 20, 7, 20, 12, 1, 10, 12, 22, 0, 5, 8, 5]
    ring3 = [-1, 10, -1, 8, -1, 10, -1, 9, -1, 8, -1, 8, -1, 9, -1, 6]
    shadow3 = [10, 10, 10, 15, 7, 19, 18, 2, 9, 27, 13, 11, 13, 10, 18, 10]
    ring4 = [10, 1, 10, 4, 5, 3, 15, 16, 4, 7, 0, 16, 8, 4, 15, 7]
    for l3 in range(0, 16):
        for l2 in range(0, 16):
            for l1 in range(0, 16):
                for l0 in range(0, 16):
                    level1 = build(ring0, shadow0)
                    level2 = build(ring1, shadow1)
                    level3 = build(ring2, shadow2)
                    level4 = build(ring3, shadow3)
                    level5 = ring4
                    if calc(level1, level2, level3, level4, level5):
                        print(f'Solved!')
                        print(f'{60 * "-"}')
                        print(f'Level 1: {level1}')
                        print(f'Level 2: {level2}')
                        print(f'Level 3: {level3}')
                        print(f'Level 4: {level4}')
                        print(f'Level 5: {level5}')
                        print(f'{60 * "-"}\n')
                        print(f'Positions - Ring1: {l0}, Ring2: {l1}, Ring3: {l2}, Ring4: {l3}')
                        return
                    ring0 = rotate(ring0)
                ring1 = rotate(ring1)
                shadow0 = rotate(shadow0)
            ring2 = rotate(ring2)
            shadow1 = rotate(shadow1)
        ring3 = rotate(ring3)
        shadow2 = rotate(shadow2)


if __name__ == "__main__":
    main()
