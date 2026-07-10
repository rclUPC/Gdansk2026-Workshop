// Parametrized test case for the ERCOFTAC diffuser.

//         Created by Omar Bounous 

//Run using:
//m4 -P blockMeshDict.m4 > blockMeshDict

//m4 definitions:
m4_changecom(//)m4_changequote([,])
m4_define(calc, [m4_esyscmd(perl -e 'use Math::Trig; printf ($1)')])
m4_define(VCOUNT, 0)
m4_define(vlabel, [[// ]Vertex $1 = VCOUNT m4_define($1, VCOUNT)m4_define([VCOUNT], m4_incr(VCOUNT))])

//Mathematical constants:
m4_define(pi, 3.1415926536)

//Geometry
m4_define(closingAngle, 9.0)
m4_define(openingAngle, 15.5)
m4_define(wedgeAngle, 5.0)
m4_define(extensionLength, 11.5)
m4_define(nozzleLength, 38.41)
m4_define(channelLength, 7.15)
m4_define(diffuserLength, 5.44)
m4_define(rLip1, 0.5)
m4_define(angleLip1, calc(90.0-openingAngle))
m4_define(diffuserLengthLip, calc(diffuserLength-rLip1*(1-sin(openingAngle*pi/180.0))))
m4_define(rIn,7.425)
m4_define(rCh,1.375)
m4_define(rOut, calc(rCh+diffuserLengthLip*tan(openingAngle*pi/180.0)+rLip1*cos(openingAngle*pi/180.0)))

m4_define(rCollectorBottom, 17.5)
m4_define(rCollectorTop, 34.5)
m4_define(separation, 0.5)
m4_define(rCh2, 4.25)  //PARAMETER
m4_define(nozzle2Length, 21.91)
m4_define(closingAngle2, 10.0) //PARAMETER
m4_define(rLip2, 4.5)
m4_define(angleLip2, calc(90.0-closingAngle2))
m4_define(nozzle2LengthLip, calc(nozzle2Length-rLip2*(1-sin(closingAngle2*pi/180.0))))
m4_define(openingAngle2, 3.0)
m4_define(total2Length, 155.0)
m4_define(channel2Length, 58.29)  //PARAMETER
m4_define(diffuser2Length, calc(total2Length-nozzle2Length-channel2Length))
m4_define(diffuser2LengthLip, calc(diffuser2Length-rLip2*(1-sin(openingAngle2*pi/180.0))))
m4_define(rOut2, calc(rCh2+diffuser2LengthLip*tan(openingAngle2*pi/180.0)+rLip2*cos(openingAngle2*pi/180.0)))

m4_define(exitLength, 100.0)



//Grid points (integers!):
m4_define(n, 25)
m4_define(rNumberOfCells, n)
m4_define(xABnumberOfCells, n)
m4_define(xBCnumberOfCells, calc(3*n))
m4_define(xCDnumberOfCells, n)
m4_define(xDEnumberOfCells, n)
m4_define(xEFnumberOfCells, calc(int(n/2)))
m4_define(xFKnumberOfCells, calc(3*n))
m4_define(xKLnumberOfCells, calc(4*n)) //Second channel
m4_define(xLMnumberOfCells, calc(4*n)) //Second diffuser
m4_define(xMOnumberOfCells, n) //Second diffuser exit
m4_define(xExitnumberOfCells, calc(2*n))
m4_define(rGrading, 0.2)
m4_define(rGradingInv, calc(1/rGrading))

//Plane A:
m4_define(xA, 0)
m4_define(rA, rIn)

//Plane B:
m4_define(xB, extensionLength)
m4_define(rB, rIn)

//Plane C:
m4_define(xC, calc(extensionLength+nozzleLength))
m4_define(rC, rCh)

//Plane D:
m4_define(xD, calc(extensionLength+nozzleLength+channelLength))
m4_define(rD, rCh)

//Plane E:
m4_define(xE, calc(extensionLength+nozzleLength+channelLength+diffuserLength))
m4_define(rE, rOut)

m4_define(xEE, calc(xD+diffuserLengthLip))
m4_define(rEE, calc(rCh+diffuserLengthLip*tan(openingAngle*pi/180.0)))

m4_define(xEEE, calc(xE-rLip1*(1-cos(angleLip1/2*pi/180.0))))
m4_define(rEEE, calc(rOut-rLip1*sin(angleLip1/2*pi/180.0)))

//Plane F:
m4_define(xF, calc(xE+rOut/2))
m4_define(rF, 0)

m4_define(xFF, calc(xF-0.167*rOut))
m4_define(rFF, calc(0.588*rOut))

//Plane G:
m4_define(xG, calc(xE+separation))
m4_define(rG, rCollectorBottom)
m4_define(xH, xG)
m4_define(xI, calc(xH+rLip2*(1-sin(closingAngle2*pi/180.0))))
m4_define(rI, calc(rCh2+nozzle2LengthLip*tan(closingAngle2*pi/180.0)))
m4_define(rH, calc(rI+rLip2*cos(closingAngle2*pi/180.0)))
m4_define(xHH, calc(xH+rLip2*(1-cos(angleLip2/2*pi/180.0))))
m4_define(rHH, calc(rH-rLip2*sin(angleLip2/2*pi/180.0)))

m4_define(xJ, 27.0)
m4_define(rJ, rCollectorBottom)
m4_define(xJJ, calc(xE-2*(xE-xJ)/3))
m4_define(rJJ, calc(rE+2*(rJ-rE)/3))
m4_define(xJJJ, calc(xE-(xE-xJ)/4))
m4_define(rJJJ, calc(rE+(rJ-rE)/4))


m4_define(xK, calc(xH+nozzle2Length))
m4_define(rK, rCh2)

m4_define(xL, calc(xK+channel2Length))
m4_define(rL, rCh2)

m4_define(xM, calc(xL+diffuser2Length))
m4_define(rM, rOut2)

m4_define(xMM, calc(xL+diffuser2LengthLip))
m4_define(rMM, calc(rCh2+diffuser2LengthLip*tan(openingAngle2*pi/180.0)))

m4_define(xMMM, calc(xM-rLip2*(1-cos(angleLip2/2*pi/180.0))))
m4_define(rMMM, calc(rOut2-rLip2*sin(angleLip2/2*pi/180.0)))

m4_define(xO, calc(xM+rOut2))
m4_define(rO, 0)
m4_define(xOO, calc(xM+rOut2*cos(pi/4)))
m4_define(rOO, calc(rOut2*sin(pi/4)))

m4_define(xP, calc(xO+exitLength))
m4_define(rP, 0)
m4_define(rQ, calc(rM+exitLength))
m4_define(xQ, xM)
m4_define(xQQ, calc(xM+(rOut2+exitLength)*cos(pi/4)))
m4_define(rQQ, calc((rOut2+exitLength)*sin(pi/4)))


/*---------------------------------------------------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  1.5                                   |
|   \\  /    A nd           | Web:      http://www.openfoam.org               |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

FoamFile
{
    version         2.0;
    format          ascii;

    root            "";
    case            "";
    instance        "";
    local           "";

    class           dictionary;
    object          blockMeshDict;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

convertToMeters 0.001;

vertices
(
//Plane A:
(xA 0 0) vlabel(A0)
(xA calc(rA*cos((wedgeAngle/2)*pi/180.0)) -calc(rA*sin((wedgeAngle/2)*pi/180.0))) vlabel(A1)
(xA calc(rA*cos((wedgeAngle/2)*pi/180.0)) calc(rA*sin((wedgeAngle/2)*pi/180.0))) vlabel(A2)

//Plane B:
(xB 0 0) vlabel(B0)
(xB calc(rB*cos((wedgeAngle/2)*pi/180.0)) -calc(rB*sin((wedgeAngle/2)*pi/180.0))) vlabel(B1)
(xB calc(rB*cos((wedgeAngle/2)*pi/180.0)) calc(rB*sin((wedgeAngle/2)*pi/180.0))) vlabel(B2)

//Plane C:
(xC 0 0) vlabel(C0)
(xC calc(rC*cos((wedgeAngle/2)*pi/180.0)) -calc(rC*sin((wedgeAngle/2)*pi/180.0))) vlabel(C1)
(xC calc(rC*cos((wedgeAngle/2)*pi/180.0)) calc(rC*sin((wedgeAngle/2)*pi/180.0))) vlabel(C2)

//Plane D:
(xD 0 0) vlabel(D0)
(xD calc(rD*cos((wedgeAngle/2)*pi/180.0)) -calc(rD*sin((wedgeAngle/2)*pi/180.0))) vlabel(D1)
(xD calc(rD*cos((wedgeAngle/2)*pi/180.0)) calc(rD*sin((wedgeAngle/2)*pi/180.0))) vlabel(D2)

//Plane E:
(xE 0 0) vlabel(E0)
(xE calc(rE*cos((wedgeAngle/2)*pi/180.0)) -calc(rE*sin((wedgeAngle/2)*pi/180.0))) vlabel(E1)
(xE calc(rE*cos((wedgeAngle/2)*pi/180.0)) calc(rE*sin((wedgeAngle/2)*pi/180.0))) vlabel(E2)

(xEE 0 0) vlabel(EE0)
(xEE calc(rEE*cos((wedgeAngle/2)*pi/180.0)) -calc(rEE*sin((wedgeAngle/2)*pi/180.0))) vlabel(EE1)
(xEE calc(rEE*cos((wedgeAngle/2)*pi/180.0)) calc(rEE*sin((wedgeAngle/2)*pi/180.0))) vlabel(EE2)

(xEEE 0 0) vlabel(EEE0)
(xEEE calc(rEEE*cos((wedgeAngle/2)*pi/180.0)) -calc(rEEE*sin((wedgeAngle/2)*pi/180.0))) vlabel(EEE1)
(xEEE calc(rEEE*cos((wedgeAngle/2)*pi/180.0)) calc(rEEE*sin((wedgeAngle/2)*pi/180.0))) vlabel(EEE2)

//Plane F:
(xF 0 0) vlabel(F0)
(xF calc(rF*cos((wedgeAngle/2)*pi/180.0)) -calc(rF*sin((wedgeAngle/2)*pi/180.0))) vlabel(F1)
(xF calc(rF*cos((wedgeAngle/2)*pi/180.0)) calc(rF*sin((wedgeAngle/2)*pi/180.0))) vlabel(F2)

(xFF 0 0) vlabel(FF0)
(xFF calc(rFF*cos((wedgeAngle/2)*pi/180.0)) -calc(rFF*sin((wedgeAngle/2)*pi/180.0))) vlabel(FF1)
(xFF calc(rFF*cos((wedgeAngle/2)*pi/180.0)) calc(rFF*sin((wedgeAngle/2)*pi/180.0))) vlabel(FF2)


//Plane G:
(xG 0 0) vlabel(G0)
(xG calc(rG*cos((wedgeAngle/2)*pi/180.0)) -calc(rG*sin((wedgeAngle/2)*pi/180.0))) vlabel(G1)
(xG calc(rG*cos((wedgeAngle/2)*pi/180.0)) calc(rG*sin((wedgeAngle/2)*pi/180.0))) vlabel(G2)

(xH 0 0) vlabel(H0)
(xH calc(rH*cos((wedgeAngle/2)*pi/180.0)) -calc(rH*sin((wedgeAngle/2)*pi/180.0))) vlabel(H1)
(xH calc(rH*cos((wedgeAngle/2)*pi/180.0)) calc(rH*sin((wedgeAngle/2)*pi/180.0))) vlabel(H2)

(xI 0 0) vlabel(I0)
(xI calc(rI*cos((wedgeAngle/2)*pi/180.0)) -calc(rI*sin((wedgeAngle/2)*pi/180.0))) vlabel(I1)
(xI calc(rI*cos((wedgeAngle/2)*pi/180.0)) calc(rI*sin((wedgeAngle/2)*pi/180.0))) vlabel(I2)

(xJ 0 0) vlabel(J0)
(xJ calc(rJ*cos((wedgeAngle/2)*pi/180.0)) -calc(rJ*sin((wedgeAngle/2)*pi/180.0))) vlabel(J1)
(xJ calc(rJ*cos((wedgeAngle/2)*pi/180.0)) calc(rJ*sin((wedgeAngle/2)*pi/180.0))) vlabel(J2)

(xK 0 0) vlabel(K0)
(xK calc(rK*cos((wedgeAngle/2)*pi/180.0)) -calc(rK*sin((wedgeAngle/2)*pi/180.0))) vlabel(K1)
(xK calc(rK*cos((wedgeAngle/2)*pi/180.0)) calc(rK*sin((wedgeAngle/2)*pi/180.0))) vlabel(K2)

(xJJ 0 0) vlabel(JJ0)
(xJJ calc(rJJ*cos((wedgeAngle/2)*pi/180.0)) -calc(rJJ*sin((wedgeAngle/2)*pi/180.0))) vlabel(JJ1)
(xJJ calc(rJJ*cos((wedgeAngle/2)*pi/180.0)) calc(rJJ*sin((wedgeAngle/2)*pi/180.0))) vlabel(JJ2)

(xJJJ 0 0) vlabel(JJJ0)
(xJJJ calc(rJJJ*cos((wedgeAngle/2)*pi/180.0)) -calc(rJJJ*sin((wedgeAngle/2)*pi/180.0))) vlabel(JJJ1)
(xJJJ calc(rJJJ*cos((wedgeAngle/2)*pi/180.0)) calc(rJJJ*sin((wedgeAngle/2)*pi/180.0))) vlabel(JJJ2)

(xL 0 0) vlabel(L0)
(xL calc(rL*cos((wedgeAngle/2)*pi/180.0)) -calc(rL*sin((wedgeAngle/2)*pi/180.0))) vlabel(L1)
(xL calc(rL*cos((wedgeAngle/2)*pi/180.0)) calc(rL*sin((wedgeAngle/2)*pi/180.0))) vlabel(L2)

(xM 0 0) vlabel(M0)
(xM calc(rM*cos((wedgeAngle/2)*pi/180.0)) -calc(rM*sin((wedgeAngle/2)*pi/180.0))) vlabel(M1)
(xM calc(rM*cos((wedgeAngle/2)*pi/180.0)) calc(rM*sin((wedgeAngle/2)*pi/180.0))) vlabel(M2)

(xMM 0 0) vlabel(MM0)
(xMM calc(rMM*cos((wedgeAngle/2)*pi/180.0)) -calc(rMM*sin((wedgeAngle/2)*pi/180.0))) vlabel(MM1)
(xMM calc(rMM*cos((wedgeAngle/2)*pi/180.0)) calc(rMM*sin((wedgeAngle/2)*pi/180.0))) vlabel(MM2)

(xMMM 0 0) vlabel(MMM0)
(xMMM calc(rMMM*cos((wedgeAngle/2)*pi/180.0)) -calc(rMMM*sin((wedgeAngle/2)*pi/180.0))) vlabel(MMM1)
(xMMM calc(rMMM*cos((wedgeAngle/2)*pi/180.0)) calc(rMMM*sin((wedgeAngle/2)*pi/180.0))) vlabel(MMM2)

(xO 0 0) vlabel(O0)
(xO calc(rO*cos((wedgeAngle/2)*pi/180.0)) -calc(rO*sin((wedgeAngle/2)*pi/180.0))) vlabel(O1)
(xO calc(rO*cos((wedgeAngle/2)*pi/180.0)) calc(rO*sin((wedgeAngle/2)*pi/180.0))) vlabel(O2)

(xOO 0 0) vlabel(OO0)
(xOO calc(rOO*cos((wedgeAngle/2)*pi/180.0)) -calc(rOO*sin((wedgeAngle/2)*pi/180.0))) vlabel(OO1)
(xOO calc(rOO*cos((wedgeAngle/2)*pi/180.0)) calc(rOO*sin((wedgeAngle/2)*pi/180.0))) vlabel(OO2)

(xP 0 0) vlabel(P0)
(xP calc(rP*cos((wedgeAngle/2)*pi/180.0)) -calc(rP*sin((wedgeAngle/2)*pi/180.0))) vlabel(P1)
(xP calc(rP*cos((wedgeAngle/2)*pi/180.0)) calc(rP*sin((wedgeAngle/2)*pi/180.0))) vlabel(P2)

(xQ 0 0) vlabel(Q0)
(xQ calc(rQ*cos((wedgeAngle/2)*pi/180.0)) -calc(rQ*sin((wedgeAngle/2)*pi/180.0))) vlabel(Q1)
(xQ calc(rQ*cos((wedgeAngle/2)*pi/180.0)) calc(rQ*sin((wedgeAngle/2)*pi/180.0))) vlabel(Q2)

(xQQ 0 0) vlabel(QQ0)
(xQQ calc(rQQ*cos((wedgeAngle/2)*pi/180.0)) -calc(rQQ*sin((wedgeAngle/2)*pi/180.0))) vlabel(QQ1)
(xQQ calc(rQQ*cos((wedgeAngle/2)*pi/180.0)) calc(rQQ*sin((wedgeAngle/2)*pi/180.0))) vlabel(QQ2)

);

// Defining blocks:
blocks
(
    //Blocks between plane A and plane B:
    // block0 
    hex (A0 B0 B1 A1 A0 B0 B2 A2) AB
    (xABnumberOfCells rNumberOfCells 1) 
    simpleGrading (1 rGrading 1)

    //Blocks between plane B and plane C:
    // block1
    hex (B0 C0 C1 B1 B0 C0 C2 B2) BC
    (xBCnumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)
    
    //Blocks between plane C and plane D:
    // block2
    hex (C0 D0 D1 C1 C0 D0 D2 C2) CD
    (xCDnumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)
    
    //Blocks between plane D and plane E:
    // block3
    hex (D0 EE0 EE1 D1 D0 EE0 EE2 D2) DEE
    (xDEnumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)
    
    //Blocks between plane E and plane F:
    // block4
    hex (EE0 F0 E1 EE1 EE0 F0 E2 EE2) EF
    (xEFnumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)
 

    // New blocks in the exit of diffuser and inlet of nozzle   
    hex (F0 K0 K1 E1 F0 K0 K2 E2) FK
    (xFKnumberOfCells rNumberOfCells 1)
    simpleGrading (rGradingInv rGrading 1)

    hex (E1 K1 I1 JJJ1 E2 K2 I2 JJJ2) FK
    (xFKnumberOfCells rNumberOfCells 1)
    edgeGrading (rGradingInv 1 1 rGradingInv 1 1 1 1 1 1 1 1)

    hex (JJJ1 I1 H1 JJ1 JJJ2 I2 H2 JJ2) FK
    (xFKnumberOfCells rNumberOfCells 1)
    simpleGrading (1 1 1)


    //Blocks in second channel
    hex (JJ1 H1 G1 J1 JJ2 H2 G2 J2) FK
    (xFKnumberOfCells rNumberOfCells 1)
    simpleGrading (1 1 1)

    hex (K0 L0 L1 K1 K0 L0 L2 K2) KL
    (xKLnumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)


    hex (L0 MM0 MM1 L1 L0 MM0 MM2 L2) LMM
    (xLMnumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)
    
    //Blocks between plane E and plane F:
    // block0
    hex (MM0 O0 M1 MM1 MM0 O0 M2 MM2) MO
    (xMOnumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)
 

    hex (O0 P0 Q1 M1 O0 P0 Q2 M2) OP
    (xExitnumberOfCells rNumberOfCells 1)
    simpleGrading (calc(1/rGrading) rGrading 1)
   
);

edges
(
    //Plane A:
    line A0 A1 
    arc A1 A2 (xA rA 0)
    line A2 A0

    //Plane B:
    line B0 B1
    arc B1 B2 (xB rB 0)
    line B2 B0

    //Plane C:
    line C0 C1
    arc C1 C2 (xC rC 0)
    line C2 C0

    //Plane D:
    line D0 D1
    arc D1 D2 (xD rD 0)
    line D2 D0

    //Plane E:
    line E0 E1
    arc E1 E2 (xE rE 0)
    line E2 E0

    arc EE1 E1 (xEEE calc(rEEE*cos((wedgeAngle/2)*pi/180.0)) -calc(rEEE*sin((wedgeAngle/2)*pi/180.0)))
    arc EE2 E2 (xEEE calc(rEEE*cos((wedgeAngle/2)*pi/180.0)) calc(rEEE*sin((wedgeAngle/2)*pi/180.0)))

    //Plane F:
    arc F0 E1 (xFF calc(rFF*cos((wedgeAngle/2)*pi/180.0)) -calc(rFF*sin((wedgeAngle/2)*pi/180.0)))
    arc FF1 FF2 (xFF rFF 0)
    arc E2 F0 (xFF calc(rFF*cos((wedgeAngle/2)*pi/180.0)) calc(rFF*sin((wedgeAngle/2)*pi/180.0)))

    arc I1 H1 (xHH calc(rHH*cos((wedgeAngle/2)*pi/180.0)) -calc(rHH*sin((wedgeAngle/2)*pi/180.0)))
    arc I2 H2 (xHH calc(rHH*cos((wedgeAngle/2)*pi/180.0)) calc(rHH*sin((wedgeAngle/2)*pi/180.0)))

    arc MM1 M1 (xMMM calc(rMMM*cos((wedgeAngle/2)*pi/180.0)) -calc(rMMM*sin((wedgeAngle/2)*pi/180.0)))
    arc MM2 M2 (xMMM calc(rMMM*cos((wedgeAngle/2)*pi/180.0)) calc(rMMM*sin((wedgeAngle/2)*pi/180.0)))

    arc O0 M1 (xOO calc(rOO*cos((wedgeAngle/2)*pi/180.0)) -calc(rOO*sin((wedgeAngle/2)*pi/180.0)))
    arc OO1 OO2 (xOO rOO 0)
    arc O0 M2 (xOO calc(rOO*cos((wedgeAngle/2)*pi/180.0)) calc(rOO*sin((wedgeAngle/2)*pi/180.0)))

    arc P0 Q1 (xQQ calc(rQQ*cos((wedgeAngle/2)*pi/180.0)) -calc(rQQ*sin((wedgeAngle/2)*pi/180.0)))
    arc QQ1 QQ2 (xQQ rQQ 0)
    arc P0 Q2 (xQQ calc(rQQ*cos((wedgeAngle/2)*pi/180.0)) calc(rQQ*sin((wedgeAngle/2)*pi/180.0)))

);

// Defining patches:
patches
(
    empty axis
    (
        (A0 B0 B0 A0)
        (B0 C0 C0 B0)
        (C0 D0 D0 C0)
        (D0 EE0 EE0 D0)
        (EE0 F0 F0 EE0)
        (F0 K0 K0 F0)
        (K0 L0 L0 K0)
        (L0 MM0 MM0 L0)
        (MM0 O0 O0 MM0)
        (O0 P0 P0 O0)
    )
    patch inletMain
    (
       (A0 A2 A1 A0)
    )
    patch outlet
    (
       (P0 Q1 Q2 P0)
       (M1 Q1 Q2 M2)
    )
    patch inletSecondary
    (
        (J1 J2 G2 G1)
    )
    wall wallNozzle1
    (
      (A1 A2 B2 B1)
      (B1 B2 C2 C1)
      (C1 C2 D2 D1)
      (D1 D2 EE2 EE1)
      (EE1 EE2 E2 E1)
    )
    wall wallInletSecondary
    (
      (E1 E2 JJJ2 JJJ1)
      (JJJ1 JJJ2 JJ2 JJ1)
      (JJ1 JJ2 J2 J1)
      (H1 H2 G2 G1)
    )
    wall wallDiffuser
    (
      (I1 I2 H2 H1)
      (K1 K2 I2 I1)
      (L1 L2 K2 K1)
      (MM1 MM2 L2 L1)
      (M1 M2 MM2 MM1)
    )
    wedge back
    (
      (A0 A1 B1 B0)
      (B0 B1 C1 C0)
      (C0 C1 D1 D0)
      (D0 D1 EE1 EE0)
      (EE0 EE1 E1 F0)
      (F0 E1 K1 K0)
      (E1 JJJ1 I1 K1)
      (JJJ1 JJ1 H1 I1)
      (JJ1 J1 G1 H1)
      (K0 K1 L1 L0)
      (L0 L1 MM1 MM0)
      (MM0 MM1 M1 O0)
      (O0 M1 Q1 P0)
    )
    wedge front
    (
      (A0 A2 B2 B0)
      (B0 B2 C2 C0)
      (C0 C2 D2 D0)
      (D0 D2 EE2 EE0)
      (EE0 EE2 E2 F0)
      (F0 E2 K2 K0)
      (E2 JJJ2 I2 K2)
      (JJJ2 JJ2 H2 I2)
      (JJ2 J2 G2 H2)
      (K0 K2 L2 L0)
      (L0 L2 MM2 MM0)
      (MM0 MM2 M2 O0)
      (O0 M2 Q2 P0)
    )
 
);

mergePatchPairs 
(
);

// ************************************************************************* //
