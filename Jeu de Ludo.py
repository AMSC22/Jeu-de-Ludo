#! /usr/bin/env python3
# coding: utf-8
from tkinter import*
from random import randrange
    
def out(word):
    fen1=Tk()
    fen1.title("Ludo Game")      # Donne le nom à la fenetre
    fen1.geometry("300x50")    # Donne une dimension fixe de la fenètre contenant le Ludo
    can1=Frame(fen1)
    chaine=Label(fen1)
    if(word=="o"):chaine.configure(text="Change Your Pawn")
    elif(type(word)==type(5)):
        if(word==1):chaine.configure(text="C'est celui de la maison Vert qui joue",fg="green")
        elif(word==2):chaine.configure(text="C'est celui de la maison Rouge qui joue",fg="red")
        elif(word==3):chaine.configure(text="C'est celui de la maison Bleue qui joue",fg="blue")
        elif(word==4):chaine.configure(text="C'est celui de la maison Jaune qui joue",fg="yellow")
    else:chaine.configure(text="Your have to play "+word+" before moving your Pawn")
    chaine.grid(pady=10,padx=10)
    can1.grid()
    return False

class Manip():
    def __init__(self,L=0,i=0,x=0,y=0,i1=0,a=56,b=56,c=56,d=56,a1=[]*4):
        self.d,self.i,self.x,self.y,self.i1,self.v,self.r,self.j,self.b,self.d1,self.d2,self.Case_Dé=L,i,x,y,i1,a,b,c,d,0,0,[0]
        self.Retour_en_arriere,self.Nombre_de_en_arriere,self.j1,self.Compteur,self.Prison,self.Case=[0],0,0,a1,1,False
        self.Pion_V,self.Pion_R,self.Pion_J,self.Pion_B,n,self.Pions_Sortir,k,self.x1,self.y1=[0]*5,[0]*5,[0]*5,[0]*5,70,[0],0,0,0
        self.V,self.V1,self.R,self.R1,self.J,self.J1,self.B,self.B1,self.Pio1,self.Pio2=[0]*5,[0],[0]*5,[0],[0]*5,[0],[0]*5,[0],0,0
        self.Option, self.Posi_PioV, self.Posi_PioR, self.Posi_PioJ, self.Posi_PioB="Sans_Prison",[0]*5,[0]*5,[0]*5,[0]*5
        self.Vx,self.Rx,self.Jx,self.Bx,self.Vy,self.Ry,self.Jy,self.By=[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n
        self.Nb_Jeu=0
        for i in [Co/2, Co*16.56]:
            for j in [Co*1.47, Co*10.47]:
                for k in range(4):
                    self.Pions_Sortir.append([i-r, j-r, i+r, j+r])
                    j+=Co*1.3
                    
    def __init1__(self):
        for i in range(0, Co*17, Co*16): self.Case_Dé.append([[Co*0.06+i,Co*0.06,Co*1.06+i,Co*1.06],[Co*1.06+i-Co/2,Co*1.06-Co/2],Co*0.06+i<=self.x1 and self.x1<=Co*1.06+i and Co*0.06<=self.y1 and self.y1<=Co*1.06])
        for i in range(0, Co*17, Co*16): self.Case_Dé.append([[Co*16.06-i,Co*14.06,Co*17.06-i,Co*15.06],[Co*17.06-i-Co/2,Co*15.06-Co/2],Co*16.06-i<=self.x1 and self.x1<=Co*17.06-i and Co*14.06<=self.y1 and self.y1<=Co*15.06])

    def Traçage_du_Tableau(self):
        for i in range(0,Co*16,Co):                      #-------------------------------------------------------------------------
            if(Co*6<=i and i<=Co*9):
                can.create_line(i+Co*1.06,0,i+Co*1.06,Co*6.06,fill="black",width=Co*0.06)
                can.create_line(Co*1.06,i+Co*0.06,Co*7.02,i+Co*0.06,fill="black",width=Co*0.06)
                can.create_line(i+Co*1.06,Co*9.06,i+Co*1.06,Co*15.06,fill="black",width=Co*0.06)  # Trace les lignes du Ludo
                can.create_line(Co*6.06,i+Co*0.06,Co*16.06,i+Co*0.06,fill="black",width=Co*0.06)
            else:
                can.create_line(i+Co*1.06,Co*6.06,i+Co*1.06,Co*9.06,fill="black",width=Co*0.06)
                can.create_line(Co*6.06,i+Co*0.06,Co*10.06,i+Co*0.06,fill="black",width=Co*0.06)
            if(i==Co*6 or i==Co*9 or i==0 or i==Co*15):
                can.create_line(i+Co*1.06,0,i+Co*1.06,Co*15.06,fill="black",width=Co*0.06)
                can.create_line(Co*1.06,i+Co*0.06,Co*16.06,i+Co*0.06,fill="black",width=Co*0.06) #---------------------------------------------------------------
        can.create_line(Co*7.06,Co*6.06,Co*10.06,Co*9.06,fill="black",width=Co*0.06)    #------------------------------------------------------
        can.create_line(Co*10.06,Co*6.06,Co*7.06,Co*9.06,fill="black",width=Co*0.06)
        for i in range(int(Co*1.46)):can.create_line(Co*7.1+i,Co*6.17+i,Co*7.1+i,Co*9-i,fill="dark green",width=Co*0.02) # Trace le carré du centre
        for i in range(int(Co*1.45)):can.create_line(Co*8.6+i,Co*7.57-i,Co*8.6+i,Co*7.6+i,fill="dark blue",width=Co*0.02)  # et le colorie
        for i in range(int(Co*1.51)):can.create_line(Co*7.12+i,Co*6.1+i,Co*10.02-i,Co*6.1+i,fill="dark red",width=Co*0.02)
        for i in range(2,int(Co*1.48)):can.create_line(Co*8.6-i,Co*7.57+i,Co*8.52+i,Co*7.57+i,fill="yellow",width=Co*0.02)    #--------------------------

        can.create_line(Co*4.06,Co*0.09,Co*4.06,Co*6.04,fill="dark green",width=Co*5.94)  #-----------------------------------------------
        can.create_line(Co*13.06,Co*0.09,Co*13.06,Co*6.04,fill="dark red",width=Co*5.94)
        can.create_line(Co*1.09,Co*12.06,Co*7+2,Co*12.06,fill="yellow",width=Co*5.94)
        can.create_line(Co*10.09,Co*12.06,Co*16.04,Co*12.06,fill="dark blue",width=Co*5.94)  # Trace chaque case avec leur

        can.create_line(Co*2.56,Co*6.08,Co*2.56,Co*7.04,fill="dark green",width=Co*0.96)                     # distinctif
        can.create_line(Co*9.08,Co*1.56,Co*10.04,Co*1.56,fill="dark red",width=Co*0.96)
        for i in range(0,Co*5,Co):
            can.create_line(Co*2.56+i,Co*7.08,Co*2.56+i,Co*8.04,fill="dark green",width=Co*0.96)
            can.create_line(Co*8.08,Co*1.56+i,Co*9.04,Co*1.56+i,fill="dark red",width=Co*0.96)

        can.create_line(Co*7.56,Co*13.08,Co*7.56,Co*14.04,fill="yellow",width=Co*0.96)
        can.create_line(Co*14.08,Co*8.56,Co*15.04,Co*8.56,fill="dark blue",width=Co*0.96)
        for i in range(Co*4,-Co,-Co):
            can.create_line(Co*8.56,Co*13.08-i,Co*8.56,Co*14.04-i,fill="yellow",width=Co*0.96)
            can.create_line(Co*14.08-i,Co*7.56,Co*15.04-i,Co*7.56,fill="dark blue",width=Co*0.96) #--------------------------------------------

    def Traçage_des_Pions(self):
        Class.Définir_Trajectoire()
        self.Compteur.sort()
        k=1                                                  #-------------------------------------------------------
        for j in range(0,Co*4,Co*3):
            for i in range(0,Co*4,Co*3):
                for i1 in self.Compteur:
                    if(i1==1):
                        VRJB=[Co*2.56-r+i,Co*1.56-r+j,Co*2.56+r+i,Co*1.56+r+j]
                        self.Pion_V[k]=can.create_oval(VRJB,fill="green")
                        self.V1.append(VRJB)
                        self.V[k]=VRJB
                    elif(i1==2):
                        VRJB=[Co*11.56-r+i,Co*1.56-r+j,Co*11.56+r+i,Co*1.56+r+j]
                        self.Pion_R[k]=can.create_oval(VRJB,fill="red")   # trace chaque pion
                        self.R1.append(VRJB)
                        self.R[k]=VRJB
                    elif(i1==4):
                        VRJB=[Co*2.56-r+i,Co*10.56-r+j,Co*2.56+r+i,Co*10.56+r+j]
                        self.Pion_J[k]=can.create_oval(VRJB,fill="yellow")  # et les colorie
                        self.J1.append(VRJB)
                        self.J[k]=VRJB
                    elif(i1==3):
                        VRJB=[Co*11.56-r+i,Co*10.56-r+j,Co*11.56+r+i,Co*10.56+r+j]
                        self.Pion_B[k]=can.create_oval(VRJB,fill="blue")
                        self.B1.append(VRJB)
                        self.B[k]=VRJB
                k+=1                                                        #----------------------------------------------
        Class.__init1__()
        self.Pio1, self.Pio2 = can.create_rectangle(self.Case_Dé[self.Compteur[0]][0],fill="white", width=Co*0.06), can.create_text(self.Case_Dé[self.Compteur[0]][1],text="Joué")

    def Deplacement_des_Pions(self):
        for i in range(1,5):
            can.coords(self.Pion_V[i],self.V[i])
            can.coords(self.Pion_R[i],self.R[i])
            can.coords(self.Pion_J[i],self.J[i])
            can.coords(self.Pion_B[i],self.B[i])

    def Sans_Prisonnement(self):
        if(self.Nombre_de_en_arriere-self.j1!=0 and self.Prison!=1):
            self.Option="Sans_Prison"
            Class.Out1()
        else:
            self.Prison=1

    def Avec_Prisonnement(self):
        if(self.Nombre_de_en_arriere-self.j1!=0 and self.Prison!=2):
            self.Option="Avec_Prison"
            Class.Out1()
        else:
            self.Prison=2
            
    def Marche_Arriere(self):
        self.j1+=len(self.Compteur)*4
        if(self.Nombre_de_en_arriere-self.j1>=0):
            k,k1=1,0
            for i in range(1,5):
                j=self.Nombre_de_en_arriere-self.j1+k
                for i1 in self.Compteur:
                    if(i1==1):self.V[i],k1=self.Retour_en_arriere[j+k1],k1+1
                    elif(i1==2):self.R[i],k1=self.Retour_en_arriere[j+k1],k1+1
                    elif(i1==4):self.J[i],k1=self.Retour_en_arriere[j+k1],k1+1
                    elif(i1==3):self.B[i],k1=self.Retour_en_arriere[j+k1],k1+1
                k,k1=k+len(self.Compteur),0
            Class.Deplacement_des_Pions()

    def Out(self):
        self.fen2=Tk()
        self.fen2.title("Ludo Game")      # Donne le nom à la fenetre
        self.fen2.geometry("300x70")    # Donne une dimension fixe de la fenètre contenant le Ludo
        can2=Frame(self.fen2)
        chaine=Label(self.fen2)
        chaine.configure(text="Voulez-vous vraimant recommencer le Jeu")
        chaine.grid(row=1,columnspan=2,pady=10,padx=10)
        Button(self.fen2,text="OUI",width=5,fg="maroon",command=Class.Recommencer).grid(row=2,column=1)
        Button(self.fen2,text="NON",width=5,fg="maroon",command=self.fen2.destroy).grid(row=2,column=2)
        can2.grid()

    def Out1(self):
        self.fen2=Tk()
        self.fen2.title("Ludo Game")      # Donne le nom à la fenetre
        self.fen2.geometry("470x90")    # Donne une dimension fixe de la fenètre contenant le Ludo
        can2=Frame(self.fen2)
        chaine=Label(self.fen2)
        if(self.Option=="Avec_Prison"):chaine.configure(text="Voulez-vous vraiment changer d'opion pour celui d'emprisonnement ?\n Si oui, Vous allez devoir recommenser votre Jeu.")
        elif(self.Option=="Sans_Prison"):chaine.configure(text="Voulez-vous vraiment changer d'opion pour celui Sans emprisonnement ?\n Si oui, Vous allez devoir recommenser votre Jeu.")
        chaine.grid(row=1,columnspan=2,pady=10,padx=10)
        Button(self.fen2,text="OUI",width=5,fg="maroon",command=Class.Recommencer).grid(row=2,column=1)
        Button(self.fen2,text="NON",width=5,fg="maroon",command=self.fen2.destroy).grid(row=2,column=2)
        can2.grid()
        
    def Recommencer(self):
        self.fen2.destroy()
        chaine1.configure(text="  ")
        can.delete(ALL)
        Class.Traçage_du_Tableau()
        Class.__init__(0,0,0,0,0,56,56,56,56,self.Compteur)
        Class.Traçage_des_Pions()    # Trace Chaque Pion
    
    def Lancez_le_Dé(self):
        #d=randrange(1,7)
        d=randrange(4,7)
        if(self.i1!=2 and self.d%6!=0):self.d=0
        if(d==6):self.d+=d
        elif(self.d!=0 and self.d%6==0 and d<6):self.d+=d
        else:self.d=d
        if(d==6):
            self.i+=1
            chaine1.configure(text="You played "+str(self.i)+" Chaine")
        elif(d<6 and self.i!=0):chaine1.configure(text="You played "+str(self.i)+" Chaine "+str(d))
        else:chaine1.configure(text="You played "+str(d))
        self.i1=1

    def Déplacement(self,Vx,Vy,d,i,T,v1,r1,b1,j1):
        if(v1!=0):V,R,J,B,a,R1,J1,B1,a1= self.V, self.R, self.J, self.B, v1, self.R1, self.J1,self.B1,v1
        elif(r1!=0):V,R,J,B,a,R1,J1,B1,a1 = self.R,self.V, self.J,self.B,r1,self.V1,self.J1,self.B1,r1+8
        elif(j1!=0):V,R,J,B,a,R1,J1,B1,a1 = self.J,self.V,self.R,self.B, j1, self.V1,self.R1,self.B1,j1+4
        elif(b1!=0):V,R,J,B,a,R1,J1,B1,a1 = self.B,self.V,self.R,self.J,b1,self.V1,self.R1,self.J1,b1+12
        if(d+i>56):
            V[a]=[Vx[i]-r,Vy[i]-r,Vx[i]+r,Vy[i]+r]
            T=out(str(56-i))
        elif(d+i==56):
            V[a],T=self.Pions_Sortir[a1],True
            #if(d+i==56 and d<6):self.d1+=1
        else:
            if(i==0 and d<6):V[a]=[Vx[i]-r,Vy[i]-r,Vx[i]+r,Vy[i]+r]
            elif(i==0 and d==6):V[a],T=[Vx[i+1]-r,Vy[i+1]-r,Vx[i+1]+r,Vy[i+1]+r],True
            elif(i!=0):
                V[a],T=[Vx[i+d]-r,Vy[i+d]-r,Vx[i+d]+r,Vy[i+d]+r],True
                #if(0<d and d<6):self.d1+=1
                for j in range(1,5):
                    if(V[a]==V[j]and j!=a):
                        V[a],T=[Vx[i]-r,Vy[i]-r,Vx[i]+r,Vy[i]+r],out("o")
                        #if(d!=0 and d!=6):self.d1-=1
                    elif(self.Prison==2):                # Version Avec Prison
                        b=[Vx[self.v]-r,Vy[self.v]-r,Vx[self.v]+r,Vy[self.v]+r]
                        if(V[a]==R[j]):R[j],r2,self.v=b,j,self.v+1
                        if(V[a]==J[j]):J[j],j2,self.v=b,j,self.v+1
                        if(V[a]==B[j]):B[j],b2,self.v=b,j,self.v+1
                    elif(self.Prison==1):                # Version Sans Prision
                        if(V[a]==R[j]):R[j],r2=R1[j],j
                        elif(V[a]==J[j]):J[j],j2=J1[j],j
                        elif(V[a]==B[j]):B[j],b2=B1[j],j
        if(v1!=0):self.V, self.R, self.J, self.B=V, R, J, B
        elif(r1!=0):self.R, self.V, self.J, self.B=V, R, J, B
        elif(j1!=0):self.J, self.V, self.R, self.B=V, R, J, B
        elif(b1!=0):self.B, self.V, self.R, self.J=V, R, J, B
        v1=r1=j1=b1=0
        return v1,r1,j1,b1,T

    def Définir_Trajectoire(self):
        for i in range(1,6):    #-------------------------------------
            j=i-1
            self.Vx[i],self.Vy[i],self.Rx[i],self.Ry[i]=Co*2.56+j*Co,Co*6.56,Co*9.56,Co*1.56+j*Co
            self.Jx[i],self.Jy[i],self.Bx[i],self.By[i]=Co*7.56,Co*13.56-j*Co,Co*14.56-j*Co,Co*8.56
        for i in range(6,12):
            j=i-6
            self.Vx[i],self.Vy[i],self.Rx[i],self.Ry[i]=Co*7.56,Co*5.56-Co*j,Co*10.56+Co*j,Co*6.56
            self.Jx[i],self.Jy[i],self.Bx[i],self.By[i]=Co*6.56-Co*j,Co*8.56,Co*9.56,Co*9.56+Co*j
        for i in range(12,14):
            j=i-12
            self.Vx[i],self.Vy[i],self.Rx[i],self.Ry[i]=Co*8.56+Co*j,Co*0.56,Co*15.56,Co*7.56+Co*j
            self.Jx[i],self.Jy[i],self.Bx[i],self.By[i]=Co*1.56,Co*7.56-Co*j,Co*8.56-Co*j,Co*14.56
        for i in range(1,14):        # Trace la trajectoire que doit
            j=i+13
            self.Vx[j],self.Vy[j],self.Rx[j],self.Ry[j]=self.Rx[i],self.Ry[i],self.Bx[i],self.By[i]  # suivre chaque Pion
            self.Jx[j],self.Jy[j],self.Bx[j],self.By[j]=self.Vx[i],self.Vy[i],self.Jx[i],self.Jy[i]
        for i in range(1,27):
            j=i+26
            self.Vx[j],self.Vy[j],self.Rx[j],self.Ry[j]=self.Bx[i],self.By[i],self.Jx[i],self.Jy[i]
            self.Jx[j],self.Jy[j],self.Bx[j],self.By[j]=self.Rx[i],self.Ry[i],self.Vx[i],self.Vy[i]
        for i in range(6):
            j=i+51
            self.Vx[j],self.Vy[j],self.Rx[j],self.Ry[j]=Co*1.56+i*Co,Co*7.56,Co*8.56,Co*0.56+i*Co
            self.Jx[j],self.Jy[j],self.Bx[j],self.By[j]=Co*8.56,Co*14.56-i*Co,Co*15.56-i*Co,Co*7.56
        for i in range(6):
            if(i!=1 and i!=4):
                for j1 in range(0,6,2):
                    self.Vx[j],self.Vy[j],self.Rx[j],self.Ry[j]=Co*1.56+j1*Co,Co*0.56+i*Co,Co*10.56+Co*j1,Co*0.56+i*Co
                    self.Jx[j],self.Jy[j],self.Bx[j],self.By[j]=Co*1.56+j1*Co,Co*9.56+i*Co,Co*10.56+j1*Co,Co*9.56+Co*i
                    j+=1                                 #-------------------------------
        
    def Posi_Pion(self):
        for i in range(57):
            for j in range(1,5):
                if(self.V[j]!=0):
                    if(self.Vx[i]==self.V[j][0]+r and self.Vy[i]==self.V[j][1]+r): self.Posi_PioV[j]=i
                if(self.R[j]!=0):
                    if(self.Rx[i]==self.R[j][0]+r and self.Ry[i]==self.R[j][1]+r): self.Posi_PioR[j]=i
                if(self.J[j]!=0):
                    if(self.Jx[i]==self.J[j][0]+r and self.Jy[i]==self.J[j][1]+r): self.Posi_PioJ[j]=i
                if(self.B[j]!=0):
                    if(self.Bx[i]==self.B[j][0]+r and self.By[i]==self.B[j][1]+r): self.Posi_PioB[j]=i
        
    def pointeur(self,event):
        x,y,self.x1,self.y1,Pion,K,k1,k2,k3,I=event.x,event.y,event.x,event.y,[],0,0,0,[],0
        del self.Case_Dé[1:]
        Class.__init1__()
        Class.Posi_Pion()
        for i in self.Compteur:
            self.Case=self.Case or self.Case_Dé[i][2]
            if(i==1):Pion.append(self.Posi_PioV)
            if(i==2):Pion.append(self.Posi_PioR)
            if(i==3):Pion.append(self.Posi_PioB)
            if(i==4):Pion.append(self.Posi_PioJ)
        for i in Pion:
            if(i!=[0,0,0,0,0]):
                k3.append(max(i))  # k3 : Position du Pion le plus loin
                k1+=1  # k1 : Nombre de Personnes sorti
            for j in i:
                if(j!=0):k2+=1  # k2 : Nombre de Pions sorti
        if(k3!=[]):k3=max(k3)
        else:k3=0
        if(self.Case):
            if(k1==0 or(k1==1 and k2==1 and k3<15)and Pion[self.d2]==[0,0,0,0,0]):K=2
            elif((k2==1 and k3>=15)or k1>1 or k2>1 or(k1==1 and Pion[self.d2]!=[0,0,0,0,0])):K=1
            if(K!=0):
                Class.Lancez_le_Dé()
                for i in Pion[self.d2]:
                    if((i==0 and self.d>=6)or(i!=0 and i+self.d<=56)):
                        I=1
                        break
                self.Nb_Jeu+=1
                if(self.d%6==0 and self.d!=0 and self.Nb_Jeu==K):self.Nb_Jeu-=1
                elif(self.Nb_Jeu==K):
                    can.delete(self.Pio1)
                    can.delete(self.Pio2)
                    if(self.d2!=len(self.Compteur)-1):self.d2+=1
                    else:self.d2=0
                    self.Nb_Jeu, self.i=0, 0
                    if(I==0):self.Pio1, self.Pio2=can.create_rectangle(self.Case_Dé[self.Compteur[self.d2]][0],fill="white", width=Co*0.06), can.create_text(self.Case_Dé[self.Compteur[self.d2]][1],text="Joué")
                    if(I==1):self.Pio1=can.create_rectangle(self.Case_Dé[self.Compteur[self.d2]][0],fill="white", width=Co*0.06)
            else:print("Echec")
            print("1= ",self.Pio1, self.Pio2)
        elif(Co*1.06<=x and x<=Co*16.06 and Co*0.06<=y and y<=Co*15.06):
            Class.Avance_Pion(x,y)
            if(self.d==0):
                self.d1=self.d2
                self.Pio2=can.create_text(self.Case_Dé[self.Compteur[self.d2]][1],text="Joué")
                print("self.d1", self.d1)
                print("1= ",self.Pio1, self.Pio2)
            if(self.d1>len(self.Compteur)-1):self.d1=0
        self.Case=False
        
    def Avance_Pion(self,x,y):
        self.i,self.i1,self.j1,Pion=0,2,0,[self.V1,self.R1,self.J1,self.B1]
        if(self.d>=6):d=6
        else:d=self.d
        Vx,Rx,Jx,Bx,Vy,Ry,Jy,By,T = self.Vx,self.Rx,self.Jx,self.Bx,self.Vy,self.Ry,self.Jy,self.By,False
        
        """for i in range(0,Co*5,Co*3):      #---------------------------------------------------------------------------------------
            if((Co*2.56+i-r<=x and x<=Co*2.56+i+r)and(Co*1.56-r<=y and y<=Co*1.56+r)):Vx[0],Vy[0]=Co*2.56+i,Co*1.56
            elif((Co*2.56+i-r<=x and x<=Co*2.56+i+r)and(Co*4.6-r<=y and y<=Co*4.56+r)):Vx[0],Vy[0]=Co*2.56+i,Co*4.56

            elif((Co*11.56+i-r<=x and x<=Co*11.56+i+r)and(Co*1.56-r<=y and y<=Co*1.56+r)):Rx[0],Ry[0]=Co*11.56+i,Co*1.56
            elif((Co*11.56+i-r<=x and x<=Co*11.56+i+r)and(Co*4.56-r<=y and y<=Co*4.56+r)):Rx[0],Ry[0]=Co*11.56+i,Co*4.56 # Determine la position initiale

            elif((Co*2.56+i-r<=x and x<=Co*2.56+i+r)and(Co*10.56-r<=y and y<=Co*10.56+r)):Jx[0],Jy[0]=Co*2.56+i,Co*10.56 # de chaque Pion
            elif((Co*2.56+i-r<=x and x<=Co*2.56+i+r)and(Co*13.56-r<=y and y<=Co*13.56+r)):Jx[0],Jy[0]=Co*2.56+i,Co*13.5

            elif((Co*11.56+i-r<=x and x<=Co*11.56+i+r)and(Co*13.56-r<=y and y<=Co*13.56+r)):Bx[0],By[0]=Co*11.56+i,Co*13.5
            elif((Co*11.56+i-r<=x and x<=Co*11.56+i+r)and(Co*10.56-r<=y and y<=Co*10.56+r)):Bx[0],By[0]=Co*11.56+i,Co*10.56 #-------------------------------"""
        v1=r1=j1=b1=0
        for i in range(1,5):
            for j in self.Compteur:
                if(j==1):
                    self.Retour_en_arriere.append(self.V[i])
                    if((self.V[i][0]<=x and x<=self.V[i][2])and(self.V[i][1]<=y and y<=self.V[i][3])):v1=i
                    if((self.V1[i][0]<=x and x<=self.V1[i][2])and(self.V1[i][1]<=y and y<=self.V1[i][3])):Vx[0],Vy[0]=self.V1[i][0]+r,self.V1[i][1]+r
                elif(j==2):
                    self.Retour_en_arriere.append(self.R[i])
                    if((self.R[i][0]<=x and x<=self.R[i][2])and(self.R[i][1]<=y and y<=self.R[i][3])):r1=i
                    if((self.R1[i][0]<=x and x<=self.R1[i][2])and(self.R1[i][1]<=y and y<=self.R1[i][3])):Rx[0],Ry[0]=self.R1[i][0]+r,self.R1[i][1]+r
                elif(j==4):
                    self.Retour_en_arriere.append(self.J[i])
                    if((self.J[i][0]<=x and x<=self.J[i][2])and(self.J[i][1]<=y and y<=self.J[i][3])):j1=i
                    if((self.J1[i][0]<=x and x<=self.J1[i][2])and(self.J1[i][1]<=y and y<=self.J1[i][3])):Jx[0],Jy[0]=self.J1[i][0]+r,self.J1[i][1]+r
                elif(j==3):
                    self.Retour_en_arriere.append(self.B[i])
                    if((self.B[i][0]<=x and x<=self.B[i][2])and(self.B[i][1]<=y and y<=self.B[i][3])):b1=i
                    if((self.B1[i][0]<=x and x<=self.B1[i][2])and(self.B1[i][1]<=y and y<=self.B1[i][3])):Bx[0],By[0]=self.B1[i][0]+r,self.B1[i][1]+r
        self.Nombre_de_en_arriere+=len(self.Compteur)*4

        for i in range(57):
            if((Vx[i]-r<=x and x<=Vx[i]+r)and(Vy[i]-r<=y and y<=Vy[i]+r)and v1!=0): v1,r1,j1,b1,T = Class.Déplacement(Vx,Vy,d,i,T,v1,r1,b1,j1)
            elif(((Co*10.06<=x and x<=Co*16.06 and Co*0.06<=y and y<=Co*6.06)or(Co*1.06<=x and x<=Co*7.06 and Co*9.06<=y and y<=Co*15.06)or(Co*10.06<=x and x<=Co*16.06 and Co*9.06<=y and y<=Co*15.06))and v1!=0 and d==6): self.V[v1],T=self.V1[v1],True
            elif((Rx[i]-r<=x and x<=Rx[i]+r)and(Ry[i]-r<=y and y<=Ry[i]+r)and r1!=0 and self.Compteur[self.d1]==2): v1,r1,j1,b1,T = Class.Déplacement(Rx,Ry,d,i,T,v1,r1,b1,j1)
            elif(((Co*1.06<=x and x<=Co*7.06 and Co*0.06<=y and y<=Co*6.06)or(Co*1.06<=x and x<=Co*7.06 and Co*9.06<=y and y<=Co*15.06)or(Co*10.06<=x and x<=Co*16.06 and Co*9.06<=y and y<=Co*15.06))and r1!=0 and d==6 and self.Compteur[self.d1]==2): self.R[r1],T=self.R1[r1],True
            elif((Jx[i]-r<=x and x<=Jx[i]+r)and(Jy[i]-r<=y and y<=Jy[i]+r)and j1!=0): v1,r1,j1,b1,T = Class.Déplacement(Jx,Jy,d,i,T,v1,r1,b1,j1)
            elif(((Co*10.06<=x and x<=Co*16.06 and Co*0.06<=y and y<=Co*6.06)or(Co*1.06<=x and x<=Co*7.06 and Co*9.06<=y and y<=Co*15.06)or(Co*10.06<=x and x<=Co*16.06 and Co*9.06<=y and y<=Co*15.06))and j1!=0 and d==6): self.J[j1],T=self.J1[j1],True
            elif((Bx[i]-r<=x and x<=Bx[i]+r)and(By[i]-r<=y and y<=By[i]+r)and b1!=0): v1,r1,j1,b1,T = Class.Déplacement(Bx,By,d,i,T,v1,r1,b1,j1)
            elif(((Co*10.06<=x and x<=Co*16.06 and Co*0.06<=y and y<=Co*6.06)or(Co*1.06<=x and x<=Co*7.06 and Co*9.06<=y and y<=Co*15.06)or(Co*10.06<=x and x<=Co*16.06 and Co*9.06<=y and y<=Co*15.06))and b1!=0 and d==6): self.B[b1],T=self.B1[b1],True
            elif(i==56):
                out(self.Compteur[self.d1])
                self.d=0
            if(v1==0 and r1==0 and j1==0 and b1==0):break
        Class.Deplacement_des_Pions()
        Class.Posi_Pion()
        if(T==False):self.d=self.d
        elif(T==True and self.d>=6):self.d-=6
        elif(T==True and self.d<6):self.d=0
        #if(len(self.Compteur)==self.d1):self.d1=0

    def Choix_De_Case1(self,event):
        self.Compteur.append(1)
        enter1.create_oval(L/2-5,L/2-5,L/2+5,L/2+5,fill="green")

    def Choix_De_Case2(self,event):
        self.Compteur.append(2)
        enter2.create_oval(L/2-5,L/2-5,L/2+5,L/2+5,fill="red")

    def Choix_De_Case3(self,event):
        self.Compteur.append(3)
        enter3.create_oval(L/2-5,L/2-5,L/2+5,L/2+5,fill="blue")

    def Choix_De_Case4(self,event):
        self.Compteur.append(4)
        enter4.create_oval(L/2-5,L/2-5,L/2+5,L/2+5,fill="yellow")

Co = 45
r,L=Co*0.435,int(Co*0.42)  # Co : Longueur d'un coté, r : Rayon de chaque Pion
fen=Tk()
fen.title("Ludo Game")      # Donne le nom à la fenetre
fen.geometry("1180x739")    # Donne une dimension fixe de la fenètre contenant le Ludo
can=Canvas(fen,width=Co*17.06,height=Co*15.06,bg="white")
Class=Manip()
Class.Traçage_du_Tableau()
chaine1=Label(fen)
#Button(fen,text="Roll the Die",command=Class.Lancez_le_Dé).grid(row=1,column=1)
Button(fen,text="Recommencer",command=Class.Out).grid(row=3,column=1)
Button(fen,text="Marche-Arrière",command=Class.Marche_Arriere).grid(row=4,column=1)
chaine1.grid(row=1,column=1)
#Button(fen,text="Exit",command=fen.destroy,width=10,fg="red").grid(row=6,column=1)
can.bind("<Button-1>",Class.pointeur)
can.grid()
chaine=Label(fen)
chaine.grid()
Button(fen,text="Sans Emprisonnement",fg="maroon",command=Class.Sans_Prisonnement).grid(row=5,column=1)
Button(fen,text="Avec Emprisonnement",fg="maroon",command=Class.Avec_Prisonnement).grid(row=6,column=1)
can.grid(row=1,column=2,rowspan=6)

fram=Frame(fen,width=Co*1.02,height=Co*1.02,bg="dark grey")
text=Label(fram,text="Choisissez Vos Cases à Jouer").grid(row=1,columnspan=2)
text1=Label(fram,text="1-) Case  Verte",fg="green",bg="dark grey",width=L).grid(row=2,sticky=W,pady=5)
text2=Label(fram,text="2-) Case Rouge",fg="red",bg="dark grey",width=L).grid(row=3,sticky=W,pady=5)
text3=Label(fram,text="3-) Case  Bleue",fg="blue",bg="dark grey",width=L).grid(row=4,sticky=W,pady=5)
text4=Label(fram,text="4-) Case  Jaune",fg="yellow",bg="dark grey",width=L).grid(row=5,sticky=W,pady=5)
enter1=Canvas(fram,width=L,heigh=L,bg="white")
enter1.bind("<Button-1>",Class.Choix_De_Case1)
enter1.grid(row=2,column=2,columnspan=1)
enter2=Canvas(fram,width=L,heigh=L,bg="white")
enter2.bind("<Button-1>",Class.Choix_De_Case2)
enter2.grid(row=3,column=2)
enter3=Canvas(fram,width=L,heigh=L,bg="white")
enter3.bind("<Button-1>",Class.Choix_De_Case3)
enter3.grid(row=4,column=2)
enter4=Canvas(fram,width=L,heigh=L,bg="white")
enter4.bind("<Button-1>",Class.Choix_De_Case4)
enter4.grid(row=5,column=2)
Button(fram,text="OK",width=5,fg="maroon",command=Class.Traçage_des_Pions).grid(row=6,column=2)
fram.grid(row=2,column=1)

fen.mainloop()
