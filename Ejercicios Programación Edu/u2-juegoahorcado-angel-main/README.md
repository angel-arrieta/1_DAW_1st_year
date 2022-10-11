[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8867058&assignment_repo_type=AssignmentRepo)
# 1DAW2223-Ahorcado. Creación del juego del ahorcado
## Descripción
El juego del "ahorcado" es un juego de lápiz y papel, en el que el objetivo es adivinar una palabra. 

Un jugador piensa una palabra secreta, y el resto de jugadores deberán ir diciendo letras que les parece que pueden estar contenidas en la palabra secreta. Si aciertan, se escriben todas las letras coincidentes.  Si la letra no está, se resta un intento, agregando una parte al cuerpo (cabeza, brazo, etc.) hasta que queda dibujado todo el cuerpo del "ahorcado". 

Gana el juego si se completa la palabra antes de completar el cuerpo, y se pierde si se completa el número de intentos antes de completar la palabra. 

En nuestra versión del ahorcado, no dibujaremos el cuerpo, por lo menos no es obligatorio, sino que esta parte se simulará estableciendo un número de intentos, por ejemplo 5.

### ¿Qué vamos a necesitar?
- Leer la palabra la palabra secreta. Para que quien tiene que adivinar no la vea, podrás darle varias veces al intro. Ya veremos que existen otra formas de ocultar lo que escribes.
  + La palabra solo contendrá letras.
  + La palabra será mayor o igual a 5 caracteres.
  + Para evitar tener problemas con las mayusculas o minusculas (Case sensitive), podrás pasarla a mayuscula.
- Leer las letras 
  + Solo se puede escribir letras, y solo una.
  + Para evitar tener problemas con las mayusculas o minusculas (Case sensitive), podrás pasarla a mayuscula.
  + Mostrar el mensaje mientras no se cumpla la condición, sin tener en cuenta los intentos.
- Puedes usar una lista para guardar las letras usadas. 
  + Mira el operador in y la funcion add.
  + Si una letra introducida no esta en la palabra, o está en la lista de letras usadas se restará un intento.
  + Si la letra está contenida en la palabra que se pretende adivinar y no está en la lista de letras usadas antes, se rellena los huecos de la palabra con la letra y se introduce la letra en la lista de letras usadas. 
- Necesitaremos trabajar con la clase String. Consulta el manual de referenia y mira las funicioens que tiene y te puedan servir para resolver el problema. Algunas: 
  + ```replaceRange```
  + ```indexOf```
  + ```contains```

### ¿Qué vamos a hacer?
- Dividirnos en grupos
- Pensar cómo habría que hacerlo: Diseñar el algoritmo
- Cuida la salida a consola, para que sea limpia.
- Usa el depurador si lo necesitas.
- Documenta el código
- Necesitarás hacer **uso de bucles** (While, for, do while, repeat) para 
  + Recuerda, diseña el algoritmo antes de ponerte a programar.
  + Solicitar la palabra/letra mientras no se cumplan las condiciones
  + Realizar el proceso del juego: solicita letra, si esta en la palabra sustituyela, sino resta intentos.
  + Reemplazar la letra en la palabra tantas veces como sea necesario.

