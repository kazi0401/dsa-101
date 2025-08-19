# Your implementation here
class MyHashMap:
    #INSANELY CONFUSED
    def __init__(self, capacity: int):
        self.data = [None] * capacity # list[tuple[any, any]]
        self.capacity = capacity
        self.sz = 0
    
    def put(self, key, value):
        self.sz += 1
    
    def get(self, key):
        pass
    
    def remove(self, key):
        index = hash(key) % self.capacity

        if self.data[index] == None:
            return 
        else:
            self.data[index] = None
            self.sz -= 1
    
    def resize(self):  # O(n)
        newCapacity = self.capacity * 2
        newData = [None] * newCapacity

        for item in self.data:
            if item != None:
                key, value = item 
                newIndex = hash(key) % newCapacity
                newData[newIndex] = (key, value)
        
        self.data = newData 
        self.capacity = newCapacity


    def hash(self, key):
        pass 
    
    def size(self):
        return self.sz

    def capacity(self):
        pass

    def load_factor(self):
        pass

if __name__ == '__main__':
    # Use this for any experiments you want to run
    pass 
