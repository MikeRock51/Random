def solution(queries):
    storage = []
    output = []
    
    def getFile(fileName):
        for file in storage:
            if file['name'] == fileName:
                return file
                
    def getPrefixFile(prefix, limit):
        files = []
        
        for file in storage:
            if file['name'].startswith(prefix):
                files.append(file)
        
        files = sorted(files, key=lambda x: int(x['size']), reverse=True)
        return files[:int(limit)]
    
    for query in queries:
        if query[0] == "ADD_FILE":
            if getFile(query[1]):
                output.append("false")
            else:
                file = {
                    "name": query[1],
                    "size": query[2]
                }
                storage.append(file)
                output.append("true")
        elif query[0] == "GET_FILE_SIZE":
            file = getFile(query[1])
            if not file:
                output.append("")
            else:
                output.append(file['size'])
        elif query[0] == "DELETE_FILE":
            file = getFile(query[1])
            if not file:
                output.append("")
            else:
                storage.remove(file)
                output.append(file['size'])
        elif query[0] == "GET_N_LARGEST":
            files = getPrefixFile(query[1], query[2])
            filesLength = len(files)
            if filesLength < 1:
                output.append("")
            else:
                formatString = ""
                # files = sorted(files, key=lambda x: x['name'])
                index = 0
                
                for file in files:
                    formatString += f"{file['name']}({file['size']})"
                    if index < filesLength - 1:
                        formatString += ", "
                    index += 1

                output.append(formatString)
                print(output)
            
                
    return output
