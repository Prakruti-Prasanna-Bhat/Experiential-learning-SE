BERTHS = ["SU", "LB", "MB", "UB", "LB", "MB", "UB", "SL"]

def parse_pnr(pnr):
    if not isinstance(pnr, str):
        return None
    if len(pnr) != 10 or not pnr.isascii() or not pnr.isdigit():
        return None
    return int(pnr[0]), int(pnr[1:])

def journey_distance(distances_csv):
    if not isinstance(distances_csv, str):
        return None

    try:
        distances = [int(d.strip()) for d in distances_csv.split(',')]
    except ValueError:
        return None

    if len(distances) < 2:
        return None

    if any(d < 0 for d in distances):
        return None

    if any(distances[i] > distances[i + 1]
           for i in range(len(distances) - 1)):
        return None

    return distances[-1] - distances[0]

def berth_type(seat):
    if not isinstance(seat, str):
        return None

    parts = seat.split('-')

    if len(parts) != 2:
        return None

    coach, number = parts

    if not coach.strip() or not number.isascii() or not number.isdigit():
        return None

    seat_number = int(number)

    if seat_number <= 0:
        return None

    return coach.upper(), BERTHS[seat_number % 8]

def main():
    print("==== Running parse_pnr ====")
    user_input = input("Enter a 10 digit PNR (e.g. 4521367890): ")
    result = parse_pnr(user_input)
    print("Zone and Number:", result)

    print("\n==== Running journey_distance ====")
    user_input = input("Enter station distances as CSV (e.g. 0,120,340): ")
    result = journey_distance(user_input)
    print("Total Distance:", result)

    print("\n==== Running berth_type ====")
    user_input = input("Enter coach and seat (e.g. S3-45): ")
    result = berth_type(user_input)
    print("Coach and Berth:", result)

if __name__ == "__main__":
    main()
