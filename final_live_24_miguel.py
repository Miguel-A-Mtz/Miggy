# Final Exam as Group Project Summer 24

def data_prompt():
    print(f'\nUpdate Flight Status')
    print(f'\t1) Takeoff 2) Inflight  3) Landing 4) Exit')
    user_status = input("\tPlease enter the flight status from above: ")
    current_angle = 0
    if user_status != '4':
        current_angle = input("\tPlease enter the current flight angle: ")
    try:
        correct_angle = float(current_angle)
    except ValueError:
        correct_angle = -1
        print("\tThat is not a valid number")
    return user_status, correct_angle


def take_off_calculation(status, current_angle):
    to_min, to_max = 30, 45
    if to_min <= current_angle <= to_max:
        print(f"\tYou are in range which is {to_min:} to {to_max}--degrees.")
    elif current_angle < to_min:
        adjust_by = to_min - current_angle
        print(f"\tNose us by {adjust_by:.2f}--degrees to reach {to_min:2f}--degrees.")
    elif current_angle > to_max:
        adjust_by = current_angle - to_max
        print(f"\tNose down by {adjust_by:.2f}--degrees to reach {to_max:2f}--degrees.")
    save_flight_data(status, current_angle)
    return


def in_flight_calculation(status, current_angle):
    in_min, in_max = 4.1, 5.2
    if in_min <= current_angle <= in_max:
        print(f"\tYou are in range which is {in_min} to {in_max}--degrees.")
    elif current_angle < in_min:
        adjust_by = in_min - current_angle
        print(f"\tNose us by {adjust_by:.2f}--degrees to reach {in_min:2f}--degrees.")
    elif current_angle > in_max:
        adjust_by = current_angle - in_max
        print(f"\tNose down by {adjust_by:.2f}--degrees to reach {in_max:2f}--degrees.")
    save_flight_data(status, current_angle)
    return


def landing_calculation(status, current_angle):
    la_min, la_max = 12.0, 25.5
    if la_min <= current_angle <= la_max:
        print(f"\tYou are in range which is {la_min} to {la_max}--degrees.")
    elif current_angle < la_min:
        adjust_by = la_min - current_angle
        print(f"\tNose us by {adjust_by:.2f}--degrees to reach {la_min:2f}--degrees.")
    elif current_angle > la_max:
        adjust_by = current_angle - la_max
        print(f"\tNose down by {adjust_by:.2f}--degrees to reach {la_max:2f}--degrees.")
    save_flight_data(status, current_angle)
    return


def save_flight_data(status, current_angle):
    if current_angle == -1:
        current_angle = "Data not available"
    with open('flight_log.txt', 'a') as flight_log:
        flight_log.write(f"\n\tStatus {status}, FLight-Angle {current_angle}")
    return


def main():
    print(f'\nWelcome to the In-Flight Calculator')
    with open('flight_log.txt', 'w') as new_flight:
        new_flight.write(f"\nFlight at Terminal")
    status, angle = data_prompt()
    while status != '4':
        if status == '1':
           take_off_calculation(status, angle)
        elif status == '2':
           in_flight_calculation(status, angle)
        elif status == '3':
           landing_calculation(status, angle)
        elif status == '4':
           break
        else:
           print('Invalid entry')
        status, angle = data_prompt()
    with open('Flight_log.txt', 'a') as new_flight:
        new_flight.write(f"\nFlight has landed.")
    print(f'\nThank you for flying Python Airways')
    return


main()
