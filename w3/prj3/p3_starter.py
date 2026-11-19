# ENG 1112 - Project 3 - starter file
# Write the six functions marked "replace", then the three numbered steps in the loop at the bottom.
# Test with the replay file sample_readings.csv first, then with the Arduino.

import math
import os
import time
from linsolve import solve  # the Project 2 solver, see Part B of the guide

SENSOR_ANGLE = 40.0   # your personal angle, in degrees
ECHO_TIME_1 = 662   # your average echo time at 10 cm, in microseconds
ECHO_TIME_2 = 1662  # your average echo time at 30 cm, in microseconds

DISTANCE_1 = 10.0     # the two reference distances, in cm
DISTANCE_2 = 30.0
REST_ANGLE = 90       # servo angle when nothing is near
AWAY_ANGLE = 150      # servo angle that swings the arm away


def calibration(echo_time_1, echo_time_2):
    matrix = [[echo_time_1, 1, DISTANCE_1],[echo_time_2, 1, DISTANCE_2]]

    sol = solve(2, matrix)

    # Two echo times in microseconds go in. Build the augmented matrix of the 2 by 2 system
    # a * t + b = d  through the two reference points, solve it with solve(), and return
    # a (in cm per microsecond) and b (in cm).
    if sol is None:
        raise ValueError("Calibration echo times must be distinct")
    a = sol[0]
    b = sol[1]
    return a, b


def distance(echo_time, a, b):
    # The calibration line: an echo time in microseconds goes in, a distance in cm comes out.
    return a * echo_time + b


def rotation(angle_in_degrees):
    # An angle in degrees goes in. Returns the 2 by 2 rotation matrix [[cos, -sin], [sin, cos]]
    # as a list of two lists. Its entries have no units.
    angle_in_radians = math.radians(angle_in_degrees)
    c = math.cos(angle_in_radians)
    s = math.sin(angle_in_radians)
    return [[c, -s], [s, c]]


def dot_product(vector_1, vector_2):
    # Two vectors of equal size go in, one number comes out: the sum of the products of the
    # matching entries. Write it with a loop, so that it works for vectors of any size.
    total = 0.0
    for index in range(len(vector_1)):
        total += vector_1[index] * vector_2[index]
    return total


def apply(matrix, vector):
    # A matrix times a vector of compatible size: every row of the matrix has as many entries
    # as the vector. Returns a list with one number for each row, the dot product of that row
    # with the vector.
    result = []
    for row in matrix:
        result.append(dot_product(row, vector))
    return result


def sensor_to_bench(echo_time, a, b, rotation_matrix):
    # Compose: echo time in microseconds -> distance r in cm -> the vector [r, 0] in the sensor
    # frame -> bench frame. Returns the list [x, y], in cm.
    r = distance(echo_time, a, b)
    sensor_vector = [r, 0.0]
    return apply(rotation_matrix, sensor_vector)


def threshold_from_knob(knob):
    # The knob reading, 0 to 1023, becomes a threshold from 5 cm to 50 cm.
    return 5.0 + 45.0 * knob / 1023.0


def read_line(source, replay) -> str:
    # The next line of readings as text, or "" when there are no more.
    if replay:
        line = source.readline()
    else:
        line = source.readline().decode(errors="ignore")
    if isinstance(line, bytes):
        line = line.decode(errors="ignore")
    return line.strip()


def send(source, replay, command):
    # Send one command to the Arduino. In replay mode, print it instead.
    if replay:
        print("  ->", command)
    else:
        source.write((command + "\n").encode())



# a,b = calibration(ECHO_TIME_1, ECHO_TIME_2)
# print(sensor_to_bench(953, a, b, rotation(40)))

# here the main code starts
print("Replay file or port: ", end="")
name = input().strip()
if not name.endswith(".csv"):
    name += ".csv"
replay = os.path.isfile(os.path.join(os.path.dirname(__file__), name))
if replay:
    source = open(os.path.join(os.path.dirname(__file__), name))
    source.readline()  # the first line is the header, skip it
else:
    import serial  # the pyserial package, installed once with: pip install pyserial
    source = serial.Serial(name, 9600, timeout=5)  # give up after 5 seconds of silence
    time.sleep(2)  # the Arduino restarts when the port opens
    source.reset_input_buffer()
    source.readline()  # the first line may be cut in half, skip it

a, b = calibration(ECHO_TIME_1, ECHO_TIME_2)
rotation_matrix = rotation(SENSOR_ANGLE)
near = False

line = read_line(source, replay)
while line != "":
    parts = line.split(",")
    if len(parts) == 2:
        echo_time = float(parts[0])
        knob = float(parts[1])
        if echo_time > 0:  # the sensor reports 0 when nothing is in range
            position = sensor_to_bench(echo_time, a, b, rotation_matrix)
            print(position)

            threshold = threshold_from_knob(knob)
            if not near and position[0] < threshold - 3.0:
                near = True
                send(source, replay, "l1")
                send(source, replay, "s" + str(AWAY_ANGLE))
            elif near and position[0] > threshold + 3.0:
                near = False
                send(source, replay, "l0")
                send(source, replay, "s" + str(REST_ANGLE))
    if replay:
        time.sleep(0.05)
    line = read_line(source, replay)
source.close()
print("No more readings.")
