
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Question 2
# Enqueue O(1) as
# Dequeue O(1) as

# Question 2


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

# Question 3


class Single_List_Traversal:
    # def o1(head):

    # Question 4


class Queue:
    def __init__(self) -> None:
        self.in_stack = []  # Hold elements in the order they were eunqueued
        self.out_stack = []
        self.sum = 0
        self.count = 0

    def enque(self, item):
        self.count += 1
        self.sum += item
        self.in_stack.append(item)

    # O(n)
    def deque(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        dequeued_element = self.out_stack.pop()

        self.count -= 1
        self.sum -= dequeued_element
        return dequeued_element

    def is_empty(self):
        return not self.in_stack and not self.out_stack

    def get_average(self):
        if self.count == 0:
            return None
        return self.sum/self.count


q = Queue()
q.enque(1)
q.enque(2)
print(q.is_empty())

print(q.deque())
print(q.deque())
print(q.is_empty())

#####################################
# rachel.kwok@sydney.edu.au
# Question 6


class Q6:
    def generate_permutations(n):
        if n == 1:
            return [[1]]
        else:
            result = []
            for k in range(1, n+1):
                sub_permutations = generate_permutations(n-1)
                for p in sub_permutations:
                    result.append([k] + p)
            return result

# Question 7


class Q7:
    def generate_permutations(n):
        stack = [[i for i in range(1, n+1)]]
        result = []
        while stack:
            lst = stack.pop()
            if len(lst) == 1:
                result.append(lst)
            else:
                for i in range(len(lst)):
                    new_lst = lst[:i] + lst[i+1:]
                    new_lst.insert(0, lst[i])
                    stack.append(new_lst)
        return result


class q6:
    def permutate(nums):
        if len(nums) == 1:
            return [nums]
