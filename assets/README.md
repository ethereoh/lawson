# Folder structure of each modules

Each module requires at least these dirs: `api`, `routes`, `schemaa`, `dal`, and `utils`. 

- `api`: defining logic of business.
- `routes`: defining methods for using those defined `api` (GET, POST, etc. ). 
- `schemas`: defining object's schemas. 
- `dal`: stands for `data access layer`, in charge of control the data communication, including managing connection to database, transfering data via Queue, Stream, etc. 
- `utils`: used for defining methods that are not direc

Note: 

- The main difference between `api` and `routes` is `api` handling logic, functions that related to requirements, meanwhile, `routes` will handling logics that are related to http/https protocols.

    

# notebooks

Intstructions for using each modules seperately


# data samples

1. Test dataset: [link](https://www.kaggle.com/datasets/iuliabunescu23/gdpr-qa-test-dataset)


