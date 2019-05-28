class AttrDisplay:
    """
    if you want to use this class you must inherit from this class
    the class which you use.
    This class help to read all attributes in class which you chose.
    """
    def _gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s = %s' % (key, self.__dict__[key]))
        return ', '.join(attrs)
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__,self._gatherAttrs())
    #def superGatherAttrs(self):
    #    attrs = []
    #    for key in sorted(self.__dict__):
    #        attrs.append('%s = %s' % (key, self.__dict__[key]))
    #    for key in sorted(self.__class__.__dict__):
    #        attrs.append('%s = %s' % (key, self.__class__.__dict__[key]))
    #    return ', '.join(attrs)

if __name__ == '__main__':
    
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class TopTestSecond(TopTest):
        count = 0
        def __init__(self):
            self.namesec = 'NANANA'

    class SubTest(AttrDisplay):
        pass

    X, Y, Z = TopTest(), SubTest(), TopTestSecond()
    print(X)
    print(Y)
    print(Z)
    
