import re

def time_eval(string, paces):
    total_time = 0

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

    #res = re.findall(r'\d+', "5T")
    #print(res[-1])
    print(time_eval("2E + 10T + 2M", paces))