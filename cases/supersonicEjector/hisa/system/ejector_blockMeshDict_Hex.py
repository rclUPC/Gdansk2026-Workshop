#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import *


# Definition of variables:

# For the GEOMETRY:

# In[2]:


alpha1=radians(9.0)
alpha2=radians(15.5)
theta=radians(5.0)     #wedge angle
l0=11.5
l1=38.41
l2=7.15
l_ch=51
l3=l_ch-l1-l2
rLip1=0.5
angleLip1= pi/2-alpha2
l3_Lip= l3-rLip1*(1-sin(alpha2))
r1=7.425
r2=1.375
r3= r2+l3_Lip*tan(alpha2)+rLip1*cos(alpha2)
rc= 17.5
#rCollectorTop= 34.5
dd= 0.5
r5= 4.25             #PARAMETER
l4= 21.91
alpha3= 10.0*pi/180    #PARAMETER
rLip2= 4.5
angleLip2= pi/2-alpha3
l4_Lip= l4-rLip2*(1-sin(alpha3))
alpha4= radians(3.0)
l_tb= 155.0
l5= 58.29  #PARAMETER
l6= l_tb-l4-l5
l6_Lip= l6-rLip2*(1-sin(alpha4))
r6= r5+l6_Lip*tan(alpha4)+rLip2*cos(alpha4)
l7= 100.0


# For the Grid points (integrers!)

# In[3]:


n= 25
rN= n
b0N= n
b1N= 3*n
b2N= n
b3N= n
b34N= int(n/2) #EF
b4N= 3*n
b5N= 4*n      #Second channel
b6N= 4*n      #Second diffuser
b67N= n        #Second diffuser exit
b7N= 2*n
b8N= b4N
b9N= b4N
b10N= b4N
rGrading= 0.2
rGradingInv= 1/rGrading

#Plane A:
xA= 0.0
rA= r1

#Plane B:
xB= l0
rB= r1

#Plane C:
xC= xB+l1
rC= r2

#Plane D:
xD= xC+l2
rD= r2

#Plane E:
xE= xD+l3
rE= r3

xEE= xD+l3_Lip
rEE= rD+l3_Lip*tan(alpha2)

xEEE= xE-rLip1*(1-cos(angleLip1/2))
rEEE= rE-rLip1*sin(angleLip1/2)

#Plane F:
xF= xE+rE/2
rF = 0.0

xFF= xF-0.167*rE
rFF= 0.588*rE

#Plane G:
xG= xE+dd
rG= rc
xH= xG
xI= xH+rLip2*(1-sin(alpha3))
rI= r5+l4_Lip*tan(alpha3)
rH= rI+rLip2*cos(alpha3)
xHH= xH+rLip2*(1-cos(angleLip2/2))
rHH= rH-rLip2*sin(angleLip2/2)

xJ= 27.0
rJ= rc
xJJ= xE-2*(xE-xJ)/3
rJJ= rE+2*(rJ-rE)/3
xJJJ= xE-(xE-xJ)/4
rJJJ= rE+(rJ-rE)/4


xK= xH+l4
rK= r5

xL= xK+l5
rL= r5

xM= xL+l6
rM= r6

xMM= xL+l6_Lip
rMM= r5+l6_Lip*tan(alpha4)

xMMM= xM-rLip2*(1-cos(angleLip2/2))
rMMM= r6-rLip2*sin(angleLip2/2)

xO= xM+r6
rO= 0.0
xOO= xM+r6*cos(pi/4)
rOO= r6*sin(pi/4)

xP= xO+l7
rP= 0.0
rQ= rM+l7
xQ= xM
xQQ= xM+(r6+l7)*cos(pi/4)
rQQ= (r6+l7)*sin(pi/4)


# import matplotlib.pyplot as plt
# import matplotlib.patches as pat
# plt.rcParams["figure.figsize"] = (24, 18)

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.set_aspect('equal')
# ax.set_xlim(-10,220)
# ax.set_ylim(-10,25)
# ax.plot([xA,xB,xC,xD,xE,xF,xK,xL,xO,xP],[0,0,0,0,0,0,0,0,0,0],'b')
# ax.add_patch(pat.Arc((xM,0),width=2*(l7+r6),height=2*(l7+r6),theta1=0,theta2=90,color='b'))
# ax.plot([xM,xM],[rQ,rM],color='b')
# ax.add_patch(pat.Arc((xM-rLip2,rM),width=2*rLip2,height=2*rLip2,theta1=270,theta2=alpha4*pi/180,color='b'))
# ax.plot([xMM,xL,xK,xI],[rMM,rL,rK,rI],color='b')
# ax.add_patch(pat.Arc((xH+rLip2,rH),width=2*rLip2,height=2*rLip2,theta2=270+alpha3*pi/180.0,theta1=180.0,color='b'))
# ax.plot([xH,xG,xJ,xE],[rH,rG,rJ,rE],color='b')
# ax.add_patch(pat.Arc((xE-rLip1,rE),width=2*rLip1,height=2*rLip1,theta2=0,theta1=270-alpha2*pi/180,color='b'))
# ax.plot([xEE,xD,xC,xB,xA,xA],[rEE,rD,rC,rB,rA,0],color='b')

# In[4]:


from ofblockmeshdicthelper import *


# In[5]:


bmd = BlockMeshDict()
bmd.set_metric('mm')


# In[6]:


basevs = [
    Vertex(xA, 0.0, 0.0, 'vA0'),
    Vertex(xB, 0.0, 0.0, 'vB0'),
    Vertex(xC, 0.0, 0.0, 'vC0'),
    Vertex(xD, 0.0, 0.0, 'vD0'),
    #Vertex(xE, 0, 0, 'vE0'),
    Vertex(xEE, 0.0, 0.0, 'vEE0'),
    Vertex(xF, 0.0, 0.0, 'vF0'),        
    Vertex(xK, 0.0, 0.0, 'vK0'),
    Vertex(xL, 0.0, 0.0, 'vL0'),
    #Vertex(xM, 0, 0, 'vM0'),
    Vertex(xMM, 0.0, 0.0, 'vMM0'),
    #Vertex(xMMM, 0, 0, 'vMMM0'),
    Vertex(xO, 0.0, 0.0, 'vO0'),
    #Vertex(xOO, 0, 0, 'vOO0'),
    Vertex(xP, 0.0, 0.0, 'vP0'),
    #Vertex(xEEE, 0, 0, 'vEEE0'),
    #Vertex(xFF, 0, 0, 'vFF0'),
    #Vertex(xG, 0, 0, 'vG0'),
    #Vertex(xH, 0, 0, 'vH0'),
    #Vertex(xHH, 0, 0, 'vHH0'),
    #Vertex(xI, 0, 0, 'vI0'),
    #Vertex(xJ, 0, 0, 'vJ0'),
    #Vertex(xJJ, 0, 0, 'vJJ0'),
    #Vertex(xJJJ, 0, 0, 'vJJJ0'),
    #Vertex(xQ, 0, 0, 'vQ0'),
    #Vertex(xQQ, 0, 0, 'vQQ0'),
    Vertex(xA, rA, 0.0, 'vA1'),
    Vertex(xB, rB, 0.0, 'vB1'),
    Vertex(xC, rC, 0.0, 'vC1'),
    Vertex(xD, rD, 0.0, 'vD1'),
    Vertex(xE, rE, 0.0, 'vE1'),
    Vertex(xEE, rEE, 0.0, 'vEE1'),
    Vertex(xEEE, rEEE, 0.0, 'vEEE1'),
    Vertex(xF, rF, 0.0, 'vF1'),
    Vertex(xFF, rFF, 0.0, 'vFF1'),
    Vertex(xG, rG, 0.0, 'vG1'),
    Vertex(xH, rH, 0.0, 'vH1'),
    Vertex(xHH, rHH, 0.0, 'vHH1'),
    Vertex(xI, rI, 0.0, 'vI1'),
    Vertex(xJ, rJ, 0.0, 'vJ1'),
    Vertex(xJJ, rJJ, 0.0, 'vJJ1'),
    Vertex(xJJJ, rJJJ, 0.0, 'vJJJ1'),
    Vertex(xK, rK, 0.0, 'vK1'),
    Vertex(xL, rL, 0.0, 'vL1'),
    Vertex(xM, rM, 0.0, 'vM1'),
    Vertex(xMM, rMM, 0.0, 'vMM1'),
    Vertex(xMMM, rMMM, 0.0, 'vMMM1'),
    Vertex(xO, rO, 0.0, 'vO1'),
    Vertex(xOO, rOO, 0.0, 'vOO1'),
    Vertex(xP, rP, 0.0, 'vP1'),
    Vertex(xQ, rQ, 0.0, 'vQ1'),
    Vertex(xQQ, rQQ, 0.0, 'vQQ1')
]

for v in basevs:
    bmd.add_vertex(v.x, v.y, 1, v.name+'+z')
    bmd.add_vertex(v.x,  v.y, 0, v.name+'-z')


# Utility to generate vertices names for blocks

# In[7]:


def vnamegen(x0y0, x1y0, x1y1, x0y1):
    return (x0y0+'-z', x0y1+'-z', x1y1+'-z', x1y0+'-z',
            x0y0+'+z', x0y1+'+z', x1y1+'+z', x1y0+'+z')


# In[8]:


b0 = bmd.add_hexblock(vnamegen('vA0', 'vA1', 'vB1', 'vB0'),
                      (b0N, rN, 1),
                      'b0',
                      grading=SimpleGrading(1,
                                            rGrading,
                                            1))

b1 = bmd.add_hexblock(vnamegen('vB0', 'vB1', 'vC1', 'vC0'),
                      (b1N, rN, 1),
                      'b1',
                      grading=SimpleGrading(1,
                                            rGrading,
                                            1))
b2 = bmd.add_hexblock(vnamegen('vC0', 'vC1', 'vD1', 'vD0'),
                      (b2N, rN, 1),
                      'b2',
                      grading=SimpleGrading(1,
                                            rGrading,
                                            1))
b3 = bmd.add_hexblock(vnamegen('vD0', 'vD1', 'vEE1', 'vEE0'),
                      (b3N, rN, 1),
                      'b3',
                      grading=SimpleGrading(1,
                                            rGrading,
                                            1))
b34 = bmd.add_hexblock(vnamegen('vEE0', 'vEE1', 'vE1', 'vF0'),
                      (b34N, rN, 1),
                      'b34',
                      grading=SimpleGrading(1,
                                            rGrading,
                                            1))
b4 = bmd.add_hexblock(vnamegen('vF0', 'vE1', 'vK1', 'vK0'),
                      (b4N, rN, 1),
                      'b4',
                      grading=SimpleGrading(rGradingInv,
                                            rGrading,
                                            1))
b5 = bmd.add_hexblock(vnamegen('vK0', 'vK1', 'vL1', 'vL0'),
                      (b5N, rN, 1),
                      'b5',
                      grading=SimpleGrading(1,
                                            rGrading,
                                            1))
b6 = bmd.add_hexblock(vnamegen('vL0', 'vL1', 'vMM1', 'vMM0'),
                      (b6N, rN, 1),
                      'b6',
                      grading=SimpleGrading(1,
                                            rGrading,
                                            1))
b67 = bmd.add_hexblock(vnamegen('vMM0', 'vMM1', 'vM1', 'vO0'),
                      (b67N, rN, 1),
                      'b67',
                      grading=SimpleGrading(1,
                                            rGrading,
                                            1))
b7 = bmd.add_hexblock(vnamegen('vO0', 'vM1', 'vQ1', 'vP0'),
                      (b7N, rN, 1),
                      'b7',
                      grading=SimpleGrading(rGradingInv,
                                            rGrading,
                                            1))
b8 = bmd.add_hexblock(vnamegen('vE1', 'vJJJ1', 'vI1', 'vK1'),
                      (b8N, \
                       2*rN, \
                       1),
                      'b8',
                      grading=EdgeGrading(rGradingInv,1,1,rGradingInv,
                                            rGradingInv,1,1,rGradingInv,
                                            1,1,1,1))
b9 = bmd.add_hexblock(vnamegen('vJJJ1', 'vJJ1', 'vH1', 'vI1'),
                      (b9N, rN, 1),
                      'b9',
                      grading=SimpleGrading(1,
                                            1,
                                            1))
b10 = bmd.add_hexblock(vnamegen('vJJ1', 'vJ1', 'vG1', 'vH1'),
                      (b10N, rN, 1),
                      'b10',
                      grading=SimpleGrading(1,
                                            1,
                                            1))


# In[9]:


bmd.add_arcedge(('vF0+z','vE1+z'),'edgeFE+z',Point(bmd.vertices['vFF1+z'].x,bmd.vertices['vFF1+z'].y,bmd.vertices['vFF1+z'].z))
bmd.add_arcedge(('vF0-z','vE1-z'),'edgeFE-z',Point(bmd.vertices['vFF1-z'].x,bmd.vertices['vFF1-z'].y,bmd.vertices['vFF1-z'].z))
bmd.add_arcedge(('vEE1+z','vE1+z'),'edgeEEE+z',Point(bmd.vertices['vEEE1+z'].x,bmd.vertices['vEEE1+z'].y,bmd.vertices['vEEE1+z'].z))
bmd.add_arcedge(('vEE1-z','vE1-z'),'edgeEEE-z',Point(bmd.vertices['vEEE1-z'].x,bmd.vertices['vEEE1-z'].y,bmd.vertices['vEEE1-z'].z))
bmd.add_arcedge(('vMM1+z','vM1+z'),'edgeMMM+z',Point(bmd.vertices['vMMM1+z'].x,bmd.vertices['vMMM1+z'].y,bmd.vertices['vMMM1+z'].z))
bmd.add_arcedge(('vMM1-z','vM1-z'),'edgeMMM-z',Point(bmd.vertices['vMMM1-z'].x,bmd.vertices['vMMM1-z'].y,bmd.vertices['vMMM1-z'].z))
bmd.add_arcedge(('vO0+z','vM1+z'),'edgeOM+z',Point(bmd.vertices['vOO1+z'].x,bmd.vertices['vOO1+z'].y,bmd.vertices['vOO1+z'].z))
bmd.add_arcedge(('vO0-z','vM1-z'),'edgeOM-z',Point(bmd.vertices['vOO1-z'].x,bmd.vertices['vOO1-z'].y,bmd.vertices['vOO1-z'].z))
bmd.add_arcedge(('vP0+z','vQ1+z'),'edgePQ+z',Point(bmd.vertices['vQQ1+z'].x,bmd.vertices['vQQ1+z'].y,bmd.vertices['vQQ1+z'].z))
bmd.add_arcedge(('vP0-z','vQ1-z'),'edgePQ-z',Point(bmd.vertices['vQQ1-z'].x,bmd.vertices['vQQ1-z'].y,bmd.vertices['vQQ1-z'].z))
bmd.add_arcedge(('vI1+z','vH1+z'),'edgeIH+z',Point(bmd.vertices['vHH1+z'].x,bmd.vertices['vHH1+z'].y,bmd.vertices['vHH1+z'].z))
bmd.add_arcedge(('vI1-z','vH1-z'),'edgeIH-z',Point(bmd.vertices['vHH1-z'].x,bmd.vertices['vHH1-z'].y,bmd.vertices['vHH1-z'].z))


# In[10]:


bmd.add_boundary('patch','axis', [i.face('s') for i in [                                                        b0,                                                        b1,                                                        b2,                                                        b3,                                                        b34,                                                        b4,                                                        b5,                                                        b6,                                                        b67,                                                        b7                                                       ]])
bmd.add_boundary('patch','inletMain',[b0.face('w')])
bmd.add_boundary('patch','outlet',[b7.face('e'),b7.face('n')])
bmd.add_boundary('patch','inletSecondary',[b10.face('n')])
bmd.add_boundary('wall','wallNozzle1', [i.face('n') for i in [b0,b1,b2,b3,b34]])
bmd.add_boundary('wall','wallInletSecondary', [i.face('w') for i in [b8,b9,b10]]+[b10.face('e')])
bmd.add_boundary('wall','wallDiffuser', [i.face('n') for i in [b5,b6,b67]]+[b8.face('e'),b9.face('e')])
bmd.add_boundary('patch','front', [i.face('t') for i in bmd.blocks.values()])
bmd.add_boundary('patch','back', [i.face('b') for i in bmd.blocks.values()])


# In[11]:


# prepare for output
bmd.assign_vertexid()


# In[12]:


# output
print(bmd.format())


# print(bmd.format(),file=open("testExtrudeMesh/system/blockMeshDict",'w'))

# In[ ]:




