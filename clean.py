with open("data.csv", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        print(line)
        if len(line.split(",")) == 15:
            with open("data_cleaned.csv", "a") as n:
                n.write(line + "\n")
