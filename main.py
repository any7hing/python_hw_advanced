class Stack:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self) -> bool: 
        if len(self.stack) == 0: return False
        else: return True

    def push(self, new_element):
        self.stack.append(new_element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    def check(self, string_data: str):
        brakets = {'(': ')', '[': ']', '{': '}'}
        brakets2 = {x: y for y, x in brakets.items()}
        if len(string_data)%2 != 0: return False
        for item in string_data:
            if item in brakets.keys():
                self.push(item)   
            if item in brakets.values():
                try:
                    res = self.pop()
                    if brakets2[item] != res: return False
                except IndexError:
                    return True
        return True


if __name__ == '__main__':
    mystack = Stack()
