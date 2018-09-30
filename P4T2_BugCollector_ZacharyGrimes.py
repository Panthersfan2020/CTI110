# The project that I am doing today is BugCollector
# Thursaday September 20 2018
# CTI-110 P4T2 - Bug Collector
# Zachary Grimes
#

total = 0

for day in range(1, 8):

    print("Enter the bugs collected on day", day)

    bugs = int(input())

    total += bugs

print("You collected a total of", total, "bugs.")
