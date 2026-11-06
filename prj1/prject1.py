# p1_bracket.py
# ENG 1112 Project 1: read the class test data and print a short report.
# The file has one row per load step, sorted by team:
#   team,step,cum_mass_g,status,mode,members,bracket_mass_g,note
# The report has four parts:
#   1. Maximum sustained load per team, in newtons.
#   2. Class average of those maxima.
#   3. Count of failures by mode code.
#   4. A flag for every team below the safety threshold.

file_name = input("Data file: ")
threshold = float(input("Threshold (N): "))

file = open(file_name)
header = file.readline()

previous_team = ""
team_max = 0.0
total = 0.0
count = 0
js = 0
mb = 0
mf = 0
ms = 0
pd = 0
dl = 0
nf = 0

for line in file:
    line = line.strip()
    if line == "":
        continue

    parts = line.split(",")
    if len(parts) < 5:
        continue
    team = parts[0].strip()
    mass = float(parts[2])
    status = parts[3].strip().upper()
    mode = parts[4].strip().upper()

    # The team changed: the previous team is finished.
    # First row has previous_team empty, so it never triggers this.
    if previous_team != "" and team != previous_team:
        print(previous_team + ": " + format(team_max, ".2f") + " N")
        total = total + team_max
        count = count + 1
        if team_max < threshold:
            print("FLAG " + previous_team + ": below threshold by "
                  + format(threshold - team_max, ".2f") + " N")
        team_max = 0.0

    if status == "HELD":
        # Only HELD rows count toward the maximum.
        # Grams to newtons: mass / 1000 * 9.81.
        # A mode written on a HELD row is not a failure, so it is ignored.
        load = mass / 1000 * 9.81
        if load > team_max:
            team_max = load
    else:
        # A FAILED or CAPPED row: count its failure mode.
        # A CAPPED bracket always counts as NF, whatever the mode column says.
        if status == "CAPPED":
            nf = nf + 1
        elif mode == "JS":
            js = js + 1
        elif mode == "MB":
            mb = mb + 1
        elif mode == "MF":
            mf = mf + 1
        elif mode == "MS":
            ms = ms + 1
        elif mode == "PD":
            pd = pd + 1
        elif mode == "DL":
            dl = dl + 1
        elif mode == "NF":
            nf = nf + 1

    previous_team = team

file.close()

# The last team has no next team to trigger it, so finish it here.
# Same five actions as the team change above.
# (If the file had no data rows, previous_team is still empty: skip.)
if previous_team != "":
    print(previous_team + ": " + format(team_max, ".2f") + " N")
    total = total + team_max
    count = count + 1
    if team_max < threshold:
        print("FLAG " + previous_team + ": below threshold by "
              + format(threshold - team_max, ".2f") + " N")

# Class average: one division at the end of an accumulation loop.
if count > 0:
    average = total / count
    print("Class average: " + format(average, ".2f") + " N")

# One line per mode code that appears at least once.
if js > 0:
    print("JS: " + str(js))
if mb > 0:
    print("MB: " + str(mb))
if mf > 0:
    print("MF: " + str(mf))
if ms > 0:
    print("MS: " + str(ms))
if pd > 0:
    print("PD: " + str(pd))
if dl > 0:
    print("DL: " + str(dl))
if nf > 0:
    print("NF: " + str(nf))