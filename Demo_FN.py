

from datetime import datetime


Day_data = 1736960280000
Day_Compare = 0

def GetDateFormTimesteam(ts):
      date_time = datetime.fromtimestamp(ts / 1000)
      formatted_date = date_time.strftime("%d/%m/%Y 00:00:00")
      parsed_date = datetime.strptime(formatted_date, "%d/%m/%Y %H:%M:%S")
      return  int(parsed_date.timestamp() * 1000)

def check_Day(data,nexDay):
      global Day_Compare
      if nexDay == 0:
            Day_Compare = GetDateFormTimesteam(data)+ 24*60*60*1000
            return False
            
      checkday =  GetDateFormTimesteam(data)
      if checkday >= Day_Compare:
            print(f'>>> {checkday} >= {Day_Compare}')
            Day_Compare = checkday + 24*60*60*1000
            return True
      else:
            return False
      
#timestamp_ms = [
#1736873880000
#,1736873940000
#,1736874000000
#,1736874060000
#,1736874120000
#]
#
#for day in timestamp_ms:
#      
#      optimized_timestamp_ms = check_Day(day,Day_Compare)
#      if optimized_timestamp_ms:
#            print(f"Ok Nexdays:{optimized_timestamp_ms}")
#            
#      print("Converted date (optimized)+7:", optimized_timestamp_ms+s)
#      print("Converted date (optimized):", optimized_timestamp_ms)



