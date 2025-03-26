#Iterators(object that enabels traversal through a sequence of data ,allowing you to access elements one at a time without needing to know the underlying structure)
my_list = [1,2,3]
my_iterator = iter(my_list)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
#IMplementing custom iterators
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1
for number in CountDown(5):
    print(number)

