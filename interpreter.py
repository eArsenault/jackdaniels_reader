import re

def time_eval(string, paces):
    total_time = 0

    #check for repeats - this can't handle nested parentheses for now
    while "(" in string:
        #find the first pair of parentheses
        o = string.find("(")
        c = string.find(")")
        #we want the last number before the open
        val = int(re.findall(r'\d+', string[:o])[-1])

        string = string[:o] + (val - 1) * (string[(o+1):c] + " + ") + string[(o+1):c] + string[(c+1):]

    #trim out the 10x, 2x, xcetera
    string = re.sub(r'\d+x',"",string)

    for step in string.split("+"):
        step = step.strip()
        total_time = total_time + int(re.findall(r'\d+', step)[-1]) * paces[step[-1]]

    return total_time

if __name__ == "__main__":
    #simple set of paces for now
    paces = { 
        "E": 7,
        "T": 5,
        "M": 5.5
    }

    print(time_eval("2E + 10x(1T) + 2x(1E)", paces))