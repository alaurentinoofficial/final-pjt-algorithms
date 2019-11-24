
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

    def __init__(self):
        self.__root = None
        self.__top = None
        self.__size = 0
    

    @property
    def length(self):
        return self.__size
    
    
    def append(self, value):
        self.__size += 1
        
        if self._item == None:
            self._item = Node(valor)
            return
        
        aux = self.__root
        while not aux.next == None:
            aux = aux.next
        
        aux.next = Node(value)
        aux.next.previous = aux
    

    def _get_item(self, index):
        if index < 0 or index > self._size-1:
            raise ValueError("Index out exception!")
            return
        
        count = 0
        aux = self._item
        
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