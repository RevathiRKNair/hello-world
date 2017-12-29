#! /usr/bin/python
a= input("enter first no:")
b= input("second number:")

class Gate(object):
    def __init__(self,a,b):
        self.input[0] = a
        self.input[1] = b
        self.output = None
        
    def logic(self):
        raise NotImplementedError

    def output(self):
        self.logic()
        return self.output


class AndGate(Gate):
       def logic(self):
         self.output = self.input[0] and self.input[1]
         return self.output

class OrGate(Gate):
    def logic(self):
        self.output = sef.input[0] or self.input[1]
        return self.output

class NotGate(Gate):
        def logic(self):
          self.output = not self.input[0]
          return self.output


c= input(" choose the operation: \n 1.NAND \n 2.NOR \n")
if c==1:
    class NandGate(AndGate, NotGate):
        def logic(self):
            andout = super (NandGate, self).logic()
            Gate.__init__(self, andout)
            self.output = NotGate.logic(self)
            return self.output
            print ("output =",self.output)
     
else:
    class NorGate(OrGate, NotGate):
        def logic(self):
            orout = super(NorGate, self).logic()
            Gate.__init__(self, orout)
            self.output = NotGate.logic(self)
            return self.output
            print ("output =",self.output)




    


