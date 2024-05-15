# Programación de Computadores - UNAL
# Strings

## Carácteres
<table cellspacing="1" bgcolor="">
	<tr bgcolor="#252582">
		<th><b>Definición</b></th>
	</tr>
	<tr bgcolor="#e4e4ed">
		<td style="color:#141414">Un carácter es el elemento mínimo de información usado para representar, controlar, transmitir y visualizar datos. Al conjunto de carácteres usados con este fin se le llama: <b>esquema de codificación</b>. Los esquemas de codificación en general usan un número de bits o bytes fijos.
	</tr>
</table>

### Esquema ASCII
Código Estadounidense Estándar para el Intercambio de Información
*(American Standard Code for Information Interchange)*.

+ En su versión original usa 7 bits, definiendo 128 carácteres.
+ En la versión extendida usa 8 bits (esto es 1 byte), definiendo 256
carácteres.
+ Es la base de los archivos de texto plano (o sin formato).
+ Es el esquema base para la escritura de programas en casi todos los
lenguajes de programación (incluido Python).

<div align='center'>
<figure> <img src="https://i.postimg.cc/qMY92n61/image.png" alt="" width="600" height="auto"/></br>
<figcaption><b>Código ASCII</b></figcaption></figure>
</div>

### Unicode
Esquema de codificación cuyo objetivo es dar a cada carácter usado por cada uno de los lenguajes humanos su propio código, es decir, permitir la "internacionalización" de la computación.

+ **UTF-8:** Definido por ocho (8) bits (un byte). Toma como base el
ASCII, ANSI de Windows y el ISO 􀀀 8859 􀀀 1. Muy usado
en HTML.
+ **UTF-16:** Definido por 16 bits (2 bytes). Usa una representación de longitud variable que permite su optimización en procesos de
codificación a texto (usando un subconjunto de ASCII o
UTF 􀀀 8).
+ **UTF-32:** Definido por 32 bits (4 bytes). Es el mas simple pues usa una representación de longitud fija.

<div align='center'>
<figure> <img src="https://i.postimg.cc/d37DSrs5/image.png" alt="" width="600" height="auto"/></br>
<figcaption><b>Unicode</b></figcaption></figure>
</div>

### Chars
Dado que Python usa ASCII para la escritura de sus programas, se cuenta
con un esquema de representación para indicar que se usaran los mismos. El carácter a usar se delimita por el carácter ' o por el carácter " (llamado escape) de carácteres tanto de control o Unicode.
 + 'A': Se refiere al carácter A
 + "3": Se refiere al carácter 3
 + '"': Se refiere al carácter "
 + "'": Se refiere al carácter '

### Cadenas de carácteres
Una cadena de carácteres str es una secuencia de cero o mas carácteres.
Una cadena de carácteres se delimita por el carácter ' o por el carácter ".
Una cadena de carácteres es una estructura de datos **inmutable**, esto
significa que no puede ser cambiada.

+ 'ejemplo de cadena'
+ "Cadena con un tabulado \t y una nueva \n línea"
+ 'Cadena con un carácter unicode \u01F4 y una comilla doble"'
+ "Cadena con una comilla simple \', una comilla doble \" y una diagonal invertida \\"
+ La cadena vacía "" o ''


**Ejemplo 1:** 
```python
str1 = "ejemplo de cadena"
print(str1) 
```

**Ejemplo 2:** 
```python
cadena = "Cadena con un tabulado \t, y una nueva \n linea"
print(cadena)
```

## Operadores
### Concatenar
Concatena (pega) dos cadenas. Se utiliza el símbolo *+*.

**Ejemplo 3:** 
```python
nombre = "Minch Yoda"
trabajo = "Stars War"
print(nombre + " el maestro")
print(nombre + trabajo)
print(trabajo + " " + nombre)
```

### Comparar
Se usan los operadores convencionales (<, <=, >, >=, ==, !=) para comparar cadenas usando el orden lexicográfico. En el orden lexicográfico, se comparan de izquierda a derecha uno a uno los carácteres, mientras sean iguales. En el caso que no sean iguales, si el carácter de la primera cadena es menor que el de la segunda a la primer cadena se le considera menor, pero si es mayor, a la primer cadena se le considera mayor. Si todos los carácteres son iguales, las cadenas son iguales.

**Ejemplo 4:** 
```python
print("Rojas" < "Rosas")
print("Rojas" == "rosas")
```

### Subindice
Accede los elementos de una cadena, el primer índice de la cadena es cero (0). Se usa el operador *[index]*.

**Ejemplo 4:** 
```python
nombre = "Minch Yoda"
print(nombre[0]) # imprime M
print(nombre[6]) # imprime Y
print(nombre[4]) # imprime h
```

### Pertenencia
Es posible determinar si una subcadena se encuentra en una cadena de carácteres. Se utiliza el operador *in*.

**Ejemplo 5:** 
```python
text = "cien años de soledad"
if "años" in text:
  print("yes")
else:
  print("no")
```

Al igual que una lista, una cadena se puede convertir en un iterable utilizando el bucle *for* y el operador *in*.

**Ejemplo 6:** 
```python
s = "hola amigos mios"
for letra in s: # se puede iterar cada letra de la cadena
print(letra, end = ", ")
```

## Métodos

### len()
La función len determina la longitud de una cadena.

**Ejemplo 7:** 
```python
nombre = "Minch Yoda"
trabajo = "Stars War"
planeta = "Tatoon \t cinco"
vacia = ""
print(len(nombre)) # 10
print(len(trabajo)) # 9
print(len(planeta)) # 14
print(len(vacia)) # 0
```

### slicing
La función slice obtiene una porción (subcadena) de una cadena. La notación es similar a la función range, [inicio:fin:incremento]. 

**Ejemplo 8:** 
```python
nombre = "Minch Yoda"
print(nombre[:5]) # Minch
print(nombre[0:7]) # Minch Y
print(nombre[6:10]) # Yoda
print(nombre[::-1]) # adoY hcniM
```

### count
El método count obtiene las veces que una subcadena se encuentra en una cadena (o en una parte de ella). La notación es count(subcadena, inicio, fin).

**Ejemplo 9:** 
```python
str1 = "The avengers"
print(str1.count("e")) # 3
print(str1.count("e", 0, 3)) # 1
print(str1.count("e", 4, len(str1))) # 2
cad = "abcabcabcabcabc" 
print(cad.count("abc")) # 5
```

### Busqueda (find - rfind)
Los métodos find y rfind obtienen la primera y última ocurrencia de una subcadena en una cadena (o en una parte de ella), respectivamente. La notación es find/rfind(subcadena, inicio, fin).

**Ejemplo 9:** 
```python
str2 = "It is not despair, for despair is " \
"only for those who see the end " \
"beyond all doubt. We do not."
print("first:", str2.find("despair")) # 10
print("last:", str2.rfind("despair")) # 23
```

### Casing
Mayúsculas, min;usculas, capitalización, swap.

**Ejemplo 10:** 
```python
s = "cien años de soledad en Macondo"
print(s.lower()) # Muestra la cadena en minusculas
print(s.upper()) # Muestra la cadena en mayusculas
print(s.capitalize()) # Primer letra a mayuscula
print(s.title()) # Primer letra cada palabra a mayuscula
print(s.swapcase()) # Mayusculas <-> minusculas
```

### Removiendo carácteres
El metodo strip/lstrip/rstrip remueve los carácteres deseados a los dos lados/izquierda/derecha de una cadena. La notación es strip/lstrip/rstrip(carácteres). Si no se dan carácteres como argumento, elimina espacios en blanco (espacios y tabulaciones).

**Ejemplo 11:** 
```python
s = "---++---cien a~nos de soledad en Macondo---++---"
print(s.strip("-+"))
print(s.lstrip("-+"))
print(s.rstrip("-+"))
```

### split()
El método split divide una cadena de acuerdo a una subcadena que sirve como delimitador, dejando las partes separadas en una lista. La notación es split(delimitador).

**Ejemplo 11:** 
```python
sdate = "01-06-2021"
sp = sdate.split("-")
print(sp)
print("dia:", sp[0], "- mes:", sp[1], "- año:", sp[2])
```

### Justificación
Existen cuatro métodos para justificar cadenas:
+ ljust() : Justificar una cadena a la izquierda
+ rjust() : Justificar una cadena a la derecha
+ center() : Centrar una cadena
+ zfill() : Llenar una cadena con ceros

**Ejemplo 12:** 
```python
str1 = "Bogota"
print(str1.ljust(15, "#"))
print(str1.rjust(15, "#"))
print(str1.center(15, "#"))
account = "123456789"
print(account.zfill(15))
```

### replace
El método replace reemplazar una subcadena en una cadena por otra. La notación es replace(anterior, nueva).

**Ejemplo 12:** 
```python
str1 = "cien años de soledad"
print(str1)
rep = str1.replace("cien", "setenta")
print(rep)
rep = rep.replace("años", "días")
print(rep)
rep = rep.replace("soledad", "clases sincronicas!")
print(rep)
```

### .join
 En general, permite convertir el contenido de una lista/tupla/string en un string separada por un carácter en particular.

**Ejemplo 13:** 
```python
l1 = ["1", "2", "3", "4"]
s1 = ", ".join(l1)
print(s1)
```

**Ejemplo 14:** 
```python
s2 = "Hola"
print(" ".join(s2))
```

## print
Tiene la forma:

*print(*objects, sep=' ', end='\n', file=None, flush=False)*

Imprime objects al flujo de texto file, separándolos por sep y seguidos por end. 

Todos los argumentos que no son por palabra clave se convierten a cadenas tal y como str() hace y se escriben al flujo, separados por sep y seguidos por end. Tanto sep como end deben ser cadenas; también pueden ser None, lo cual significa que se empleen los valores por defecto. Si no se indica objects, print() escribirá end.

## format
A la hora de imprimir cadenas de carácteres se pueden *'formatear'* para lograr cierto estilo o reemplazar ciertos valores. Existen diversas formas de hacerlo:

### Old style
El estilo clásico utiliza el operador *%*. Se asemeja bastante a usar *printf* de C. *%* Define un placeholder en el cual se podrá reemplazar un valor con ciertas carácteristicas (tipo de datos, representación, entre otras).

```python
name = "Felipe"
print("Hola, %s" % name)
```

En caso que sean múltiples argumentos se pueden referir con una tupla.

```python
name = "Felipe"
dia = 15
print("Hola, %s, hoy es el dia %i" % (name, dia))
```

Tipos de datos a representar en el placeholder.

<div align='center'>
<table>
<tr>
<td><code>b</code></td>
<td>Binary integer</td>
</tr>
<tr>
<td><code>c</code></td>
<td>Single character</td>
</tr>
<tr>
<td><code>d</code></td>
<td>Decimal integer</td>
</tr>
<tr>
<td><code>e</code> or <code>E</code></td>
<td>Exponential</td>
</tr>
<tr>
<td><code>f</code> or <code>F</code></td>
<td>Floating point</td>
</tr>
<tr>
<td><code>g</code> or <code>G</code></td>
<td>Floating point or Exponential</td>
</tr>
<tr>
<td><code>o</code></td>
<td>Octal integer</td>
</tr>
<tr>
<td><code>s</code></td>
<td>String</td>
</tr>
<tr>
<td><code>x</code> or <code>X</code></td>
<td>Hexadecimal integer</td>
</tr>
<tr>
<td><code>%</code></td>
<td>Percentage</td>
</tr>
</table>
</div>

### Felipe's style (maybe the worse)
As expected, I wanna do thing in my own way. To format stuff in a string I just concatenate all stuff using *+* and convert everyting to a string with *str()*.

```python
name = "Felipe"
dia = 15
print("Hola, "+ name + ", hoy es el dia " + str(dia))
```

### The new style
Python 3 trajó consigo una nueva forma de formatear utilizando la función *.format()*. En términos generales se asemeja al uso del placeholder *%*, el cual es sustituido por *{}*, luego dentro de los argumentos de la función format se reemplazan los valores y el estilo.

```python
name = "Felipe"
print("Hola, {}".format(name))
```

```python
name = "Felipe"
dia = 15
print("Hola, {}, hoy es el dia {}".format(name, dia))
```

```python
name = "Felipe"
dia = 15
print("Hola, {nombre}, hoy es el dia {dia}".format(nombre=name, dia=dia))
```

```python
name = "Felipe"
dia = 15
print("Hola, {nombre:s}, hoy es el dia {dia:d}".format(nombre=name, dia=dia))
```

### f-Strings
Disponibles para Python 3.6+ esta nueva nueva forma permite embeber expresiones de python dentro de cadenas de carácteres.

```python
name = "Felipe"
print(f'Hola, {name}')
```

```python
name = "Felipe"
dia = 15
print(f"Hola, {name}, hoy es el dia {dia}")
```

## Reto 12
1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

2. Procesar el <a href="https://www.py4e.com/code3/mbox.txt">archivo</a> y extraer:
 - Cantidad de vocales
 - Cantidad de consonantes
 - Listado de las 50 palabras que más se repiten
