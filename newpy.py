import math
import numpy as np
class baseplate:
    Pd=0
    Pl=0
    Md=0
    Ml=0
    d=0
    bf=0
    A=0
    Fy=0
    fc=0
    

    def __init__(self):
        print ("enter deadload:")
        self.Pd= float(input())
        print ("enter liveload:")
        self.Pl= float(input())
        print ("enter deadmoment:")
        self.Md= float(input())
        print ("enter livemoment:")
        self.Ml= float(input())
        print("enter width of flange")
        self.bf= float(input())
        print("enter d of section")
        self.d= float(input())
        print("enter compression strength of concrete")
        self.fc= float(input())
        #A barabare nesbate A2 be A1 ast
        print("enter A2/A1:")
        self.A= float(input())
        print("enter Fy:")
        self.Fy= float(input())
        
        
    def calc (self):
        Mu = self.Md * 1.2+self.Ml*1.6
        Pu = self.Pd*1.2 + self.Pl*1.6
        e=Mu/Pu
    #farz minkonim khamesh hole mehvare ghavi ast
        B = round(self.d+10)
        D = round(self.bf+10)
       
        
        Fpmax=Pu/(B*D)+6*Mu/(D*B*B)
        Fpmin=Pu/(B*D)-6*Mu/(D*B*B)
        Fp=0.65*0.85 *self.fc*math.sqrt(self.A)
        #agar Fpmax dar in baze gharar greft az negareshe dovom estefade mikonim

        if ((Fpmax <= Fp+0.1) and (Fpmax >= Fp-0.1)):
             print("enter distance of the center of anchor to the end of base plate")
             z=float(input())
             print("enter strength of anchor")
             fy=float(input())
             print("enter number of anchors on one side")
             na=float(input())
             f = B/2 - z
             fprim=0.5*Fp*D*(B/2+f)
             x1=(3*fprim+3*math.sqrt(fprim*fprim-(2/3)*D*(Pu*f+Mu)))/(Fp*D)
             x2=(3*fprim-3*math.sqrt(fprim*fprim-(2/3)*D*(Pu*f+Mu)))/(Fp*D)
             if ((x1>0) and (x1<B)):
                x=x1
             else:
                x=x2
             Tu = 0.5*Fp*x*D-Pu
             fut =0.75*0.75*fy
             As=Tu/fut
             if Tu>=0 :
                r=0
                while (r< math.sqrt(As/(3.14*na))):
                    r=r+0.25
                phiNp=0.7 * 1*2*3.14*r*r*8*self.fc
                if (Tu/(6*phiNp)<=1.1):
                    print("-----> the elongation of anchors is fine")
                m=(B-0.95*self.d)/2
                n=(D-0.8*self.bf)/2
                fup1 = Fpmax * (x-m)/x
                qup1=(fup1+Fpmax)/2
                Mu1=Fpmax*m*m/3+fup1*m*m/6
                Mu2=qup1*m*n/2
                Vu1=(fup1+Fpmax)/2*m
                Vu2=qup1*n/2
                tp=max(2.11 * math.sqrt(max(Mu1,Mu2)/self.Fy),max(Vu1,Vu2)/(0.6*self.Fy))
                print("PL ",B,"*",D,"*",round(tp))
                print(2*na,"anchors on two sides of baseplate.  ",r," in - diameter rods (Grade",fy,")")
             else:
                m=(B-0.95*self.d)/2
                n=(D-0.8*self.bf)/2
                fup1 = Fpmax * (x-m)/x
                qup1=(fup1+Fpmax)/2
                Mu1=Fpmax*m*m/3+fup1*m*m/6
                Mu2=qup1*m*n/2
                Vu1=(fup1+Fpmax)/2*m
                Vu2=qup1*n/2
                tp=max(2.11 * math.sqrt(max(Mu1,Mu2)/self.Fy),max(Vu1,Vu2)/(0.6*self.Fy))
                print("PL ",B,"*",D,"*",round(tp))
                print("4 3/4 in - diameter rods (Grade 36)")
            
        #az negareshe aval estefade mikonim     
        else :
            if e <= B/6:
                m=(B-0.95*self.d)/2
                n=(D-0.8*self.bf)/2
                fup1=Pu/(B*D)+Mu*(B/2 - m)/(D*(B*B*B)/12)
                qup1=0.5*(fup1+Fpmax)
                Mu1=Fpmax*m*m/3 + fup1*m*m/6
                Mu2=qup1*n*n/2
                Vu1=0.5*(fup1+Fpmax)*m
                Vu2=qup1*n*n
                
                tp=max(2.11 * math.sqrt(max(Mu1,Mu2)/self.Fy),max(Vu1,Vu2)/(0.6*self.Fy))
                print("PL ",B,"*",D,"*",round(tp))
                print("4 3/4 in - diameter rods (Grade 36)")
                
            else :
            #negareshe aval halate dovom
                print("enter distance of the center of anchor to the end of base plate")
                z=float(input())
                print("enter tf of section")
                tf=float(input())
                print("enter strength of anchor")
                fy=float(input())
                print("enter Es")
                Es=float(input())
                print("enter Ec")
                Ec=float(input())
                print("enter number of anchors on one side")
                na=float(input())
                
                f = B/2 - z
                h = self.d - 2*tf
                Tu =(Mu-Pu*h/2)/(f+h/2)
                fut =0.75*0.75*fy
                As=Tu/fut
                r=0
                while (r<math.sqrt(As/(3.14*na))):
                    r=r+0.25
                n1=Es/Ec
                a1=3*(e-B/2)
                a2=6*(n1*na*3.14*r*r/D)*(f+e)
                a3=-a2*(B/2+f)
                arrayin=[1,a1,a2,a3]
                arrayout=np.roots(arrayin)
                s1=float(arrayout[0])
                s2=float(arrayout[1])
                s3=float(arrayout[2])
                
                if ((s1 > 0) and (s1<B)):
                    sa = s1
                elif ((s2 > 0) and (s2<B)):
                    sa=s2
                elif ((s3 > 0) and (s3<B)):
                    sa=s3
                
                Tu = Pu *(e+sa/3-B/2)/(B/2+f-sa/3)
              
                if ((Tu/(na*3.14*r*r))<= fut):
                    print("----> the tensile tension in anchors is fine")
                fpmax=(2*Pu*(e+f))/(sa*D*(B/2+f-sa/3))
                if(fpmax<Fp ):
                    print("-----> compression tension at the end of baseplate is less than  compression strength of concrete")
                    
                    
                phiNp=0.7 * 1*2*3.14*r*r*8*self.fc
                if (Tu/(6*phiNp)<=1.1):
                    print("-----> the elongation of anchors is fine")
                m=(B-0.95*self.d)/2
                n=(D-0.8*self.bf)/2    
                fup1 = fpmax * (sa-m)/sa
                qup1=(fup1+fpmax)/2
                Mu1=fpmax*m*m/3+fup1*m*m/6
                Mu2=qup1*m*n/2
                Vu1=(fup1+fpmax)/2*m
                Vu2=qup1*n/2
                tp=max(2.11 * math.sqrt(max(Mu1,Mu2)/self.Fy),max(Vu1,Vu2)/(0.6*self.Fy))
                print("PL ",B,"*",D,"*",round(tp))
                print(2*na,"anchors on two sides of baseplate.  ",r," in - diameter rods (Grade",fy,")")
    
    
samp = baseplate()
samp.calc()    