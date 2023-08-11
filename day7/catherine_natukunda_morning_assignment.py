#context manager
#multithreading and multiprocessing
#context manager is an object that defines a temporary context for  a block of code
"""help avoid commomn errors
implement common patterns like transactions
help to ensure resources are released properly
make code conscious and consistent
"""
"""
#example1 to open a file and return a context manager instance
def open_file(filename):
    #this will open a file and return a context manager instance
    file = open(filename,'r')

    def __enter__():
       return file
    def __exit__(self, exc_type, exc_value,exc_tb):
        file.close()   

        return __enter__.__exit__
#with helps close a file
with open_file('my_file.txt') as f:
    contents = f.read() 
"""
"""
#ex2 demonstrate context manager using time series
import time
class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time-self.start_time
        print(f"the time for execution{execution_time} seconds elapsed")

#with example usage
with Timer():
  # measure the execution time
  time.sleep(2)

#miltithreading and multiprocessing used to imoprove performance of a python program
# two techniques used to improve the performance of a python program
# 1 Mltitreading is a technique where multiple threads are created within a single process
# 2 multiprocessing is a technique where multiple threads are created .(independent task)

#example3 of multithreading
import threading

def task(name):
    print(f"running task{name}")

#create multiple threads
threads =[]
for i in range (10):
   t = threading.Thread(target = task, args=(f"thread{i}",))   
   threads.append(t)
   t.start()

#wait for all threads to finish before it joins
for t in threads:
    t.join()


# example4 multiprocessing    
import multiprocessing

def process_task(name):
    print(f"processing task{name}")

    #create a pool of proceses
pool = multiprocessing.Pool(processes=5)

    #submit multiple task to the pool
for i in range(2):
    pool.apply_async(process_task,args =(f"process{i}",))
#close the pool and wait for all process to finish
pool.close()
pool.join()

#example5       
#multiprocessing and multithreading
import threading
import multiprocessing

def task (name):
    print(f"running task {name} on thread {threading.current_thread().name} withprocess {multiprocessing.current_process().name}")

#create multiple threads
treads = []
for i in range(4):
    t = threading.Thread(target=task,args=(f"thread{i}",))
    t.start()

    #create a wait for all threads to finish
for t in threads:
    t.join()  
"""
#Assignment A7:
#1a) Show a context manager for file handling that automatically opens and closes a file.

"""
class FileHandler:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
#for opening a file and returning it
    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file
#for closing a file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Example usage
file_path = 'example.txt'

# Writing to the file using the context manager
with FileHandler(file_path, 'w') as file:
    file.write('my name is Catherien Natukunda!')

# Reading from the file using the context manager
with FileHandler(file_path, 'r') as file:
    contents = file.read()
    print(contents)
"""

"""
#b) Shows a context manager for managing a database connection.

import mysql.connector

#class as context manager
class DatabaseConnection:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

#establishes the database connection and returns the objects
    def __enter__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )
        return self.connection
#responsible for closing the connection when the context is exited regardless of whether an exception occurs or not
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

# Example usage
host = 'localhost'
username = 'root'
password = ''
database = 'Cathy'

# Executing SQL queries using the context manager
with DatabaseConnection(host, username, password, database) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Courses (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

# Performing database operations using the context manager
with DatabaseConnection(host, username, password, database) as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name) VALUES (%s)", ('BSSE',))
    conn.commit()

    cursor.execute("SELECT * FROM employees")
    results = cursor.fetchall()
    for row in results:
        print(row)
"""

#c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.
import multiprocessing
import threading
import time

# Function to execute in threads
def thread_task(name, duration):
    start_time = time.process_time()
    print(f"Thread '{name}' started")
    time.sleep(duration)
    end_time = time.process_time()
    execution_time = end_time - start_time
    print(f"Thread '{name}' finished in {execution_time} seconds")

# Function(task be executed) to execute in processes
def process_task(name, duration):
    start_time = time.process_time()
    print(f"Process '{name}' started")
    
    # Create threads within the process
    threads = []
    threads.append(threading.Thread(target=thread_task, args=(f"{name}-Thread1", duration)))
    threads.append(threading.Thread(target=thread_task, args=(f"{name}-Thread2", duration)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.process_time()
    execution_time = end_time - start_time
    print(f"Process '{name}' finished in {execution_time} seconds")

#to ensure the multiprocessing  code is executed correctly
if __name__ == '__main__':
    # Create and start multiple processes
    processes = []
    processes.append(multiprocessing.Process(target=process_task, args=("Process 1", 3)))
    processes.append(multiprocessing.Process(target=process_task, args=("Process 2", 5)))

    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All processes finished")
