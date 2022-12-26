def camelSolve(words):
      s = "".join(word[0].upper() + word[1:].lower() for word in words)
      return s[0].lower() + s[1:]

def camelCaser(snake_case):
    constituents = snake_case.split('_')    
    return camelSolve(constituents)    
    
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
 


def swiftify():
    nameOfClass = input()
    f = open("input.txt", 'r') 
    variables = [] 
    keys = []
    types = [] 
    for line in f:
        elements = line.split(':', 1)
        if len(elements) == 2:
            keys.append((elements[0]))
            variables.append(camelCaser((elements[0]).split('"')[1]))
            output = elements[1]
            print(type(output))
            if countX(output, '"') == 2:
                types.append("String?")
            elif countX(output,'.') == 1:
                types.append("Double?")
            elif ("true" in output) or ("false" in output):
                types.append("Bool?")
            elif output.isnumeric:
                types.append("Int?")
        else:
            continue   
    f.close()
    g = open("output.txt", 'w')
    g.write("public class {0}: GenericResponse {{\n".format(nameOfClass))
    g.write("\n")
    for i,vare in enumerate(variables):
        g.write("\t public var {0} : {1}\n".format(variables[i],types[i]))
    g.write("\n")
    g.write("\t override open func mapping(map: Map) {\n")
    g.write("\t\t super.mapping(map: map)\n")
    for i,vare in enumerate(variables):
        g.write('\t\t {0} <- map[{1}]\n'.format(variables[i],keys[i].strip()))
    g.write("\t}\n")
    g.write("}\n")
    g.close()   


if __name__ == "__main__":
    swiftify()
