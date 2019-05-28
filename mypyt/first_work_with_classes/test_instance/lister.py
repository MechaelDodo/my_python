class ListInstance:
    def __str__(self):
        self.__visited = {}
        bases_names = ''
        for cl_name in self.__class__.__bases__:
            bases_names += (cl_name.__name__ + ',')
        return '<Instance of %s (%s), address %s:\n%s %s>' % (
            self.__class__.__name__,
            bases_names,
            id(self),
            self.__attrnames(self, 0),
            self.__listclass(self.__class__, 4))
    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n%s<Class %s:, address %s: (see above)>\n' % (
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent+4)
                        for c in aClass.__bases__)
            return '\n %s<Class %s, address %s:\n%s %s %s\n' % (
                dots,
                aClass.__name__,
                id(aClass),
                self.__attrnames(aClass, indent),
                ''.join(genabove),
                dots)
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '%s = <>\n' % attr
            else:
                result += spaces + '\t %s = %s\n' % (attr, getattr(obj, attr))
        return result
