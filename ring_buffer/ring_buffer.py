from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        else:
            self.current += 1
            for i in range (0, self.current):
                self.storage.move_to_end(self.storage.head)
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            for i in range (0, self.current):
                self.storage.move_to_front(self.storage.tail)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
