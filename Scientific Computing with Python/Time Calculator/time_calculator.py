def add_time(starting_time, duration, starting_day=False):
    # List of days to help track the starting day and calculate the final day
    day_list = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]

    # Initialize day_count to track the number of days passed
    day_count = 0

    # Extract hours, minutes, and period (AM/PM) from the starting time
    start_hours, start_mins = starting_time.split(":")
    start_mins, period = start_mins.split(" ")
    period = period.strip().lower()

    # Extract hours and minutes from the duration
    add_hours, add_mins = duration.split(":")

    # Initialize total_hours and total_mins to calculate the new time
    total_hours = 0
    total_mins = int(start_mins) + int(add_mins)

    # Adjust total_mins and update total_hours if necessary
    if total_mins >= 60:
        total_hours += 1
        total_mins -= 60

    # Format total_mins with leading zero if less than 10
    if total_mins < 10:
        total_mins = f"0{total_mins}"

    # Update total_hours based on the starting period
    if period == "am" or (period == "pm" and total_hours == 12):
        total_hours += int(start_hours)
    elif period == "pm" or (period == "am" and total_hours == 12):
        total_hours += int(start_hours) + 12

    # Add hours from the duration to total_hours
    total_hours += int(add_hours)

    # Handle cases where total_hours exceeds 24
    while total_hours >= 24:
        total_hours -= 24
        day_count += 1

    # Format the new time with AM/PM and 12-hour clock
    if total_hours >= 12:
        if total_hours != 12:
            total_hours -= 12
        new_time = f"{total_hours}:{total_mins} PM"
    elif total_hours <= 11:
        if total_hours == 0:
            total_hours += 12
        new_time = f"{total_hours}:{total_mins} AM"

    # If starting_day is provided, calculate the final day
    if starting_day:
        starting_day = starting_day.lower()
        final_day = 0

        # Find the index of the starting_day in the day_list
        for day in day_list:
            if starting_day == day.lower():
                break
            final_day += 1

        # Update final_day based on day_count
        final_day += day_count

        # Handle cases where final_day exceeds 7
        while final_day >= 7:
            final_day -= 7

        # Get the current_day based on the final_day
        current_day = day_list[final_day]

        # Append the day information to the new_time
        new_time += f", {current_day}"

    # Append information about the number of days if day_count is greater than 0
    if day_count > 0:
        if day_count == 1:
            new_time += " (next day)"
        else:
            new_time += f" ({day_count} days later)"

    # Return the formatted new_time
    return new_time
