import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
xs=[-m/4 for m in range(-168,-131)]
print(xs)
'''for x in range(len(xs)):
    xs[x]=round(10000/xs[x])'''
for x in range(len(xs)):
    xs[x]=10000/xs[x]
def formplot(aminoacid,name,clr):
    x=np.array(xs)
    y=np.array(aminoacid)
    x_new = np.linspace(x.min(), x.max(),500)
    f = interp1d(x, y, kind='quadratic')
    y_smooth=f(x_new)
    plt.plot (x_new,y_smooth,label=name,color=clr, ms = 2)
    plt.scatter (x, y,color=clr,s = 4 )
def transmit(aminoacid):
    for i in range(len(aminoacid)):
        aminoacid[i]=(1/(pow(10,aminoacid[i])))*100
        aminoacid[i]

    
yY=[0.34,0.25,0.19,0.16,0.16,0.1575,0.15,0.18,0.2,0.24,0.26,0.31,0.36,0.42,0.48,0.56,0.65,0.72,0.81,
    0.88, 0.94,1.0,1.02,0.95,0.9,0.84,0.68,0.47,0.27,0.12, 0.05,0.01,0, -0.01,-0.02,-0.02, -0.03]
yW=[0.28,0.28,0.3, 0.29, 0.29, 0.3, 0.32, 0.34, 0.37, 0.42, 0.45, 0.5, 0.54, 0.61,0.66,0.72,0.77,
    0.84,0.88, 0.92,0.94, 0.95, 0.96,0.97,0.97,0.93,0.83,0.73,0.71,0.65,0.41,0.25,0.12,0.06,0.02,0,-0.02]
yF=[0.34, 0.31,0.30,0.29,0.31,0.33,0.34,0.35,0.4,0.43,0.41,0.42,0.48,0.46,0.40,0.38,0.36,0.3,0.25,0.17,
    0.14,0.13,0.11,0.09,0.09,0.08,0.08,0.07,0.06,0.06,0.05,0.04,0.04,0.03,0.03,0.02,0.02]

yZ=[0.04,0.03,0.01,0,0,-0.01,-0.02,0,0,0,0,0,-0.01,-0.005,-0.005,-0.005,-0.01,-0.0075,-0.0075,-0.02,-0.02,
    -0.02,-0.02,-0.02,-0.02,-0.02,-0.0225,-0.0225,-0.025,-0.03,-0.03,-0.03,-0.03,-0.0285,-0.0275,-0.0275,-0.04]
print(len(xs),len(yF),len(yW),len(yY),len(yZ))
print(xs)

formplot(yY,'Тирозин','dodgerblue')
formplot(yW, 'Триптофан','darkorange')
formplot(yF,'Фенілаланін','darkviolet')
formplot(yZ,'Zero','black')

plt.legend(loc="upper left")
plt.title("Спектри поглинання триптофану, тирозину і фенілаланіну")
plt.xlabel("λ (nm)",size=10)
plt.ylabel("D",rotation='horizontal',size=15)
plt.grid(axis = 'both')
plt.show()


transmit(yY)
transmit(yW)
transmit(yF)


formplot(yY,'Тирозин','dodgerblue')
formplot(yW, 'Триптофан','darkorange')
formplot(yF,'Фенілаланін','darkviolet')

plt.legend(loc="upper left")
plt.title("Спектри пропускання триптофану, тирозину і фенілаланіну")
plt.xlabel("λ (nm)",size=10)
plt.ylabel("T ( %)",rotation='vertical',size=15)
plt.grid(axis = 'both')
plt.show()



