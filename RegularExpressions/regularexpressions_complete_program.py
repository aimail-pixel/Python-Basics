"Core Basics complete program: Regular Expressions (re module)"

def main():
    import re

    text = "ccu-42: Open; DEL-108: Closed"
    pattern = re.compile(r"\b(?P<city>[A-Z]{3})-(?P<number>\d+)\b", re.I)
    print("Starts with ticket:", bool(pattern.match(text)))
    print("First ID:", pattern.search(text).group())
    print("Fields:", pattern.findall(text))
    for hit in pattern.finditer(text):
        print(hit.groupdict(), hit.span())
    print("Masked:", pattern.sub(r"\g<city>-***", text))
    for record in re.split(r";\s*", text):
        code, status = re.split(r":\s*", record, maxsplit=1)
        print("Valid:", bool(pattern.fullmatch(code)), bool(re.fullmatch(r"\w+", status)))


if __name__ == "__main__":
    main()
