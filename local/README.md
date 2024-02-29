# Delta Lake locally Project

Why Delta format?

Delta under the hood is parquet files
with a transaction log in the form of a table.

The transaction log is a table that contains all the changes made to the data.

Parquet files are immutable, so to update a file, a new file is created and the transaction log is updated.

The advantage of Parquet files is that they are columnar, which allows for efficient reads and writes.

This allows for ACID transactions, schema evolution, and time travel.

# Data Maturity Model

Our data hierarchy of needs has 5 levels:

1. Data Collection
2. Data Wrangling
3. Data Integration
4. BI and Analytics
5. Artificial Intelligence

## Data Collection

Data Collection is the process of gathering data from different sources.

Now, data can come in different formats and in different ways.

Data can come in the forms, such as:

- Structured Data
- Semi-Structured Data
- Unstructured Data

## Data Wrangling

Collected data will be loaded into a staging area, not to forget that the extracted data
is likely not be clean.

And so in this step, we will need to focus on improving the data quality.
Soma common situations that make data dirty are:

- Missing Values
- Duplicate Values
- Inconsistent Values
- Incorrect Values
- Incomplete Values
- Outliers
- Invalid Values
- Inaccurate Values
- Inappropriate Values

...

The goal of the transform phase is converting data from its operational source format into a format that is suitable for analysis.

## Data Integration

Data integration, this step is all about writing our transform data from the staging area to a target
database where the analytics workloads will be performed.


We can do loading two ways by doing a refresh a.k.a. rewriting the data completely, which will replace
our old data.

Or we can do an update where only the changes we apply to the source data will be added to the data
warehouse.

# ETL and ELT

ETL stands for Extract, Transform, Load.

What do you think, how much did of one megabyte hard drive would have cost you back in 1967?

Well, the answer is one million dollars.

Of course, like throughout the decades, the cost of storage and computation has have decreased and
so did the way data engineers handled data integrations.
If you think about it, when storage is expensive, you were serious to consider what data you will
persist in your database.
Back then, data engineers face a ton of issues we could not just scale up and down as we do today.

**And since storage and compute resources were scarce, it made perfect sense to do the transformations
outside of the database in a staging area. That's why ETL was the widespread and traditional approach**.

However, it is not all fun and shiny to just bring a few example issues out of many we detail.
If there's a change in the schema, then your model is broken or if you think about
data velocity, it changes over time, and scaling is not exactly an easy task.

Or if you want to extract from another source, it takes time to add new data connections, not to mention
the horror that comes with testing and debugging an ETL.

Now, ELT stands for Extract, Load, Transform. It is the solution to the problems we just mentioned.
The world has changed and storage costs like two cents these days for every one GB
of data. So it was logical to reorganize the traditional ETL workflow.

Since today's computation and storage resources are super cheap, there is no harm in loading raw data
from sources stamps right into the destination.
Data warehouses like Snowflake Redshift and BigQuery are extremely scalable and performant, so it makes
sense to do two transformations inside the database rather than external processing layer.

We can handle issues with upstream schemas and downstream data models that would have been rather rather
hard with the traditional meteor approach where transformations were done in between the load and extraction
stages.

# Minio Data Lake

Minio is an open source object storage server that is compatible with Amazon S3 cloud storage service.
Minio is a high performance distributed object storage server, designed for large-scale private cloud infrastructure.

To access Minio, go to http://localhost:9000 and use the access key and secret key to login.

## Create a bucket

To create a bucket, click on the + icon and enter the name of the bucket.

Features:
* Versioning: Keep multiple versions of an object in the same bucket.
* Object Locking: Prevent objects from being deleted or modified for a fixed amount of time.
* Quota: Set a quota on the bucket to limit the amount of data that can be stored in the bucket.
* Retention: Set a retention period for the objects in the bucket. There are two types of retention: Compliance and Governance.
    * Compliance: Objects cannot be deleted or modified for a fixed amount of time.
    * Governance: Objects cannot be deleted or modified for a fixed amount of time, but the retention period can be extended.
  

