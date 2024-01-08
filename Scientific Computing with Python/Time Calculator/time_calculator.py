def add_time(starting_time, duration, starting_day=False):
    day_list = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]
    day_count = 0

    start_hours, start_mins = starting_time.split(":")
    start_mins, period = start_mins.split(" ")
    period = period.strip().lower()
    add_hours, add_mins = duration.split(":")

    total_hours = 0
    total_mins = int(start_mins) + int(add_mins)

    if total_mins >= 60:
        total_hours += 1
        total_mins -= 60

    if total_mins < 10:
        total_mins = f"0{total_mins}"

    if period == "am" or (period == "pm" and total_hours == 12):
        total_hours += int(start_hours)
    elif period == "pm" or (period == "am" and total_hours == 12):
        total_hours += int(start_hours) + 12

    total_hours += int(add_hours)

    while total_hours >= 24:
        total_hours -= 24
        day_count += 1

    if total_hours >= 12:
        if total_hours != 12:
            total_hours -= 12
        new_time = f"{total_hours}:{total_mins} PM"
    elif total_hours <= 11:
        if total_hours == 0:
            total_hours += 12
        new_time = f"{total_hours}:{total_mins} AM"

    if starting_day:
        starting_day = starting_day.lower()
        final_day = 0
        for day in day_list:
            if starting_day == day.lower():
                break
            final_day += 1
        final_day += day_count
        while final_day >= 7:
            final_day -= 7
        current_day = day_list[final_day]
        new_time += f", {current_day}"

    if day_count > 0:
        if day_count == 1:
            new_time += " (next day)"
        else:
            new_time += f" ({day_count} days later)"

    return new_time
