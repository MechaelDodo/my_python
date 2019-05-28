class C:
	def __init__(self, fun):
		self.calls = 0
		self.func = fun
	def __call__(self, *args):
		self.calls += 1
		print('calls: %s, fun\'s name: %s' % (
			self.calls, self.func.__name__))
		self.func(*args)

@C                  
def spam(a, b, c):      #spam = C(spam)       
    print(a, b, c)

spam(1, 2, 3)
spam(44, 2, 3)
s = C(spam(11,2,3))

