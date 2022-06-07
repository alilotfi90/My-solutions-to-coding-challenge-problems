#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  plane7.py
#  
#  Copyright 2018 Ali Lotfi <ali@ali-Oryx-Pro>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import argparse
from copy import deepcopy
import os
class Plane:
    # There are p points and lines. They are numbered from 0 to p-1.
    # Each line has q points.
    def __init__(self, name):
        self.name = name
        self.lines = []
        self.readplane()
        self.p = len(self.lines)
        self.q = len(self.lines[0])
        self.points = []
        self.fill_points()
        self.joins = []
        self.fill_joins()
        self.meets = []
        self.fill_meets()

    def readplane(self):
        # The only argument of the program is a file name.
        # The file contains p rows, which are the lines of the plane.
        # Each row is a list of q integers (the points of the line) separated by spaces.
        # lines[] is a list of p lists, which are the listings of the points on the lines.
        # We do not check that the points on the lines are pairwise different,
        # nor the number of points. Maybe we should, if we do not trust the tables.
        planef = open(self.name, 'r')
        for line in planef:
			print(line)
			self.lines.append(map(int, line.split()))
    def fill_points(self):
        # points[] is a list of p lists, which are the listings of the lines through the given points.
        # No error checking here
        for i in range(self.p):
            self.points.append([])
        for i in range(self.p):
            for j in self.lines[i]:
                self.points[j].append(i)

                
    def fill_joins(self):
        # joins is a pxp matrix.
        # The rows and columns correspond to the points.
        # The elements in the diagonal are all -1.
        # Otherwise, joins[i][j] is the line containing i and j.
        empty = []
        for i in range(self.p):
            empty.append(-1)
        for i in range(self.p):
            self.joins.append(deepcopy(empty))
        for i in range(self.p):
            a = self.lines[i]
            # a is the i-th line.
            # It is the join of any two different points on this line. We fill the matrix accordingly.
            for j in range(self.q):
                for k in range(self.q):
                    if j == k:
                        continue
                    if self.joins[a[j]][a[k]] != -1:
                        print "Error: points ", a[j], " and ", a[k], " are contained in lines ", i, " and ", [a[j]][a[k]], " ."
                        exit()
                    else:
                        self.joins[a[j]][a[k]] = i
        # Error checking.
        for i in range(self.p):
            for j in range(self.p):
                if i == j:
                    if self.joins[i][j] != -1:
                        print "Error: points ", i, " and ", j, "have no join."
                        exit()
                elif self.joins[i][j] == -1:
                    print "Internal error 1."
                    # This cannot happen, elements on the diagonal should be -1
                    exit()

    def fill_meets(self):
        # meets is a pxp matrix.
        # The rows and columns correspond to the points.
        # The elements in the diagonal are all -1.
        # Otherwise, meets[i][j] is the intersection point of the lines i and j.
        empty = []
        for i in range(self.p):
            empty.append(-1)
        for i in range(self.p):
            self.meets.append(deepcopy(empty))
        for i in range(self.p):
            a = self.points[i]
            # a is the list of lines containing point i.
            # It is the meet of any two different lines through this point. We fill the matrix accordingly.
            for j in range(self.q):
                for k in range(self.q):
                    if j == k:
                        continue
                    if self.meets[a[j]][a[k]] != -1:
                        print "Error: lines ", a[j], " and ", a[k], " contain points ", i, " and ", [a[j]][a[k]], " ."
                        exit()
                    else:
                        self.meets[a[j]][a[k]] = i
        # Error checking.
        for i in range(self.p):
            for j in range(self.p):
                if i == j:
                    if self.meets[i][j] != -1:
                        print "Error: lines ", i, " and ", j, "have no intersection."
                        exit()
                elif self.meets[i][j] == -1:
                    print "Internal error 2."
                    # This cannot happen, elements on the diagonal should be -1
                    exit()

class Coord:
    def __init__(self, P, O, X, Y, Z):
        # We assume that Z is on XY.
        self.P = P
        self.O = O
        self.X = X
        self.Y = Y
        self.Z = Z
        self.OX = P.joins[O][X]
        self.OY = P.joins[O][Y]
        self.OZ = P.joins[O][Z]
        self.XY = P.joins[X][Y]
        self.vlines = []
        self.vlines_inv = {}
        self.hlines = [-1]*P.q
        self.prep_subtraction_lines()

    def prep_subtraction_lines(self):
        # We prepare 3 lists.
        # vlines contains the lines through Y except XY, indexed from 0 to q-1.
        # vlines_inv is the inverse of the previous list, it is a dictionary.
        # hlines applies the transformation A -> A(O+Z) + X to vlist
        self.vlines = deepcopy(self.P.points[self.Y])
        self.vlines.remove(self.XY)
        for i in range(self.P.q-1):
            self.vlines_inv[self.vlines[i]] = i
            self.hlines[i]=self.P.joins[self.P.meets[self.vlines[i]][self.OZ]][self.X]
    
    def subtract(self, b, a):
        # We use the formula {[A(O+Z) + X ]B + Z}(O+X) + Y
        # B and A are lines through Y except XY.
        # The result is also such a line.
        # a and b are in range(q-1), the underlying set of the loop.
        # We use the lists defined in prep_subtraction_lines()
        # The result is also in range(q-1)
        m = self.P.meets[self.hlines[a]][self.vlines[b]]
        rp = self.P.meets[self.P.joins[m][self.Z]][self.OX]
        rl = self.P.joins[rp][self.Y]
        return self.vlines_inv[rl]



def prep_subtraction(P, C, rf):
    # P is a plane
    # C is a valid Coordinate-system
    # rf is the file containing the results
    X = C.X
    Y = C.Y
    Z = C.Z
    O = C.O
    algname = P.name +  '_OXYZ' + '_' + str(O) + '_' + str(X) + '_' + str(Y) + '_' + str(Z)
    print algname
    of = open(algname + '.alg', 'w')
    of.write(str(P.q-1) + '\n')
    of.write(str(2) + '\n')
    for b in range(P.q-1):
        for a in range(P.q-1):
            s = C.subtract(b,a)
            of.write(str(s) + '\n')
    of.close()
    check_algebra(algname, rf)
    

def check_algebra(algname, rf):
    os.system("typ " + algname + "> /dev/null")
    print
    tf = open(algname + '.typ', 'r')
    types = set()
    for r in tf:
        if r[0] == ',':
            list = r.split(",")
            types.add(r[-2])
    tf.close()
    rf.write(algname + ' ' + ''.join(str(e) for e in types) + '\n')
    os.system("rm " + algname + ".*")
    

def check_quadrilaterals(name):
    P = Plane(name)
    resultsfile = open(name + '.res', 'w')
    for X in range(P.p-1):
        for Y in range(P.p):
            if X == Y:
                continue
            for O in range(P.p):
                if O == X:
                    continue
                if O == Y:
                    continue
                XY = P.lines[P.joins[X][Y]]
                print X, Y, P.joins[X][Y], XY
                if O in XY:
                    continue
                for Z in XY:
                    if Z == X:
                        continue
                    if Z == Y:
                        continue
                    prep_subtraction(P, Coord(P, O, X, Y, Z), resultsfile)

def typ3detect(filename):
	t=open(filename,"r")
	count=0
	for line in t:
		if count<10 and int(line[len(line)-2])==3:
			print(line)
			
			count=count+1
		if count==10:
			exit()
def main(args):
	
    #t=open("fano.txt","r")
    p=Plane("fano.txt")
    p.lines
    print(p.points)
    print(p.meets)
    print(p.joins)
    p.fill_points()
    print(args[1])
    typ3detect(args[1])
    #p.readplane()
    #c=Coord("fano.txt",p,o,x,y,z)
    #for j in range(0,len(p.lines)):
	#	print(p.lines[j])
    #print("starting new exploaration:\n")
    #for i in range(0,len(p.points)):
	#	print(p.points[i])
    #p.fill_points()
    O=p.points[0][0]
    X=p.points[0][1]
    Y=p.points[0][2]
    Z=p.points[0][3]
    check_quadrilaterals("fano.txt")
    #print(p.q)
    #p.fill_joins()
    #p.fill_meets()
    #print(p.meets)	
    #print(p.joins)
    #print("this is",O)
    #c=Coord(p,O,X,Y,Z)
    #parser = argparse.ArgumentParser()
    #parser.add_argument("plane")
    #args = parser.parse_args()
    #check_quadrilaterals(args.plane)
    
    return 0

if __name__ == '__main__':
    import sys
    import os
    sys.exit(main(sys.argv))
