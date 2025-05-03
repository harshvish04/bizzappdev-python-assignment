"""
# Problem: Seating Arrangement Problem
You have N dinner party guests. Each guest has two favorite neighbors they'd like to sit
next to. The problem is to find a valid circular seating arrangement fulfilling all
preferences.

Approach:
- Because it's a circular table, each person has to be seated so that their two
neighbors are the two individuals they prefer.
- We'll attempt all permutations of the guest list and for each, verify whether all neighbor preferences are met.
- Brute-force is acceptable for small N (<= 8).
"""

from itertools import permutations

def is_valid_seating(arrangement, preferences):
    n = len(arrangement)
    for i in range(n):
        guest = arrangement[i]
        left = arrangement[(i - 1) % n]
        right = arrangement[(i + 1) % n]
        preferred = preferences[guest]
        if not (left in preferred and right in preferred):
            return False
    return True

def find_seating_arrangement(preferences):
    guests = list(preferences.keys())
    for perm in permutations(guests):
        if is_valid_seating(perm, preferences):
            return list(perm)
    return None

# input
guests = {
    'Raj': ['Guru', 'Nuevil'],
    'Guru': ['Raj', 'Harsh'],
    'Nuevil': ['Raj', 'Harsh'],
    'Harsh': ['Guru', 'Nuevil']
}

result = find_seating_arrangement(guests)

if result:
    print("Valid seating arrangement found:")
    print(" -> ".join(result))
else:
    print("No valid seating arrangement is possible.")
