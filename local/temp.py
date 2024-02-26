import pandas as pd
import os
from deltalake import DeltaTable
from deltalake.writer import write_deltalake


df = pd.DataFrame({"x": [1, 2, 3]})

print(df.head())

write_deltalake("tmp/some_delta_lake", df)

