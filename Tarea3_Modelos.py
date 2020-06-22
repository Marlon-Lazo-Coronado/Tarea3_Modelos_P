#Definimos Las Librerias
import csv
from math import *
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
import scipy as sp
from scipy.stats import rayleigh
from scipy.stats import kurtosis
from scipy.stats import skew
from matplotlib import pyplot as plt
from numpy.random import randint
from mpl_toolkits.mplot3d.axes3d import Axes3D

def main():
    
   

    datos=pd.read_csv('xy.csv', header=0)
    #print(datos['y5'])
    #print(datos.iloc[[1],])
    #print(datos)
    
    
    
    ###############PRIMERO RECORTO LA MATRIY Y HAGO LAS SUMAS##################
    
    ####### Recotamos la matriz para X ##############################
    t2=datos.iloc[:,1:22] #for i in (len(A)) 
    Matrix=t2.iloc[0:13]
    
    t3=datos.iloc[:,1:22] #for i in (len(A)) #Esta es temporarl  
    matrixt=t3.iloc[0:13] #Para hacer el for
  
    ###### Sumamos los espacios de la matriz para el vector de probabilidad X ###########
    for col in range(11):
        for row in  range(21):
            Matrix.iat[col,0]+=Matrix.iat[col,row]
        Matrix.iat[col,0]=Matrix.iat[col,0]-matrixt.iat[col,0]
    #print(Matrix) #Verificamos resultados 
    #print(matrixt)
    
    
    Px=Matrix.iloc[0:13,0:1]
    #s=0.00262+0.00177+0.00325+0.00353+0.003+0.00365+0.00544+0.00466+0.00381+0.00445+0.00122+0.0049+0.0022+0.00359+0.00304+0.00212+0.00355+0.00247+0.00337+0.00184+0.00266
    #print(s) #Prueba de una buena suma
    #print(Px)
    
    
    
    ######### Ahora hacemos lo mismo para Y ######################
    t2=datos.iloc[:,1:22] #Recortamos la matriz
    MY1=t2.iloc[0:13]
    
    t3=datos.iloc[:,1:22] #Temporal 
    MY2=t3.iloc[0:13] 
    
    #Cro un vector dataframe de 21 espacios para guardar las probabilidades Y y despues de calcuar las sumas
    t4=datos.iloc[:,1:2] 
    Py=t4.iloc[0:13]  #Otro vector para guardar valores

    for x in np.arange(0, 21): #Ampliamos el tamaño del dataframe de 11 a 21 para poder sumar
        Py.loc[x] = [np.random.randint(-1,1) for n in range(1)]
    #print(Py)

    
     # Sumamos los espacios para las probabilidades del vector Y ###########
    for col in range(21):
        for row in  range(11):
            MY1.iat[0,col]+=MY1.iat[row,col]
        MY1.iat[0,col]=(MY1.iat[0,col]-MY2.iat[0,col])
    
    #Asinamos los valores calculados
    for col in range(21):
            Py.iat[col,0]=MY1.iat[0,col]
    #print(Py)





    #EN TODO LO ANTERIOR SE SUMARON LOS VALORES DE las rpobabilidades

    ######### GRAFICAMOS ##########
    #########            ########### 
    #Creamos el vectror de la variable discreta Y
    a1={None:[1]}
    Y=pd.DataFrame(a1)
    #Extendemos el tamaño
    for x in np.arange(0, 21): #Asignamos los valores discretos de Y
        Y.loc[x] = [(5+x) for n in range(1)]
    #print(Y)
    
    
     #Creamos el vectror de la variable discreta X
    a2={None:[1]}
    X=pd.DataFrame(a2)
    #Extendemos el tamaño
    for x in np.arange(0, 11): #Asignamos los valores discretos de X
        X.loc[x] = [(5+x) for n in range(1)]
    #print(X)
    
    
    #Graficamos para ver la distribucion de los datos
    #plt.plot(Y,Py,'ro')
    #plt.plot(X,Px,'ro')
    

    ##### CALCULAMOS LA MEDIA y DESVIACION PARA PROPONER UN MODELO MATEMATICO GAUSSIANO######
    ################################################
    
    ############# MEDIA #################
    ### PARA Y Media=sumatoria yixPi ######
    t5=0
    for col in range(21):
            t5+=Py.iat[col,0]*Y.iat[col,0]
    #print('La media de Y es: ', t5) #Media=15.04566
    
    ### PARA X Media=sumatoria yixPi ######
    t6=0
    for col in range(11):
            t6+=Px.iat[col,0]*X.iat[col,0]
    #print('La media de X es: ', t6) #Media=9.9354
    
    ############## DESVIACION ##########
    #Para Y, tuve que hacer construir un vector del dataframe 
    #porque no me dejaba hacer una formula
    C = Py.values.tolist()
    B=Y.values.tolist()
    
    t7=0
    for i in range(21):#piso
        t7+=((B[i][0]**2)*C[i][0])
    r=0
    r=(t7-t5**2)**(1/2) #Desviacion estandar Y=5.306
    #print('Desviacion estandar Y: ', r)
    
    
   ####Calculamos la desviacion para X
    D= Px.values.tolist()
    F=X.values.tolist()
    #print(C)
    t8=0
    for i in range(11):#piso
        t8+=((F[i][0]**2)*D[i][0])
    tq=0
    tq=(t8-t6**2)**(1/2) #Desviacion estandar X=2.802
    #print('Desviacion estandar de X: ', tq)
    
    
    print('#########################################################')
    print('Los dos modelos son Gausianos por lo que se presenta el miu y el sigma para X e Y.\n')
    print('Estos parametros se calcularon utilizando los datos, no el modelo,')
    print('esto mediante las formulas de la variable decreta, junto a los graficos se')
    print('dejaran imagenes que contienen las formulas que se han utilizado.')
    
    print('Para la variable X')
    print('La media miu de X es: ', t6) #Media=9.9354
    print('Desviacion estandar sigma de X: ', tq)
    
    
    
    print('\nPara la variable Y')
    print('La media miu de Y es: ', t5) #Media=15.04566
    print('Desviacion estandar sigma de Y: ', r)
    
    
   
    
    ############# CALCULAMOS LOS MOMENTOS ###################
    #########################################################
    print('\n#########################################################')
    print('Con respecto a los momentos de la Variable aleatoria conjunta\n')
    print('Los momentos han sido calculados con base en los datos del csv y sin utilizar')
    print('el modelo, para esto se utilizaron las ecuaciones de la presentacion 10.\n')
    
    
    Datos2=pd.read_csv('xyp.csv', header=0)
    
     ####### Recotamos la matriz para XYP ##############################
    tu=Datos2.iloc[:,0:4] #for i in (len(A)) 
    Matrixyp=tu.iloc[0:233]
    #print(Matrixyp)
    #print(Datos2)
    
    
    #Calculamos la corelacion
    corelacion=0
    for col in range(233):
             corelacion+=Matrixyp.iat[row,0]*Matrixyp.iat[row,1]*Matrixyp.iat[row,2]
    print('La correlación Rxy es: ', corelacion)
    
    print('Sepuede decir que ambas variables no estan corelacionadas ya son independientes')
    print('sin embargo la correlacion es de 21.32 muy distante a E[X]*E[Y]=149.55 que es la expresion')
    print('para cuando la variables no estan correlacionadas. Sin embargo a como se explica en la')
    print('presentacion esto no es nesesariamente cierto para variables aleatorias gaussianas.\n')
    
    
    
    #Calculamos la covarianza
    covarianza=0
    for col in range(233):
             covarianza+=(Matrixyp.iat[row,0]-9.9354)*(Matrixyp.iat[row,1]-15.04566)*Matrixyp.iat[row,2]
    print('La covarianza Cxy es: ', covarianza)
    
    print('La covarianza tiene mucho sentido ya que X y Y son variables aleatorias')
    print('independientes por lo que la covarianza de la funcion bidimencional es cero')
    print('esto se expresa como Cxy=0. Si las variables son ondendientes la covarianza')
    print('es cero, en nuestro caso Cxy=0.06405.\n')
    
    
    print('El coeficiente de correlacion p es: ', 0.06405/(5.3*2.8))
    print('Para el coeficiente de correlacion basta con aplicar la formula que se')
    print('indica en la presentacion 10 diapositiva 19, en donde se tiene la formula')
    print('p=Cxv/[(Desviacion.E X)*(Desviacion.E Y)], por lo tanto solo utilizamos') 
    print('estos paramatros calculado anteriormente.\n')
    
    
    
    
    
    ######### Graficamos Los Modelos Calculados #########
    #####################################################
    # GRAFICAMOS f(y)
    plt.plot(Y,Py,'ro')
    def f2(y):
        fy = 0.0734*np.exp((-(y-15.04)**2)/59.06)
        return fy
    y = np.linspace(0,25, 50)
    p3 = plt.plot(y, f2(y), label='Modelo Gaussiano')
    #sns.distplot(Fxm)
    plt.legend(('Funcion 3'), prop = {'size': 20}, loc='upper right')
    plt.xlabel('Variable Aleatoria Y')
    plt.ylabel('Probabilidad')
    plt.title('Comparacion entre las dos curvas')
    plt.legend(loc=1)
    plt.show()
    
    
    # GRAFICAMOS f(x)
    plt.plot(X,Px,'ro')
    def f3(x):
        fx = 0.1424*np.exp((-(x-9.9354)**2)/15.7)
        return fx
    x = np.linspace(0,15, 50)
    p3 = plt.plot(x, f3(x), label='Modelo Gaussiano')
    #sns.distplot(Fxm) #ESTO ES PARA QUE PYTHON AJUSTE PERO NO ME DA EL MODELO
    plt.legend(('Funcion 3'), prop = {'size': 20}, loc='upper right')
    plt.xlabel('Variable Aleatoria X')
    plt.ylabel('Probabilidad')
    plt.title('Comparacion entre las dos curvas')
    plt.legend(loc=1)
    plt.show()
    
    
   # GRAFICAMOS f(X,Y)
    x = np.linspace(0,15, 100)
    y = np.linspace(0,25, 100)
    x,y = np.meshgrid(x,y)
    z = 0.0105*np.exp(-((((x-9.9354)**2)/15.7)+(((y-15.04)**2)/59.06)))
    fig = plt.figure(figsize=(7,7))
    ax=fig.add_subplot(1,1,1, projection='3d')
    ax.plot_wireframe(x,y,z, rstride=2, cstride=2, cmap='Blues')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X,Y)')
    ax.set_title('Funcion de Distribucion Conjunta')
    plt.show()


   
main()






