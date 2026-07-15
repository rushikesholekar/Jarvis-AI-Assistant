import re

text = "Remember my favorite language is Python"

match = re.search(
    r"Remember my (.*) is (.*)",
    text,
    re.IGNORECASE
)

if match:
    print(match.group(1))
    print(match.group(2))