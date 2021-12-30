import numpy as np
import matplotlib.pyplot as plt

#defining the magnetic field

Bx=0    #T
By=0    #T
Bz=1    #T


#defining the initial velocity

vxo=1   #m/s
vyo=1   #m/s
vzo=0   #m/s

vx=[vxo]
vy=[vyo]
vz=[vzo]

#defining the particle characteristics

q=1     #C
m=1     #kg
a=q/m
#defining the electric field

Ex=0.1   #N/C
omega=a*Bz 
E=[]
j=100000
ts=np.linspace(0,100,j)
i=0


def En(t):
    return Ex*np.cos(omega*t)

while i != j:
    E.append(round(En(ts[i]),4))
    i+=1


#---------------------------------------------------------------------
#------------Euler's method----velocity-------------------------------
#---------------------------------------------------------------------

i=0
j=100000
h=(1/j)*(10**2)  #step
a=q/m

while i != j:
    vx.append(a*(vy[i]*Bz-vz[i]*By+E[i])*h+vx[i])
    vy.append(a*(vz[i]*Bx-vx[i]*Bz)*h+vy[i])
    vz.append(a*(vx[i]*By-vy[i]*Bx)*h+vz[i])
    i+=1
vx.remove(vx[-1])
vy.remove(vy[-1])
vz.remove(vz[-1])

#-------------------------------------------------------------------
#-----------defining the space characteristics----------------------
#-------------------------------------------------------------------

xo=2
yo=2
zo=2

x=[xo]
y=[yo]
z=[zo]

#---------------------------------------------------------------------
#------------Euler's method----space----------------------------------
#---------------------------------------------------------------------
i=0

while i!= len(vx):
    x.append(vx[i]*h+x[i])
    y.append(vy[i]*h+y[i])
    z.append(vz[i]*h+z[i])
    i+=1

#------------------------------------------------------------------------
#-------------printing---------------------------------------------------
#------------------------------------------------------------------------

def vsqrd(l,m,n):
    return (l**2+m**2+n**2)

print("inintial KE=",(1/2)*m*vsqrd(vx[0],vy[0],vz[0]), " jouls")
print("final KE=",(1/2)*m*vsqrd(vx[-1],vy[-1],vz[-1]), " jouls")



#------------------------------------------------------------------------
#-------------plotting the results---------------------------------------
#------------------------------------------------------------------------

ax=plt.axes(projection='3d')


plt.plot(x,y,z)
plt.show()

