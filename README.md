<div align="center">
    <img alt="Galois Logo" src="./assets/galois.png" alt="Logo" width="400">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
 
A **simple document store** that can store, retrieve, and query JSON documents using a custom query language.

[🎯 Features](#-features) •
[⚙️ Installation](#️-installation) •
[⚡️ Quickstart](#️-quickstart) •
[🤖 Benchmarks](#-benchmarks) •
[🏈 Gameplan](#-gameplan)


</div>

## 🎯 Features
---
This project is part of the application of my learnings from chapters 2 and 3 of the  book [Designing Data-Intensive Applications](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/):

* Data store supporting collections of JSON documents
* CRUD operations for collections and JSON documents
* Custom query language to search and filter documents based on their properties **(Coming Soon)**
* Custom storage engine based on LSM Trees **(Coming Soon)**

## ⚙️ Installation
---
This project is setup as a python package.
```bash
# install from source
git clone git@github.com:joaoflf/galois.git
cd galois 
pip install .
```

## ⚡️ Quickstart
---
```python
from galois.database import Database
from galois.collection import Collection

# more to come
```

## 🤖 Benchmarks
---
## 🏈 Gameplan
---
* Implementing CRUD (Create, Read, Update, Delete) operations for JSON documents and collections ✅
* Design custom query language to search and filter documents based on their properties 🔄 
* Implement query language using Abstract Syntax Trees (AST) 📭
* Implement custom storage engine based on LSMTrees 📭