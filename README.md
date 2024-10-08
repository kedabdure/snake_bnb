# MongoDB Quickstart with Python course

Course materials for Talk Python's **free** MongoDB course.

Learn the most popular NoSQL / document database: MongoDB.
In just 2 hours, you'll be up and running with MongoDB and Python.

[![Course image](https://raw.githubusercontent.com/mikeckennedy/mongodb-quickstart-course/master/readme_resources/mongo-quickstart-logo-scaled.jpg)](http://freemongodbcourse.com/)

## Take the course

Are you ready to take the course? Visit the course website to get started.

[**freemongodbcourse.com**](http://freemongodbcourse.com/)

It's easy and 100% free.

## Course outline

- Why choose NoSQL and MongoDB?
- Modeling data in a document-database
- mongoengine ODM: Map classes to MongoDB
- Course wrap-up

## You have a free and paid course?

Wondering how this compares to our full, commercial [MongoDB for Python for Developers course](https://training.talkpython.fm/courses/explore_mongodb_for_python_developers_course/mongodb-for-python-for-developers-featuring-orm-odm-mongoengine)? This course is a brief introduction and 2.0 hours long. The full MongoDB course covers much more, in greater depth and is 7 hours of content.

Think of this course as the appetizer to prepare you for the main course. That said, the demo materials and majority of the content is unique to this course.

# MongoEngine

## MongoEngine

- is an Object-Document Mapper (ODM) for MongoDB in Python. Similar to how SQLAlchemy works with relational databases, MongoEngine allows developers to work with MongoDB in a more Pythonic way by mapping Python classes to MongoDB documents.

### Key Features of MongoEngine:

- Schema Definition: class to collection(Table in SQL case)
- Validation: Automatic validation based on the type of the field defined ing the schema, to ensure data being saved into MongoDb adheres to the expected structure.
- Querying: Provide a more pythonic way to query MongoDb
- Integration: integrate with python frameworks seamlessly like flask and Django

* When to Use MongoEngine:

- When you want to leverage MongoDB in a Python application but prefer an object-oriented approach.
- If your application benefits from defining clear data models with validation and relationships.

# PyMongo

- is essential when you need full control over database interactions or when you're working on a performance-critical application. It allows you to utilize the full power of MongoDB without any abstraction layer.

## Key feature of PyMongo

- Direct access
- Flexibility
- Performance

* When to Use PyMongo:
  When you need fine-grained control over your MongoDB interactions.
