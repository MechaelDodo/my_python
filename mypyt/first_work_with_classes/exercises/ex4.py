class Meta:
    def __init__(self): pass
    def __getattr__(self, attr):
        print('get', attr)
    def __setattr__(self, attr, val):
        print('set', attr, val)

if __name__ == '__main__':
    s = Meta()
    s.append
    s.a = 'sad'
    s.vb = 'haha'
    
    
