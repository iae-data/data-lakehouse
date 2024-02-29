import pandas as pd
import uuid
from datetime import datetime
import random
from deltalake.writer import write_deltalake


class FileWriter:
    def __init__(self, path: str):
        self.path = path

    @staticmethod
    def random_table_generator(n_rows: int):
        data = []
        for _ in range(n_rows):
            data.append({
                "id": str(uuid.uuid4()),
                "value": round(random.randint(0, 1000)),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        return pd.DataFrame(data)

    def write(self, df: pd.DataFrame):
        if df.empty:
            print("Dataframe is empty. Generating a random df.")
            df = self.random_table_generator(10)
        write_deltalake(self.path, df)
        print(f"Data written to {self.path}")
