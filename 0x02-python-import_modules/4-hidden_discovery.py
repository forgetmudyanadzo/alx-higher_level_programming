#!/usr/bin/python3
#4-hidden_discovery.py

if __name__ == "__main__":
    import hidden_4
    all_dir = dir(hidden_4)
    avoid = "__"
    for i in range(0, len(all_dir)):
        if avoid not in all_di[i]:
            print(all_dir[i])
