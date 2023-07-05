
class Foo:
    def __init__(self, bar):
        self.bar = bar
 
    def update(self, bar):
        self.bar = bar
 
foo = Foo(10)
foo.update(20)
print(foo.__class__)