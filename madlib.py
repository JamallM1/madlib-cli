
print("Welcome to Madlib")

def read_template (path):
    file = open(path, "r")
    read = file.read()
    file.close()
    return read.strip()

def parse_template(words):
    string = ""
    lis = []
    capture = False
    captured_word = ""
    for x in words:
        if capture:
            if x == "}":
                capture = False
                lis.append(captured_word)
                captured_word = ""
                string += x
            else:
                captured_word += x
        else:
            string += x
            if x == "{":
                capture = True
    return string, tuple(lis)

def merge(str, tup):
    return str.format(*tup)

print("""   
Welcome to My Madlib game
Please input info for a response
""")

if __name__ == '__main__':
    filepath = "Assets/make_me_a_video_game_output.txt"

    final, desc = parse_template(read_template(filepath))

    responses = []
    for x in desc:
        if x.lower() == "adjective":
            print(f"Enter an {x}")
            response = input("> ")
            responses.append(response)
        else:
            print(f"Enter a {x}")
            response = input("> ")
            responses.append(response)

    print(merge(final, tuple(response)))
