import sys

summary = 0
count = 0
for line in sys.stdin:
    try:
        summary += float(line)
    except:
        count += 1
print(summary if int(summary)!=summary else int(summary))
print(count)