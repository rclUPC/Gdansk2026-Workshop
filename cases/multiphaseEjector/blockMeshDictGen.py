#!/usr/bin/env python
# coding: utf-8

# Script for generating mesh for ejector - Zhang 2012 
# ================================


class ejectorMesh(object):
    
    def __init__(self):
        from numpy import radians,tan, sin, pi

        # Geometric parameters (all in mm)
        self.l1 = 380
        self.l2 = 85
        self.l3 = 70
        self.l4 = 180
        self.r1 = 80/2
        self.r2 = 14/2
        self.r3 = 21/2
        self.r4 = 60/2

        # Equivalent Secondary Inlet length
        self.rMax = 57.05;                             # Radius to the revolution geometry of the equivalent inlet
        dOrig = 80;                                    # Diameter of Zhang 2012 Secondary Inlet
        self.le = 0.25*(dOrig**2)/(2*self.rMax)        # Length of the equivalent area Secondary Inlet
        
        # Outline Geometry definition (coordinates measured in WebPlotDigitizer and checked with report-Given parameters)

            # Plane A
        self.xA0 = 0
        self.rA0 = 0
        self.xA1 = 0
        self.rA1 = self.r1

            # Plane B
        self.xB0 = 92.72
        self.rB0 = 0
        self.xB1 = self.xB0
        self.rB1 = self.r1

            # Plane C
        self.xC0 = self.l1
        self.rC0 = 0
        self.xC1 = self.xC0
        self.rC1 = self.r2


        intendedXplaneD = 489.34-self.l2
        actualXplaneD = 407.80
        corrPlanesDE = 0.5*abs(intendedXplaneD-actualXplaneD)
        
            # Plane D (corrected coordinates: 
        self.xD0 = 407.80-corrPlanesDE
        self.rD0 = 0
        self.xD1 = self.xD0
        self.rD1 = self.r2
        self.xD2 = self.xD0
        self.rD2 = 9.46

            # Plane E
        substractToE3 = 0.25                   # Parameter for the trimming of orthogonal quality. Default name is 'substract' but at the end of the trimming it could actually be an addition.
        self.xE0 = 489.34+corrPlanesDE
        self.rE0 = 0
        self.xE3 = self.xE0+substractToE3
        self.rE3 = self.r3    


        intendedXplaneF = self.xE0+self.l3
        actualXplaneF = 559.12
        corrPlaneF = abs(intendedXplaneF-actualXplaneF)                
        
            # Plane F
        substractToF3 = substractToE3/2
        self.xF0 = 559.12+corrPlaneF
        self.rF0 = 0
        self.xF3 = self.xF0+substractToF3
        self.rF3 = self.r3

        intendedXplaneG = self.xF0+self.l4
        actualXplaneG = 737.65
        corrPlaneG = abs(intendedXplaneG-actualXplaneG)                        

            # Plane G
        self.xG0 = 737.65+corrPlaneG
        self.rG0 = 0
        self.xG3 = self.xG0
        self.rG3 = self.r4
        
            # Plane H
        self.xH0 = 131.88
        self.rH0 = 43.21
        self.xH1 = self.xH0
        self.rH1 = 57.05

            # Plane I
        self.xI1 = 292.63
        self.rI1 = 57.05

            # Plane J
        self.xJ1 = 372.23
        self.rJ1 = 29.55

            # Plane K
        self.xK0 = 378.74
        self.rK0 = self.rD2

            # Plane l
        self.xL1 = self.xH1+self.le
        self.rL1 = self.rH1

        # Midpoints geometry definition (factors are adjusted by hand)
        
            # Plane J
        factorJ = 0.94
        self.xJ0 = self.xH0+factorJ*(self.xK0-self.xH0)
        self.rJ0 = self.rK0+(1-factorJ)*(self.rH0-self.rK0)

            # Plane I
        factorI = 0.6
        self.xI0 = self.xH0+factorI*(self.xK0-self.xH0)
        self.rI0 = self.rK0+(1-factorI)*(self.rH0-self.rK0)

            # Plane K
        factorK = 0.12
        self.xK1 = self.xJ1+factorK*(self.xE3-self.xJ1)
        self.rK1 = self.rE3+(1-factorK)*(self.rJ1-self.rE3)

            # Plane L
        factorL = 0.9*self.le/(self.xI0-self.xH0)
        self.xL0 = self.xH0+factorL*(self.xI0-self.xH0)
        self.rL0 = self.rI0+(1-factorL)*(self.rH0-self.rI0)

            # Plane D
        factorD = 0.3
        self.xD3 = self.xJ1+factorD*(self.xE3-self.xJ1)
        self.rD3 = self.rE3+(1-factorD)*(self.rJ1-self.rE3)      

            # Plane E
        factorE1 = 0.4
        factorE2 = 0.5
        self.xE1 = self.xE0
        self.rE1 = self.rE0+factorE1*(self.rE3-self.rE0)
        self.xE2 = self.xE0
        self.rE2 = self.rE0+factorE2*(self.rE3-self.rE0)

            # Plane F
        factorF1 = 0.4
        factorF2 = 0.5
        self.xF1 = self.xF0
        self.rF1 = self.rF0+factorF1*(self.rF3-self.rF0)
        self.xF2 = self.xF0
        self.rF2 = self.rF0+factorE2*(self.rF3-self.rF0)

            # Plane G
        factorG1 = 0.4
        factorG2 = 0.5
        self.xG1 = self.xG0
        self.rG1 = self.rG0+factorG1*(self.rG3-self.rG0)
        self.xG2 = self.xG0
        self.rG2 = self.rG0+factorG2*(self.rG3-self.rG0)        
        
        # Mean longitude parameters (for blocks 6, 7, 8, 9, 10, 11 and 12; i.e. secondary inlet)
        from math import sqrt
            
            # Utility to calculate Mean Longitude between segments AB & CD
        def meanlongitude(xA, yA, xB, yB, xC, yC, xD, yD):
            AB = sqrt((xA-xB)**2+(yA-yB)**2)
            CD = sqrt((xC-xD)**2+(yC-yD)**2)
            #return (0.5*(AB+CD))
            return (min(AB,CD)+0.33*abs(AB-CD)) # Return a value closer to the smaller segment
        
                # Horizontal
        self.x3 = meanlongitude(self.xL0, self.rL0, 
                                self.xI0, self.rI0,
                                self.xL1, self.rL1,                                
                                self.xI1, self.rI1) 
        self.x4 = meanlongitude(self.xI0, self.rI0, 
                                self.xJ0, self.rJ0,
                                self.xI1, self.rI1,                                
                                self.xJ1, self.rJ1)
        self.x5 = meanlongitude(self.xJ0, self.rJ0, 
                                self.xK0, self.rK0,
                                self.xJ1, self.rJ1,                                
                                self.xK1, self.rK1)
        self.x6 = meanlongitude(self.xK0, self.rK0, 
                                self.xD2, self.rD2,
                                self.xK1, self.rK1,                                
                                self.xD3, self.rD3)
        self.x7 = meanlongitude(self.xD0, self.rD0,
                                self.xE0, self.rE0,
                                self.xD1, self.rD1,
                                self.xE1, self.rE1)
        self.x8 = meanlongitude(self.xD1, self.rD1,
                                self.xE1, self.rE1,
                                self.xD2, self.rD2,
                                self.xE2, self.rE2)
        self.x9 = meanlongitude(self.xD2, self.rD2,
                                self.xE2, self.rE2,
                                self.xD3, self.rD3,
                                self.xE3, self.rE3)
        self.x10 = meanlongitude(self.xE0, self.rE0,
                                 self.xF0, self.rF0,
                                 self.xE1, self.rE1,
                                 self.xF1, self.rF1)
        self.x11 = meanlongitude(self.xE1, self.rE1,
                                 self.xF1, self.rF1,
                                 self.xE2, self.rE2,
                                 self.xF2, self.rF2)
        self.x12 = meanlongitude(self.xE2, self.rE2,
                                 self.xF2, self.rF2,
                                 self.xE3, self.rE3,
                                 self.xF3, self.rF3)
        self.x13 = meanlongitude(self.xF0, self.rF0,
                                 self.xG0, self.rG0,
                                 self.xF1, self.rF1,
                                 self.xG1, self.rG1)
        self.x14 = meanlongitude(self.xF1, self.rF1,
                                 self.xG1, self.rG1,
                                 self.xF2, self.rF2,
                                 self.xG2, self.rG2)
        self.x15 = meanlongitude(self.xF2, self.rF2,
                                 self.xG2, self.rG2,
                                 self.xF3, self.rF3,
                                 self.xG3, self.rG3)
        self.x16 = meanlongitude(self.xH0, self.rH0,
                                 self.xL0, self.rL0,
                                 self.xH1, self.rH1,
                                 self.xL1, self.rL1)
        
                # Vertical
        self.r1 = meanlongitude(self.xB0, self.rB0,
                                self.xB1, self.rB1,
                                self.xC0, self.rC0,
                                self.xC1, self.rC1)
        self.r4 = meanlongitude(self.xI0, self.rI0, 
                                self.xI1, self.rI1, 
                                self.xJ0, self.rJ0,
                                self.xJ1, self.rJ1)        
        self.r7 = meanlongitude(self.xD0, self.rD0,
                                self.xD1, self.rD1,
                                self.xE0, self.rE0,
                                self.xE1, self.rE1)        
        self.r8 = meanlongitude(self.xD1, self.rD1,
                                self.xD2, self.rD2,
                                self.xE1, self.rE1,
                                self.xE2, self.rE2)        
        self.r6 = meanlongitude(self.xK0, self.rK0, 
                                self.xK1, self.rK1, 
                                self.xD2, self.rD2,
                                self.xD3, self.rD3)        
        self.r9 = meanlongitude(self.xD2, self.rD2,
                                self.xD3, self.rD3,
                                self.xE2, self.rE2,
                                self.xE3, self.rE3)
        self.r10 = self.rF1-self.rF0
        self.r11 = self.rF2-self.rF1
        self.r12 = meanlongitude(self.xE2, self.rE2,
                                 self.xE3, self.rE3,
                                 self.xF2, self.rF2,                                 
                                 self.xF3, self.rF3)

    def discretization(self,n):
        # Discretization
        
            # Number of cells along the axis  (n = number of cell in nozzle (length))
        self.Delta = (self.xD0-self.xC0)/n # cell size (mm)
                # Main inlet
        self.b0N = int((self.xB0-self.xA0)/self.Delta)
        self.b1N = int((self.xC0-self.xB0)/self.Delta)
        self.b2N = int((self.xD0-self.xC0)/self.Delta)
                # Secondary inlet
        self.b3N = round(self.x3/self.Delta)
        self.b4N = round(self.x4/self.Delta)
        self.b5N = round(self.x5/self.Delta)
        self.b6N = round(self.x6/self.Delta)
        self.b16N = round(self.x16/self.Delta)
                # Mixing Chamber - Diffuser
        self.b7N = round(self.x9/self.Delta)    # ---------------------
        self.b8N = self.b7N                   # Coupled blocks 7,8,9
        self.b9N = self.b7N                   # ---------------------
        self.b10N = round(self.x12/self.Delta)  # ------------------------
        self.b11N = self.b10N                 # Coupled blocks 10,11,12
        self.b12N = self.b10N                 # ------------------------     
        self.b13N = round(self.x15/self.Delta)  # ------------------------
        self.b14N = self.b13N                 # Coupled blocks 13,14,15
        self.b15N = self.b13N                 # ------------------------       
        

            # Number of cells on radial direction
                # 1st layer
        self.r0N = round(self.r1/self.Delta)    # -----------------------------
        self.r1N = self.r0N                   #
        self.r2N = self.r0N                   # Coupled blocks 0,1,2,7,10,13
        self.r7N = self.r0N                   #
        self.r10N = self.r0N                  #
        self.r13N = self.r0N                  # -----------------------------
                # 3rd layer
        self.r3N = round(self.r4/self.Delta)    # -----------------------------------
        self.r4N = self.r3N                   #
        self.r5N = self.r3N                   #
        self.r6N = self.r3N                   # Coupled blocks 16,3,4,5,6,9,12,15
        self.r9N = self.r3N                   #
        self.r12N = self.r3N                  #
        self.r15N = self.r3N                  #
        self.r16N = self.r3N                  # ---------------------------------
                # Middle layer
        self.midDelta = 0.5*(self.r7/self.r7N + self.r9/self.r9N) # Comprimeix les cel·les
        self.r8N = max(1,
            round(self.r8/self.midDelta)) # -----------------------------
        self.r11N = self.r8N                  # Coupled blocks 8,11,14
        self.r14N = self.r8N                  # -----------------------------        

        # Grading
        self.rGrading = 0.2 #rGrading = 0.2
        self.rGradingInv = 1/self.rGrading

    def plot(self):
        import matplotlib.pyplot as plt
        import matplotlib.patches as pat
        from numpy import degrees
        plt.rcParams["figure.figsize"] = (24, 18)

        fig = plt.figure(figsize=(20,20))
        ax = fig.add_subplot(1,1,1)
        ax.set_aspect('equal')
        ax.set_xlim(-10,self.xG0+20)
        ax.set_ylim(-10,self.rH1+10)
        xVector = [self.xA0,self.xB0,self.xC0,self.xD0,self.xE0,self.xF0,self.xG0,self.xG3,self.xF3,self.xE3,self.xD3,self.xK1,self.xJ1,self.xI1,self.xL1,self.xH1,self.xH0,self.xL0,self.xK0,self.xD2,self.xD1,self.xC1,self.xB1,self.xA1,self.xA0]
        rVector = [self.rA0,self.rB0,self.rC0,self.rD0,self.rE0,self.rF0,self.rG0,self.rG3,self.rF3,self.rE3,self.rD3,self.rK1,self.rJ1,self.rI1,self.rL1,self.rH1,self.rH0,self.rL0,self.rK0,self.rD2,self.rD1,self.rC1,self.rB1,self.rA1,self.rA0]
        
        ax.plot(xVector,rVector,'b')      # Plot blue outline
        xVector = [self.xA0,self.xA1,self.xB0,self.xB1,self.xC0,self.xC1,self.xD0,self.xD1,self.xD2,self.xD3,self.xE0,self.xE1,self.xE2,self.xE3,self.xF0,self.xF1,self.xF2,self.xF3,self.xG0,self.xG1,self.xG2,self.xG3,self.xH0,self.xH1,self.xI0,self.xI1,self.xJ0,self.xJ1,self.xK0,self.xK1,self.xL0,self.xL1]
        rVector = [self.rA0,self.rA1,self.rB0,self.rB1,self.rC0,self.rC1,self.rD0,self.rD1,self.rD2,self.rD3,self.rE0,self.rE1,self.rE2,self.rE3,self.rF0,self.rF1,self.rF2,self.rF3,self.rG0,self.rG1,self.rG2,self.rG3,self.rH0,self.rH1,self.rI0,self.rI1,self.rJ0,self.rJ1,self.rK0,self.rK1,self.rL0,self.rL1]
        labels = ['A0','A1','B0','B1','C0','C1','D0','D1','D2','D3','E0','E1','E2','E3','F0','F1','F2','F3','G0','G1','G2','G3','H0','H1','I0','I1','J0','J1','K0','K1','L0','L1']
        ax.plot(xVector, rVector,'k',marker='o',markersize=5,linestyle='')
        for i in range(len(xVector)):
            ax.text(xVector[i]+2,rVector[i]+1,labels[i],fontsize=12,ha='left',color='k')
        ax.set_xlabel("m")

    def createDictionary(self):

        import ofblockmeshdicthelper as ofbmd

        bmd = ofbmd.BlockMeshDict()
        bmd.set_metric('m')

        basevs = [
        # Axis vertices
            ofbmd.Vertex(self.xA0, self.rA0, 0.0, 'vA0'),
            ofbmd.Vertex(self.xB0, self.rB0, 0.0, 'vB0'),
            ofbmd.Vertex(self.xC0, self.rC0, 0.0, 'vC0'),
            ofbmd.Vertex(self.xD0, self.rD0, 0.0, 'vD0'),
            ofbmd.Vertex(self.xE0, self.rE0, 0.0, 'vE0'),
            ofbmd.Vertex(self.xF0, self.rF0, 0.0, 'vF0'),
            ofbmd.Vertex(self.xG0, self.rG0, 0.0, 'vG0'),
        # Primary inlet vertices
            ofbmd.Vertex(self.xA1, self.rA1, 0.0, 'vA1'),
            ofbmd.Vertex(self.xB1, self.rB1, 0.0, 'vB1'),
            ofbmd.Vertex(self.xC1, self.rC1, 0.0, 'vC1'),
            ofbmd.Vertex(self.xD1, self.rD1, 0.0, 'vD1'),
        # Secondary inlet vertices
            ofbmd.Vertex(self.xH0, self.rH0, 0.0, 'vH0'),
            ofbmd.Vertex(self.xH1, self.rH1, 0.0, 'vH1'),
            ofbmd.Vertex(self.xI0, self.rI0, 0.0, 'vI0'),
            ofbmd.Vertex(self.xI1, self.rI1, 0.0, 'vI1'),
            ofbmd.Vertex(self.xJ0, self.rJ0, 0.0, 'vJ0'),
            ofbmd.Vertex(self.xJ1, self.rJ1, 0.0, 'vJ1'),
            ofbmd.Vertex(self.xK0, self.rK0, 0.0, 'vK0'),
            ofbmd.Vertex(self.xK1, self.rK1, 0.0, 'vK1'),
            ofbmd.Vertex(self.xL0, self.rL0, 0.0, 'vL0'),
            ofbmd.Vertex(self.xL1, self.rL1, 0.0, 'vL1'),
            ofbmd.Vertex(self.xD2, self.rD2, 0.0, 'vD2'),
            ofbmd.Vertex(self.xD3, self.rD3, 0.0, 'vD3'),            
        # Mixing chamber & Diffuser vertices
            ofbmd.Vertex(self.xE1, self.rE1, 0.0, 'vE1'),
            ofbmd.Vertex(self.xE2, self.rE2, 0.0, 'vE2'),
            ofbmd.Vertex(self.xE3, self.rE3, 0.0, 'vE3'),
            ofbmd.Vertex(self.xF1, self.rF1, 0.0, 'vF1'),
            ofbmd.Vertex(self.xF2, self.rF2, 0.0, 'vF2'),
            ofbmd.Vertex(self.xF3, self.rF3, 0.0, 'vF3'),
            ofbmd.Vertex(self.xG1, self.rG1, 0.0, 'vG1'),
            ofbmd.Vertex(self.xG2, self.rG2, 0.0, 'vG2'),
            ofbmd.Vertex(self.xG3, self.rG3, 0.0, 'vG3'),
        ]

        from numpy import sin, pi
        for v in basevs:
            bmd.add_vertex(v.x, v.y, 0.0, v.name+'+z')
            bmd.add_vertex(v.x,  v.y, -0.1, v.name+'-z')

        # Utility to generate vertices names for blocks
        def vnamegen(x0y0, x1y0, x1y1, x0y1):
            return (x0y0+'-z', x0y1+'-z', x1y1+'-z', x1y0+'-z',
                    x0y0+'+z', x0y1+'+z', x1y1+'+z', x1y0+'+z')
        
        # Blocks 
        b0 = bmd.add_hexblock(vnamegen('vA0', 'vA1', 'vB1', 'vB0'),
                              (self.b0N, self.r0N, 1),
                              'b0',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,
                                                    1, #self.rGrading,
                                                    1))

        b1 = bmd.add_hexblock(vnamegen('vB0', 'vB1', 'vC1', 'vC0'),
                              (self.b1N, self.r1N, 1),
                              'b1',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,
                                                    1, #self.rGrading,
                                                    1))
        b2 = bmd.add_hexblock(vnamegen('vC0', 'vC1', 'vD1', 'vD0'),
                              (self.b2N, self.r2N, 1),
                              'b2',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,
                                                    1, #self.rGrading,
                                                    1))
        b3 = bmd.add_hexblock(vnamegen('vL0', 'vL1', 'vI1', 'vI0'),
                              (self.b3N, self.r3N, 1),
                              'b3',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,
                                                    1, #self.rGrading,
                                                    1))        
        b4 = bmd.add_hexblock(vnamegen('vI0', 'vI1', 'vJ1', 'vJ0'),
                              (self.b4N, self.r4N, 1),
                              'b4',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,
                                                    1, #self.rGrading,
                                                    1))
        b5 = bmd.add_hexblock(vnamegen('vJ0', 'vJ1', 'vK1', 'vK0'),
                              (self.b5N, self.r5N, 1),
                              'b5',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,
                                                    1, #self.rGrading,
                                                    1))
        b6 = bmd.add_hexblock(vnamegen('vK0', 'vK1', 'vD3', 'vD2'),
                              (self.b6N, self.r6N, 1),
                              'b6',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,
                                                    1,
                                                    1))
        b7 = bmd.add_hexblock(vnamegen('vD0', 'vD1', 'vE1', 'vE0'),
                              (self.b7N, self.r7N, 1),
                              'b7',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,
                                                    1,
                                                    1))
        b8 = bmd.add_hexblock(vnamegen('vD1', 'vD2', 'vE2', 'vE1'),
                              (self.b8N, self.r8N, 1),
                              'b8',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,
                                                    1,
                                                    1))
        b9 = bmd.add_hexblock(vnamegen('vD2', 'vD3', 'vE3', 'vE2'),
                              (self.b9N, self.r9N, 1),
                              'b9',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,
                                                    1,
                                                    1))        
        b10 = bmd.add_hexblock(vnamegen('vE0', 'vE1', 'vF1', 'vF0'),
                              (self.b10N, self.r10N, 1),
                              'b10',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,1,1))   
        
        b11 = bmd.add_hexblock(vnamegen('vE1', 'vE2', 'vF2', 'vF1'),
                               (self.b11N, self.r11N, 1),
                               'b11',
                               'fluid',
                               grading=ofbmd.SimpleGrading(1,1,1))
        
        b12 = bmd.add_hexblock(vnamegen('vE2','vE3','vF3','vF2'),
                               (self.b12N, self.r12N, 1),
                               'b12',
                               'fluid',
                               grading=ofbmd.SimpleGrading(1,1,1))
        
        b13 = bmd.add_hexblock(vnamegen('vF0', 'vF1', 'vG1', 'vG0'),
                              (self.b13N, self.r13N, 1),
                              'b13',
                              'fluid',
                              grading=ofbmd.SimpleGrading(1,1,1))   
        
        b14 = bmd.add_hexblock(vnamegen('vF1', 'vF2', 'vG2', 'vG1'),
                               (self.b14N, self.r14N, 1),
                               'b14',
                               'fluid',
                               grading=ofbmd.SimpleGrading(1,1,1))
        
        b15 = bmd.add_hexblock(vnamegen('vF2','vF3','vG3','vG2'),
                               (self.b15N, self.r15N, 1),
                               'b15',
                               'fluid',
                               grading=ofbmd.SimpleGrading(1,1,1))     
        
        b16 = bmd.add_hexblock(vnamegen('vH0','vH1','vL1','vL0'),
                               (self.b16N, self.r16N, 1),
                               'b16',
                               'fluid',
                               grading=ofbmd.SimpleGrading(1,1,1))             

        # Boundaries
        bmd.add_boundary('patch','inletMain',[b0.face('w')])
        bmd.add_boundary('patch','outlet',[i.face('e') for i in [b13,b14,b15]])
        bmd.add_boundary('patch','inletSecondary',[b16.face('n')]) # ALERTA!! hipòtesi diferent al model real... veure croquis
        bmd.add_boundary('wall','wallNozzle1', [i.face('n') for i in [b0,b1,b2]])
        bmd.add_boundary('wall','wallNozzle2', [i.face('s') for i in [b3,b4,b5,b6,b16]]+[i.face('n') for i in [b3,b4,b5,b6,b9]]+[i.face('w') for i in [b16,b8]])
        bmd.add_boundary('wall','wallDiffuser', [i.face('n') for i in [b12,b15]])
        bmd.add_boundary('symmetry','front', [i.face('t') for i in bmd.blocks.values()])
        bmd.add_boundary('symmetry','back', [i.face('b') for i in bmd.blocks.values()])

        # prepare for output
        bmd.assign_vertexid()
        return bmd

    def printDictionary(self,bmd):
        # output
        print(bmd.format())

    def saveDictionary(self,bmd,casePath):
        print(bmd.format(),file=open(casePath+"/system/blockMeshDict",'w'))
        print("blockMeshDict saved in "+casePath+"/system/blockMeshDict")

# This part is to check the mesh in a notebook, but it is not necessary for the script to run.
######
    def createMesh(self,casePath):
        import os

        os.system('/bin/bash -c \"source /opt/openfoam11/etc/bashrc; cd {}; sbatch jobMakeMesh.scr"'.format(casePath))

    def showMesh(self,casePath):
        from fluidfoam import MeshVisu

        myMesh = MeshVisu(path=casePath)

        get_ipython().run_line_magic('matplotlib', 'widget')
        from  matplotlib.collections import LineCollection

        # compute mesh aspect ratio:
        xmin, xmax = myMesh.get_xlim()
        ymin, ymax = myMesh.get_ylim()
        AR = (ymax - ymin) / (xmax - xmin)

        fig, ax = plt.subplots( figsize = (18,18*AR))
        
        # create a collection with edges and print it
        ln_coll = LineCollection(myMesh.get_all_edgesInBox(), linewidths = 0.25, colors = 'blue')
        ax.add_collection(ln_coll, autolim=True)

        # impose the dimensions of the box as the limits of the figure
        ax.set_xlim(myMesh.get_xlim())
        ax.set_ylim(myMesh.get_ylim())

        # to avoid distorting the mesh:
        ax.set_aspect('equal')

        # to don't print axis:
        ax.axis('off')
#######

myEjector = ejectorMesh()
# To use in a intereactive notebook, uncomment the following line:
# myEjector.plot()

n = 15 # Dicretization level (number of cells in nozzle length)
myEjector.discretization(n)

bmd = myEjector.createDictionary()

myEjector.saveDictionary(bmd,casePath='./')
