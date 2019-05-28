import processor

class Uppercase(processor.Processor):
    def converter(self, data):
        return data.upper()

class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())
    def close(self):    pass

if __name__ == '__main__':
    fw =  open('write_test.txt', 'w')
    obj = Uppercase(open('read_test.txt'), fw)
    obj.process()
    fw.close()

    Uppercase(open('read_test.txt'),HTMLize()).process()
    
