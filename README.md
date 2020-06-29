# Tarea3_Modelos_P
Esta tarea trata sobre las variables aleatorias múltiples.


Punto 1.
Primero se calculo el vector de probabilidades X y Y sumando las filas para el caso de X y las columnas en caso de Y. Ya que es la forma de calculas las funciones marginales de variable discreta segun lo explicado por el profesor.

Luego se crearon dos vectores X y Y con X de 5 a 15 y Y 5 a 25. Y se graficaron los vectores de variable contra sus probabilidades generando una distribucion gaussiana discreta.

Luego para calcular los parametros miu y sigma, se utilizaron formulas generales de distribuciones discretas estas formulas estan en este repositorio en forma de imagenes, la direccion de donde se tomo esta informacion es: https://www.superprof.es/apuntes/escolar/matematicas/probabilidades/distribucion-binomial/media-y-varianza-de-una-variable-aleatoria-discreta.html. Para esto fue necesario aplicar algunas operaciones a los datos como si fuera una matriz.


Punto 2.
Este punto es muy sensillo, como en el punto anterior se calculo un mui y un sigma para X y Y, practicamente ya se cuenta con las funciones de distribucion de estas dos variables. Revisando la presentacion 10 nos damos cuenta que la funcion de distribucion conjunta f(x,y) es la multiplicacion de las funciones marginales en caso de haber independencia entre estas, que es lo que se indica en el enunciado. Por lo tanto la funcion de distribucion conjunta es una exponencial que depende de x e y.


Punto 3.
Este punto se abordo siguiendo las recomendaciones que el profesor dio en la consulta, en donde explico las formulas de variable continua para estos parametros y su interpretación en variable discreta, por lo que se siguió al pie de la letra las instrucciones aplicando operaciones sobre las filas y las columnas del csv xyp.

La interpretación de los momento se imprime en el codigo, sin embargo tambien lo pondre aqui para mayor seguridad.

Sepuede decir que ambas variables no estan corelacionadas ya son independientes, en este caso la correlacion es de 149.542 muy cercano a E[X]*E[Y]=149.55 que es la expresion para cuando las variables no estan correlacionadas, sin embargo a como se explica en la presentación esto no es nesesariamente cierto para variables aleatorias gaussianas, aunque por dicha si se cumplio en este caso, ayudandonos a comprobar la coerencia de los datos
    
La covarianza tiene mucho sentido ya que X y Y son variables aleatorias independientes por lo que la covarianza de la funcion bidimencional es cero esto se expresa como Cxy=0. Si las variables son indenpentes la covarianza es cero, en nuestro caso Cxy= 0.0677.
    
El coeficiente de correlacion p es 0.06773/(5.3*2.8)), para el coeficiente de correlacion basta con aplicar la formula que se indica en la presentacion 10 diapositiva 19, en donde se tiene la formula 'p=Cxv/[(Desviacion.E X)*(Desviacion.E Y)], por lo tanto solo utilizamos estos paramatros calculado anteriormente. Nuevamente este parametro nos indica el grado de independencia entre las variables X, Y dando como resultado un valor muy bajo p=0.00456 confirmando la supocicion inicial, este parametro es independiente de la escala de medida de las variables.


Punto 4.
Las graficas 2D se generadon utilizando los comandos y librerias que se usaron para la tarea 1 y la grafica 3D se hizo siguiendo las intrucciones que se explican en el video: https://www.youtube.com/watch?v=N5k05yuEw-0&list=PLXz_3wH5zsTIoEgGJFqsj2Am2l7ojBjhe&index=16&t=241s.





