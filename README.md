<div align="center">
    <img alt="Galois Logo" src="./assets/galois.png" alt="Logo" width="400">
</div>
<div align="center">
    <img alt="python badge" src="https://img.shields.io/badge/python-3.10-blue.svg">
    <img alt="build badge" src="https://github.com/joaoflf/galois/actions/workflows/build.yml/badge.svg">
    </br></br>

A **simple document store** that can store, retrieve, and query JSON documents using a custom query language.

[🎯 Features](#-features) •
[⚙️ Installation](#️-installation) •
[⚡️ Quickstart](#️-quickstart) •
[🔤 Query Language](#-query-language) •
[🤖 Benchmarks](#-benchmarks) •
[🏈 Gameplan](#-gameplan)


</div>

&nbsp;

## 🎯 Features

This project is part of the application of my learnings from chapters 2 and 3 of the  book [Designing Data-Intensive Applications](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/):

* Data store supporting collections of JSON documents
* CRUD operations for collections and JSON documents
* Custom query language to search and filter documents based on their properties
* Custom storage engine based on LSM Trees **(Coming Soon)**
* Data stored in a binary encoding similar to Avro
 
&nbsp;

## ⚙️ Installation

This project is setup as a python package.
```bash
# install from source
git clone git@github.com:joaoflf/galois.git
cd galois 
pip install .
```

&nbsp;

## ⚡️ Quickstart

```python
from galois.database import Database
from galois.collection import Collection

db = Database("music_library")
tracks = db.get_collection("tracks")

query = "(AND (NOT duration_ms=120000) (OR tempo<120 key>4))"
db.get_collection("tracks").find(query)

```

&nbsp;

## 🔤 Query Language
A simple, yet powerful, language designed to query JSON documents. The syntax is inspired by Lisp and offers logical `AND`, `OR`, and `NOT` operations, as well as comparison operators `=`, `<`, and `>`.

### Logical Expressions
Logical expressions are used to combine other expressions with a logical operator: AND, OR, or NOT.

The syntax is as follows:
```
(OPERATOR EXPRESSION1 EXPRESSION2 ...)
````

Example:
```
(AND (OR name=John name=Jane) age=30)
```

### Comparison Expressions
Comparison expressions are used to compare a field in the document with a value.

The syntax is as follows:
```
field OPERATOR value
```

Example:
```
age>30
```

### Semantics

* `AND`: All of the expressions must be true.
* `OR`: At least one of the expressions must be true.
* `NOT`: The expression must be false.
* `=`: The field in the document must equal the value.
* `<`: The field in the document must be less than the value.
* `>`: The field in the document must be greater than the value.

&nbsp;

## 🤖 Benchmarks


We used a dataset containing nearly 600k Spotify tracks to perform various benchmarks. This dataset can be found on [Kaggle](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks?select=tracks.csv).

For simplicity, only the `artists`, `name`, `loudness`, `duration_ms`, `key`, and `tempo` columns were selected from the dataset.

## Document Insertion

**Task**: Create and write 586,672 documents to disk, including unique ID generation.

**Time taken**: 95,291 ms

## Querying

**Task**: Perform the following query and return matching documents:
```
(AND (NOT duration_ms=120000) (OR tempo<120 key>4))
```
**Time taken**: 15,547 ms

&nbsp;

## 🏈 Gameplan

* Implementing CRUD (Create, Read, Update, Delete) operations for JSON documents and collections ✅
* Implement a unique id generator similar to MongoDB ✅
* Design custom query language to search and filter documents based on their properties ✅
* Implement query language parser to an Abstract Syntax Tree (AST) ✅
    * Implemented a rudimentary parser based on regexes because the focus of the project is data management. In the future could use a context-free grammar parser like Bison
* Implement the AST executor ✅
* Perform some load benchmarks ✅
* Implement custom storage engine based on LSMTrees 🔁
* Implement a rough version of the Avro binary encoding 📥
* Have Galois use this Avro encoding 📥
