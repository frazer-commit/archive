import numpy as np
import time

rng = np.random.default_rng()

# Typical implementation
def step1(frame):
    new_frame = np.zeros(frame.shape, dtype=int)

    for iy, row in enumerate(frame):
        for ix, cell in enumerate(row):
            # Get neighbor coords around the cell
            x1 = max(0, ix-1)
            y1 = max(0, iy-1)
            x2 = min(frame.shape[1], ix+2)
            y2 = min(frame.shape[0], iy+2)

            window = frame[y1:y2, x1:x2]

            neighbours = np.sum(window)
            neighbours -= cell

            if neighbours == 3:
                new_frame[iy, ix] = 1
            elif neighbours == 2 and cell == 1:
                new_frame[iy, ix] = 1
            else:
                new_frame[iy, ix] = 0

    return new_frame

# My version
def step2(frame):
    nbs = np.zeros(frame.shape)

    # Create padding
    temp = np.zeros([i+2 for i in frame.shape])
    temp[1:-1, 1:-1] = frame

    frame = temp

    height = frame.shape[0]
    width = frame.shape[1]

    # Generate 8 neighbour windows
    for y in range(3):
        for x in range(3):
            if x == 1 and y == 1:
                continue
            w = frame[y:height-2+y, x:width-2+x]
            nbs += w

    # Whether a cell should stay alive or not
    condition = lambda cell, nbs: cell*(nbs==2) + (nbs==3)
    
    result = condition(frame[1:-1, 1:-1], nbs)
    
    return result

def show(frame):
    for row in frame:
        for cell in row:
            print("█" if cell == 1 else " ", end="")
        print()

def speed_test(*functions):
    start_frame = rng.integers(0, 2, size=(50, 50))
    
    for func in functions:
        frame = start_frame[:]
        start = time.time()
        
        for _ in range(500):
            frame = func(frame)
        
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed*1000:.0f}ms")


if __name__ == "__main__":
    # "Blazingly fast" / 270x speed increase :o
    speed_test(step1, step2)
    """
    speed_test(step1)
    frame = np.zeros((10, 10), dtype=int)

    frame[1, 2] = 1
    frame[2, 3] = 1
    frame[3, 1:4] = [1, 1, 1]

    print("Start")
    show(frame)
    
    print("Step1")
    show(step1(frame))

    print("Step2")
    show(step2(frame))
    """
