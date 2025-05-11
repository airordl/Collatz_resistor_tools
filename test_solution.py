import math

def coll(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

N = 875514018568053701214007839211072313423758584413036683813182871324569488094620616837514582073833253943883336490984917884260362118774652388107578507264

GAV = 10**9

seen = set()

steps = 0

while True:
    if N == 1:
        print("Reached 1 after", steps, "steps.")
        break

    if N in seen:
        print("Nontrivial cycle detected! Stuck at:", math.floor(N))
        break

    seen.add(N)
    N = coll(N)
    steps += 1

    if steps % 10**6 == 0:
        print(f"Progress: {steps:,} steps completed.")

