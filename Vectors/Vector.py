#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 20:26:20 2017

@author: bobrinik

"""


class Vector:    
    def __init__(self, values):
        self.values = values

    @classmethod
    def zipper(cls,func, v1, v2):
        myVector = Vector(list(map(func, zip(v1.values, v2.values))))
        return myVector        

    def add(self, vector):
        return (self.zipper(lambda v: v[0] + v[1], self, vector))
    
    def minus(self, vector):
        if(len(self.values) != len(vector.values)):
            raise Exception("Vectors don't have the same dimension")
        return (self.zipper(lambda v: v[0] - v[1], self, vector))
    
    def negate(self):
        self.values = list(map(lambda v: -1 * v, self.values))
        
    def mult(self, scalar):
        result = map(lambda v: scalar * v, self.values)
        myVector = Vector(list(result))
        return myVector
        
    def div(self, scalar):
       values = map(lambda v:  float(v) / scalar, self.values)
       myVector = Vector(list(values))
       return myVector
    
    def dot_product(self, vector):
        if(len(self.values) != len(vector.values)):
            raise Exception("Vectors don't have the same dimension")
        
        values = map(lambda v: v[0]*v[1], zip(self.values, vector.values))
        mySum = sum(values)
        return mySum
    
    def pprint(self):
        result = ",".join(str(v) for v in self.values)
        print(result)
        
    def get(self):
        result = ",".join(str(v) for v in self.values)
        return result

    def equal(self, vector):
        if(len(self.values) != len(vector.values)):
            raise Exception("Vectors don't have the same dimension")
        
        for i in range(len(vector.values)):
            if(self.values != vector.values):
                return False
        return True
    
    def copy(self):
        values = self.values[:]
        myVector = Vector(values)
        return myVector
            
if __name__ == '__main__':
    v1 = Vector([1,2,3])
    v2 = Vector([1,2,3])
    v3 = v1.add(v2)
    assert(v3.get() == "2,4,6")
    v4 = v3.minus(v1)
    assert(v4.get() == "1,2,3")
    v5 = v4.mult(2)
    assert(v5.get() == "2,4,6")
    v6 = v5.div(2)
    assert(v6.get() == "1.0,2.0,3.0")
    v6.negate()
    assert(v6.get() == "-1.0,-2.0,-3.0")
    dot_prod = v6.dot_product(v5)
    assert(dot_prod == -28.0)
    assert(v1.equal(v2))
    v7 = v1.copy()
    v1.negate()
    assert(v7.get() == "1,2,3")