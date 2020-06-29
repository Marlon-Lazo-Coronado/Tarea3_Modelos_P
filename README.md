# Tarea3_Modelos_P
Esta tarea trata sobre las variables aleatorias múltiples.

Punto 1.

Primero se calculo el vector de probabilidades X y Y sumando las filas para el caso de X y las columnas en caso de Y. Ya que es la forma de calculas las funciones marginales de variable discreta segun lo explicado por el profesor.

Luego se crearon dos vectores X y Y con X de 5 a 15 y Y 5 a 25. Y se graficaron los vectores de variable contra sus probabilidades generando una distribucion gaussiana discreta.

Luego para calcular los parametros miu y sigma, se utilizaron formulas generales de distribuciones discretas estas formulas estan en este repositorio en forma de imagenes, la direccion de donde se tomo esta informacion es: https://www.superprof.es/apuntes/escolar/matematicas/probabilidades/distribucion-binomial/media-y-varianza-de-una-variable-aleatoria-discreta.html. Para esto fue necesario aplicar algunas operaciones a los datos como si fuera una matriz.



Punto 2.

Este punto es muy sensillo, como en el punto anterior se calculo un mui y un sigma para X y Y, practicamente ya se cuenta con las funciones de distribucion de estas dos variables. Revisando la presentacion 10 nos damos cuenta que la funcion de distribucion conjunta f(x,y) es la multiplicacion de las funciones marginales en caso de haber independencia entre estas, que es lo que se indica en el enunciado. Por lo tanto la funcion de distribucion conjunta es una exponencial que depende de x e y.




Punto 3.
Este punto se abordo siguiendo las recomendaciones que el profesor dio en la consulta, en donde explico las formulas de variable continual para estos parametros y su interpretacion en variable discreta, por lo que se siguio al pie de la letra las instrucciones aplicando operaciones sobre las filas y las columnas del csv xyp.

