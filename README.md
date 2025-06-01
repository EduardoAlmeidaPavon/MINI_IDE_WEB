# Analizador Léxico y Sintáctico

## Información del Estudiante
- **Nombre:** EDUARDO ALMEIDA PAVON
- **Materia:** LENGUAJES Y AUTOMATAS I
- **Profesor:** KEVIN DAVID MOLINA GOMEZ
- **Institución:** INSTITUTO TECNOLOGICO DE MINATITLAN

## Instrucciones para Ejecutar el Proyecto

1. **Requisitos:**
   - Python 3.x instalado

2. **Pasos para ejecutar:**
   ```bash
   # Ejecutar el analizador
   python main.py
   ```

## Lenguaje Personalizado

### Tokens
| Token | Descripción | Ejemplo |
|-------|-------------|---------|
| NUMERO | Números enteros o decimales | 42, 3.14 |
| IDENTIFICADOR | Nombres de variables | edad, nombre |
| OPERADOR | Operadores matemáticos | +, -, *, /, = |
| PARENTESIS | Paréntesis | (, ) |
| PUNTUACION | Puntuación | , ; : |
| CADENA | Texto entre comillas | "Hola" |

### Gramática Básica
- Declaración de variable: `identificador = valor;`
- Operación matemática: `resultado = valor operador valor;`

### Manejo de Errores
1. **Error Léxico:** Caracteres no permitidos
2. **Error Sintáctico:** Estructura incorrecta
3. **Error Semántico:** Variables no declaradas

## Ejemplos

### Entradas Válidas
```
edad = 25;
nombre = "Juan";
suma = 5 + 3;
```

![Image_Alt](https://github.com/EduardoAlmeidaPavon/MINI_IDE_WEB/blob/ab7ed3ae61e32a907fa5c3f672d5a7469d57578e/Ejemplo%20Valido%20Lexico.png)

![Image_Alt](https://github.com/EduardoAlmeidaPavon/MINI_IDE_WEB/blob/ab7ed3ae61e32a907fa5c3f672d5a7469d57578e/Ejemplo%20Valido%20Sintactico.png)


### Entradas Inválidas
```
# Error léxico
edad@ = 25;

# Error sintáctico
edad = ;

# Error semántico
resultado = x + 5;  // x no está declarada
```

![Image_Alt](https://github.com/EduardoAlmeidaPavon/MINI_IDE_WEB/blob/ab7ed3ae61e32a907fa5c3f672d5a7469d57578e/Ejemplo%20Invalido%20Lexico.png)

![Image_Alt](https://github.com/EduardoAlmeidaPavon/MINI_IDE_WEB/blob/ab7ed3ae61e32a907fa5c3f672d5a7469d57578e/Ejemplo%20Invalido%20Sintactico.png)


## Máquina de Turing
El proyecto incluye una implementación de Máquina de Turing para la validación de cadenas con los siguientes estados:
- Estado inicial: q0
- Estados finales: q_accept, q_reject
- Símbolos: 0, 1, _ (espacio en blanco)

- ![Image_Alt](https://github.com/EduardoAlmeidaPavon/MINI_IDE_WEB/blob/ab7ed3ae61e32a907fa5c3f672d5a7469d57578e/Turing%20Valido.png)

- ![Image_Alt](https://github.com/EduardoAlmeidaPavon/MINI_IDE_WEB/blob/ab7ed3ae61e32a907fa5c3f672d5a7469d57578e/Turing%20Invalido.png)

 
