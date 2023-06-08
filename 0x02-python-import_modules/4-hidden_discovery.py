#!/usr/bin/python3
#4-hidden_discovery.py

if __name__ == "__main__":
    import hidden_4
    print(''.join([i + '\n' for i in dir(hidden_4)
        if "__" not in i[:2]]), end="")
