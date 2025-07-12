

"""
Hashtable = A data structure that stores unique keys to values ex.<Integer, String>
Each key/value pair is known as an Entry
FAST insertion, look up, deletion of key/value pairs
Not ideal for small data sets, great with large data sets

hashing = Takes a key and computes an integer (formula will vary based on key & data type)
In a Hashtable, we use the hash % capacity to calculate an index number

key.hashCode() % capacity = index

bucket = an indexed storage location for one or more Entries
can store multiple Entries in case of a collision (linked similarly a LinkedList)

collision = hash function generates the same index for more than one key
less collisions = more efficiency

Runtime complexity: Best Case O(1)
Worst Case O(n)
"""


def hash_function(key, capacity):
    """ Computes the hash index for a given key. """
    return hash(key) % capacity


class HashTable:
    """ A simple implementation of a hash table. """
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        # Initialize buckets as empty lists
        self.buckets = [[] for _ in range(capacity)]

    def insert(self, key, value):
        """ Inserts a key-value pair into the hash table. """
        index = hash_function(key, self.capacity)
        bucket = self.buckets[index]

        # Check if the key already exists and update it
        for entry in bucket:
            if entry[0] == key:
                entry[1] = value
                return

        # If the key does not exist, append a new entry
        bucket.append([key, value])
        self.size += 1

    def get(self, key):
        """ Retrieves the value associated with a given key. """
        index = hash_function(key, self.capacity)
        bucket = self.buckets[index]

        for entry in bucket:
            if entry[0] == key:
                return entry[1]

        return None  # Key not found

    def delete(self, key):
        """ Deletes a key-value pair from the hash table. """
        index = hash_function(key, self.capacity)
        bucket = self.buckets[index]

        for i, entry in enumerate(bucket):
            if entry[0] == key:
                del bucket[i]
                self.size -= 1
                return True

        return False  # Key not found

    def __str__(self):
        """ Returns a string representation of the hash table. """
        return str(self.buckets)


# Example usage
ht = HashTable()
ht.insert("name", "Alice")
ht.insert("age", 30)
ht.insert("city", "New York")
# Update existing key
ht.insert("name", "Bob")

print("Hash Table:", ht)

print("Get 'name':", ht.get("name"))
print("Get 'age':", ht.get("age"))

ht.delete("age")
print("After deleting 'age':", ht)

print("Get 'age' after deletion:", ht.get("age"))
