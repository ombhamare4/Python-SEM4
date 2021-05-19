import pandas as pd
import matplotlib.pyplot as plt

sema=['Sem 1','Sem 2','Sem 3','Sem 4']
passa=[49,43,41,45]
# plt.plot(sema,passa)
passb=[43,46,44,40]
plt.plot(sema,passa,label='Sem A')
plt.plot(sema,passb,label='Sem B')
plt.legend(loc = 'best')