def add_time(start, duration, week_day= ""):

    d_hour = None
    s_hour = None
    d_minute = None
    s_minute = None
    s_period = None
    index = None
    new_hour = None
    md = 0 # Decimal minute
    mu = 0 # Unity minute
    count = 0
    days_count = 0
   

    
    days_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  
    # Get hour, minutes and time period from the starter hour
    index = start.find(":") # Find the column
    s_hour = int(start[:index]) # Get the hour
    s_minute = start[index+1:index+3] # Get the minutes
    s_period = start[index+4:].lower() # Get AM/PM


    # Splits minutes in two digits to avoid bugs =)
    md = s_minute[0]
    mu = s_minute[1]

    # Converting to int, so we can do some math
    md = int(md)
    mu = int(mu)
   

    # Get hour, minutes and time period from the duration 
    index = duration.find(":") 
    d_hour = int(duration[:index])
    d_minute = int(duration[index+1:index+3])
   
    # Calculating the minutes
    for i in range(1, d_minute+1):
      mu +=1 
      if mu == 10: 
        mu = 0
        md += 1
        if md == 6:
          md = 0
          s_hour += 1


    # Calculating the hours
    for i in range(1, d_hour+1):
        s_hour += 1
        if s_hour == 13:
          s_hour = 1
          
          if s_period == "am":
            s_period = "pm"
          else:
            s_period = "am"
            days_count += 1
            
    # Find the day of week informed by user
    if week_day != "":
      for i in range(len(days_week)):
        if days_week[i] == week_day:
          count = i

    # Find new week day
    for i in range(1, days_count+1):
      count += 1
      if count == 7:
        count = 0

    # Is showing how many days have passed?
    if days_count == 0:
      days_count = ""
    elif days_count == 1:
      days_count = "(next day)"
    else:
      days_count = "("+str(days_count) + " days later)"

    # Show day of the week if optional argument was informed
    if week_day != "":
      new_hour = str(s_hour)+":" + str(md) + str(mu) + " " + s_period.upper() + " " + days_count + " " + days_week[count]
    else:
      new_hour = str(s_hour)+":" + str(md) + str(mu) + " " + s_period.upper() + " " + days_count
    return new_hour
   

hour = add_time("11:30 PM", "100:00")

print(hour)
