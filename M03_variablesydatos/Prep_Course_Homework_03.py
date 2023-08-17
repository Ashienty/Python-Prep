#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
numero1=7
print(numero1)




# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
cte=8.5
print(cte)





# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:


print (type(numero1))


# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre=("Pablo")




# 5) Crear una variable que contenga un número complejo

# In[3]:
complejo=complex(7j)





# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(complejo))






# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
verdad='True'
laVerdad=True
print(type(verdar))
#cadena
print(type(laVerdad))
#boolean





# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

#por poner 'True' la salida es igual en ambas pero uno el boolea y el otro un string que dice true 
print('verdad', verdad,' laVerdad:',laVerdad)





# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
sumaReal=3+3.5






# 11) Realizar una operación de suma de números complejos

# In[2]:
sumaCompleja=3j+4j
print(sumaCompleja)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
sumaRealCompleja=3+3j
print(sumaRealCompleja)




# 13) Realizar una operación de multiplicación

# In[5]:
5*5




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2**8)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
cociente=27/4
print(cociente)





# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
b=27//4
print(27//4)




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
a=27%4
print(27%4)





# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
#para usar lo de arriva les voy a asignar una cte a los valores asi realmete uso los de arriva
resultadoRebuscado=b*4+a
print(resultadoRebuscado)





# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
hola='hola'
mundo='mundo'

print(hola+mundo)





# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
#da falso por que uno es un int y el otro es un str
2=='2'





# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
dosint=2
dosstr='2'
dosstr=int(dosstr)
dosint==dosstr
print(type(dosstr),type(dosint))





# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
#por que esta expresado como un str pero asignado como un float

# In[12]:
a = float('3.8')
print (a)





# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
variable=3
variable-=1
print(variable)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

#se hace 4 por que el valor 0001 que es 1 pasa a ser 0100 creo, que es 4 

1 << 2

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
#si ambos fueran int daria 4 si ambos fueran str daria 2 2 pero la combinacion es un problema 

# In[23]:


2 + '2'



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
risa= 'ja'*3
print(risa)



