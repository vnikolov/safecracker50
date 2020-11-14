import numpy as np
from collections import deque


# Rotate a ring
def rotate(r):
    r = deque(r)
    r.rotate(1)
    return list(r)


# Build the ring in play
def build(r, s):
    n = [0] * 16
    for i in range(0, 16):
        n[i] = r[i] if r[i] != -1 else s[i]
    return n


# Calculate all positions and check if the sum matches the expected value
def check(r0, r1, r2, r3, r4):
    exp: int = 50
    s = np.array([r0, r1, r2, r3, r4])
    t = np.sum(s, axis=0)
    return (len(set(t)) == 1) and t[0] == exp


# Run the solution
def main():
    # Rings, top down. The shadow is the one under the ring.
    ring0 = [8, -1, 8, -1, 16, -1, 19, -1, 8, -1, 17, -1, 6, -1, 6, -1]
    shadow0 = [6, 18, 8, 17, 4, 20, 4, 14, 4, 5, 1, 14, 10, 17, 10, 5]
    ring1 = [10, -1, 14, -1, 11, -1, 8, -1, 12, -1, 11, -1, 3, -1, 8, -1]
    shadow1 = [20, 8, 19, 10, 15, 20, 12, 20, 13, 13, 0, 22, 19, 10, 0, 5]
    ring2 = [0, -1, 11, -1, 8, -1, 8, -1, 8, -1, 10, -1, 11, -1, 10, -1]
    shadow2 = [1, 24, 8, 10, 20, 7, 20, 12, 1, 10, 12, 22, 0, 5, 8, 5]
    ring3 = [-1, 10, -1, 8, -1, 10, -1, 9, -1, 8, -1, 8, -1, 9, -1, 6]
    shadow3 = [10, 10, 10, 15, 7, 19, 18, 2, 9, 27, 13, 11, 13, 10, 18, 10]
    ring4 = [10, 1, 10, 4, 5, 3, 15, 16, 4, 7, 0, 16, 8, 4, 15, 7]

    count = 0
    for i3 in range(0, 16):
        for i2 in range(0, 16):
            for i1 in range(0, 16):
                for i0 in range(0, 16):
                    count += 1
                    # Establish the ring numbers at the current position
                    level1 = build(ring0, shadow0)
                    level2 = build(ring1, shadow1)
                    level3 = build(ring2, shadow2)
                    level4 = build(ring3, shadow3)
                    level5 = ring4
                    
                    # Check if the current position solves the problem
                    if check(level1, level2, level3, level4, level5):
                        print(f'Solved! Took only {count} operations...')
                        print(f'{60 * "-"}')
                        print(f'Level 1: {level1}')
                        print(f'Level 2: {level2}')
                        print(f'Level 3: {level3}')
                        print(f'Level 4: {level4}')
                        print(f'Level 5: {level5}')
                        print(f'{60 * "-"}\n')
                        print(f'Positions - Ring 1 ({i0}), Ring 2 ({i1}), Ring 3 ({i2}), Ring 4 ({i3})')
                        return
                    
                    # Rotate the top ring
                    ring0 = rotate(ring0)
                    
                # Rotate the second ring
                ring1 = rotate(ring1)
                shadow0 = rotate(shadow0)
                
            # Rotate the third ring
            ring2 = rotate(ring2)
            shadow1 = rotate(shadow1)
            
        # Rotate the forth ring
        ring3 = rotate(ring3)
        shadow2 = rotate(shadow2)


if __name__ == "__main__":
    main()
