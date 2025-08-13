# Your implementation here
class MyHashMap:
    #INSANELY CONFUSED
    def __init__(self):
        self.capacity = 10
    def put(self, key, value):
        self[key] = value
        if self[key] is not None:
            self.capacity *= 2
            self.key += 1
    def get(self, key):
        if self.key not in self:
            pass
        else:
            return self.key
    def remove(self, key):
        if self.key not in self:
            pass
        else:
            del(self.key)
            del(self[key])
    def resize(self):
        self.capacity *= 2

    def size(self):
        self.count = 0
        for self.keys() in self:
            self.count += 1
        return self.count

    def capacity(self):
        return self.capacity_val

    def load_factor(self):
        return 1 - (self.count / self.capacity_val)

if __name__ == '__main__':
    # Use this for any experiments you want to run
    pass 
