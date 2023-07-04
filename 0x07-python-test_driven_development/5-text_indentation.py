#!/usr/bin/python3

"""
Text_indentation Module
adds two new lines after "?.:"
doesn't print any spaces at the beginning or end of the sentences.
"""


def text_indentation(text):
    """
    text_indentation function:
    checks to see if input is valid
    adds two new lines after any instances of `?` or `.` or `:`
    then prints the result without any new lines at the beginning
    """
    if not isinstance(text, str):
        raise TypeError("text must be astring")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

        while count < len(text):
            print(text[count], end="")
            if text[count] == "\n" or text[count] in ".?:":
                if text[count] in ".?:":
                    print("\n")
                    count = count + 1
                    while count < len(text) and text[count] == " ":
                        count = count + 1
                        continue
                    count = count + 1
