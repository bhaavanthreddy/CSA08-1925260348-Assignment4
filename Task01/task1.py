def process_mess_bill(filename):
    total = 0.0
    report = []
    rejected_lines = []

    with open(filename, "r") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                parts = line.split(",")

                if len(parts) != 3:
                    raise ValueError("Invalid number of fields")

                name = parts[1]
                amount = float(parts[2])

                total += amount
                report.append(name + " " + str(amount))

            except ValueError:
                rejected_lines.append((line_number, line))

    print("Report")
    print("------")

    for item in report:
        print(item)

    print("Total:", total)

    print("\nRejected Lines")
    print("--------------")

    for item in rejected_lines:
        print(item)


process_mess_bill("mess_oct.txt")
