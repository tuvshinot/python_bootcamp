#user.py
from library import Base

class Derived(Base):
    def bar(self):
        return self.foo()

dirData = dir(Derived)

if 'foo' not in dirData:
    raise TypeError('Foo not difined!')
print('we have foo')
