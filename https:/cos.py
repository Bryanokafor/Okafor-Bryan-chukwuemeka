scores = [70, 60, 50, 40]

for score in scores:
    if 90 <= score <= 100:
        print(f"Score: {score}, Grade: A")
    elif 80 <= score < 90:
        print(f"Score: {score}, Grade: B")
    elif 70 <= score < 80:
        print(f"Score: {score}, Grade: C")
    elif 60 <= score < 70:
        print(f"Score: {score}, Grade: D")
    else:
        print(f"Score: {score}, Grade: F")
