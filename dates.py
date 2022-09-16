from dataclasses import dataclass
import datetime

x = datetime.datetime.now()
print(x.strftime('%B'))