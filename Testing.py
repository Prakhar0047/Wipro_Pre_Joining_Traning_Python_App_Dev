from datetime import date as date_n
date1 = date_n(2025,12,23)
date2 = date_n(2022,2,23)

di = str(date1-date2)
dt_l = di.split()
print(dt_l)