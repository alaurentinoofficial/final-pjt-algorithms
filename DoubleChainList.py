class Ordering:
    
    @staticmethod
    def compare(asceding=True, key=lambda x: x):
        def wrapper(a, b):
            asceding_multiplier = 1 if asceding else -1

            return ((key(a) > key(b)) - (key(a) < key(b))) * asceding_multiplier
        
        return wrapper


class Node:
    def __init__(self, value, previous_node=None, next_node=None):
        self.__value = value    
        self.__previous = previous_node if isinstance(previous_node, Node) else None
        self.__next = next_node if isinstance(next_node, Node) else None
    

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, x):
        self.__value = x
    
    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, x):
        if isinstance(x, Node):
            self.__previous = x
    
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, x):
        if isinstance(x, Node):
            self.__next = x

class DoubleChainList:

    def __init__(self, interable=None, orderby=lambda a, b: 1):
        self.__root = None
        self.__top = None
        self.__size = 0
        self.__interations = 0
        self.__compare = orderby

        if interable != None:
            for item in interable:
                self.append(item)
    
    def __iter__(self):
        self.__interations = 0
            
        return self
    
    def __next__(self):
        if self.__interations < self.__size:
            self.__interations += 1
            return self.__getitem__(self.__interations - 1)
        else:
            raise StopIteration()

    @property
    def length(self):
        return self.__size
    
    
    def append(self, value):
        self.__size += 1
        node = Node(value)
        
        if self.__root == None:
            self.__root = Node(value)
            return
        
        pivot = self.__root

        while pivot.next != None and self.__compare(node.value, pivot.next.value) == 1:
            pivot = pivot.next

        aux_next = pivot.next
        pivot.next = node

        node.previous = pivot
        node.next = aux_next
    

    def _get_item(self, index):
        if index < 0 or index > self.__size-1:
            raise ValueError("Index out exception!")
            return
        
        count = 0
        aux = self.__root
        
        while count < index:
            aux = aux.next
            count += 1
        
        
        return aux
    
    def __setitem__(self, index, value):
        self._get_item(index).value = value
    
    def __getitem__(self, index):
        return self._get_item(index).value
    
    def pop(self, index):
        if index < 0 or index > self._size-1:
            raise ValueError("Index out exception!")
            return
        
        if index == 0:
            self._size -= 1
            self._item = self._item.next
            return
        
        before = self._get_item(index-1)
        after = self._get_item(index+1) if index+1 != self._size+1 else None
        
        self._size -= 1
        before.next = after