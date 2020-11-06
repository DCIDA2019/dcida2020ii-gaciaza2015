Licenciatura: 
 - El objetivo será reproducir la gráfica 9, y tabla 10 del artículo https://arxiv.org/pdf/1401.4064.pdf
 - La información mas importante del articulo para llevar a cabo este proyecto está en las secciones 4.1, 5 (algunos puntos) y 6.
 - Para lograrlo sigue los siguientes pasos: 
   - Haz una función que calcule la distancia modulo observada, eq. 4, dados unos valores de los parámetros alpha,beta,Mb y DeltaM
   - Define una función que calcule la distancia modulo teórica para un modelo cosmológico, usando la libreria: https://docs.astropy.org/en/stable/cosmology/
   - Usando las dos funciones anteriores reproduce la gráfica en la figura 8 (panel superior) 
   - Una vez las dos funciones de arriba esten funcinando correctamente. Utiliza emcee para hacer la inferencia de parámetros (son 5). Utiliza un likelihood Gaussiano, 
 . Nota que en este caso se tiene una matriz de covarianza, no solo una covarianza diagonal, por lo que el menos logaritmo del likelihood toma una forma como la ecuación 15.  
 
- Nota: Los problemas suelen surgir al incluir la matriz de covarianza, por lo que una primera aproximación sería usar una matriz covarianza diagonal, y verificar que todo 
funcion, y posteriormente trabajar en añadir la matriz de covarianza completa...
