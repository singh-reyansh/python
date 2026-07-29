# 

from datetime import datetime
from datetime import date
from datetime import time
now = datetime.now()
# print(now)

# print(now.date())
# print(now.time())
# print(now.year)

# d = date(2025,4,21)
# print(d)
# t =time(10,15,20)
# print(t)


print(now.strftime("%Y %M %D"))


# Scenario --