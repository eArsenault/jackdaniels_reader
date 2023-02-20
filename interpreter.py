import re

def convert_pace(paces):
    system = paces.pop("sys")

    paces_value = paces
    for k, time in paces_value.items():
        time_min, time_sec = time.split(":")
        paces_value[k] = float(time_min) + float(time_sec)/60
    
    if system == "metric":
        paces_metric = paces_value
        paces_imperial = {k: v * 1.609 for k,v in paces_metric.items()}
    else:
        paces_imperial = paces_value
        paces_metric = {k: v / 1.609 for k,v in paces_imperial.items()}

    return paces_metric, paces_imperial

def time_eval(string, paces):
    total_time = 0
    pace_met, pace_imp = convert_pace(paces)

    #check for repeats - this can't handle nested parentheses for now
    #assume we are using natural numbers of reps
    while "(" in string:
        #find the first pair of parentheses
        o = string.find("(")
        c = string.find(")")
        #we want the last number before the open
        val = int(re.findall(r'\d+', string[:o])[-1])

        string = string[:o] + (val - 1) * (string[(o+1):c] + " + ") + string[(o+1):c] + string[(c+1):]

    #trim out the 10x, 2x, xcetera - no longer needed at this point
    string = re.sub(r'\d+x',"",string)

    for step in string.split("+"):
        step = step.strip()
        #finds either a whole number or number plus digit
        dist = float(re.search(r'(\d+\.\d*)|(\d+)', step)[0])
        #if dist >= 100, assume distance is metres
        if dist > 99:
            total_time = total_time + (dist/1000) * pace_met[step[-1]]
        elif step[-2] == 'k':
            total_time = total_time + dist * pace_met[step[-1]]
        else:
            total_time = total_time + dist * pace_imp[step[-1]]

    return total_time

if __name__ == "__main__":
    #use my paces for now
    paces = { 
        "E": "6:00",
        "T": "5:00",
        "M": "5:20",
        "I": "4:00",
        "R": "3:45",
        "J": "6:30",
        "sys": "metric"
    }

    print(time_eval("10.5kT + 2E", paces))