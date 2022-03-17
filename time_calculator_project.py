def add_time(start, duration, start_day=None):
    
    start = start.split()
    duration = duration.split(":")
    week_days = {"monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":0 }
    if start_day != None : start_day = start_day.lower()

    #looking for input errors
    if len(start) != 2 or duration[1] > "59" :
        print("Error: Invalid input")
        exit()
    if start[1] != "AM" and start[1] != "PM" :
        print("Error: Invalid input")
        exit()
    if start_day!=None and start_day not in week_days :
        print("Error: Invalid input")
        exit()

    start_hr = start[0].split(":")
    start_hr,start_min = start_hr
    duration_hr,duration_min = duration

    raw_min = int(start_min) + int(duration_min)   #sums hours and minutes and arranges them based on a 12hr clock
    final_min = raw_min % 60    
    q_min = raw_min // 60

    raw_hr = int(start_hr) + int(duration_hr) + q_min
    final_hr = raw_hr % 12
    if final_hr == 0 : final_hr = 12
    q_hr = raw_hr // 12

    final_day = ""              #extracts the value of the start_day from a range of 1-7 for later calculation
    if start_day != None :
        for k,v in week_days.items() :
            if k == start_day : x = v
    else: x=0
    frame = start[1]    #sets AM or PM based on odd and even numbers and states how many days have passed from start to end
    day_prompt = ""     # also sets x to be able to calculate which day of the week the final day is, based on a 1-7 number range
    if q_hr % 2 == 1 :
        if frame == "AM" :
            frame = "PM"
        else :
            frame = "AM"
            day_prompt = " (next day)"
    if q_hr == 2 :
        day_prompt = " (next day)"
    if q_hr > 2 :
        n = q_hr // 2
        if n % 2 == 0:
            day_prompt = f" ({n} days later)"
            x += n
        else :
            if start[1] == "PM" : 
                day_prompt = f" ({n + 1} days later)"
                x += n+1
            elif q_hr == 3 :
                day_prompt = " (next day)"
            elif start[1] == "AM" : 
                day_prompt = f" ({n} days later)"
                x += n
    if day_prompt == " (next day)" : x += 1
    if start_day != None :
        for k,v in week_days.items():
            if v == x % 7 : final_day = f", {k.title()}"
    frame = " " + frame
    new_time = f"{final_hr}:{final_min:02}{frame}{final_day}{day_prompt}"
    return new_time