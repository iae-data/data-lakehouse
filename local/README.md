# Delta Lake locally

Why Delta format?

Delta under the hood is parquet files
with a transaction log in the form of a table.

The transaction log is a table that contains all the changes made to the data.

Parquet files are immutable, so to update a file, a new file is created and the transaction log is updated.

The advantage of Parquet files is that they are columnar, which allows for efficient reads and writes.

This allows for ACID transactions, schema evolution, and time travel.

