import mongoengine

def global_init():
    """
    Initializes the connection to the MongoDB database using MongoEngine.

    This function sets up a connection to a MongoDB database, allowing you to interact
    with the database in your application. The connection is registered with a specific alias 
    so it can be easily referenced later in your code.

    Parameters:
    - alias='core': A string that serves as an alias for this particular database connection.
                    You can use this alias ('core') to refer to the connection throughout your application.
                    
    - name='snake_bnb': The name of the MongoDB database to which you are connecting.
                        In this case, the database is named 'snake_bnb'.
    """
    mongoengine.register_connection(alias='core', name='snake_bnb')
