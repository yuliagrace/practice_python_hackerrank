def is_leap(year):
    leap = False
    
    if year % 4 == 0:
      return True
    elif year % 100 == 0:
      return False
    else:
      return leap

year = int(input())
