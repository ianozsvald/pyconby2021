import time
import pandas as pd

from config import COLUMNS, RAW_DATA, PICKLE, PICKLE_PROT4

# 4.4GB input
print(f"Reading csv from {RAW_DATA}")
df = pd.read_csv(RAW_DATA, names=COLUMNS, parse_dates=['date'])

print(f"Writing to {PICKLE}")
t1 = time.time()
df.to_pickle(PICKLE, protocol=-1)
print(f"Took {time.time()-t1:0.1f}s to write with HIGHEST_PROTOCOL")

# no obvious speed changes for r or w
#print(f"Writing to {PICKLE_PROT4} with protocol 4")
#t1 = time.time()
#df.to_pickle(PICKLE_PROT4, protocol=4)
#print(f"Took {time.time()-t1:0.1f}s to write with protocol 4")
