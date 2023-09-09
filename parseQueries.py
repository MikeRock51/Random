#!/usr/bin/env python3

def solution(queries):
    container = []
    output = []

    for query in queries:
        if query[0] == "ADD":
            container.append(query[1])
            output.append("")
        elif query[0] == "EXISTS":
            if query[1] in container:
                output.append("true")
            else:
                output.append("false")
        elif query[0] == "REMOVE":
            if query[1] in container:
                container.remove(query[1])
                output.append("true")
            else:
                output.append("false")
        elif query[0] == "GET_NEXT":
            nextVal = None
            for value in sorted(container, key=lambda x: int(x)):
                if int(value) > int(query[1]):
                    nextVal = value
                    break
            if not nextVal:
                output.append("")
            else:
                output.append(str(nextVal))

    return output
