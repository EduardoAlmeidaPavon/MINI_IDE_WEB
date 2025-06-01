import re

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.errors = []
        
        # Definición de patrones para tokens
        self.token_patterns = [
            ('NUMERO', r'\d+(\.\d+)?'),
            ('IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('OPERADOR', r'[\+\-\*/=<>!]=?|&&|\|\|'),
            ('PARENTESIS', r'[\(\)]'),
            ('LLAVE', r'[\{\}]'),
            ('CORCHETE', r'[\[\]]'),
            ('PUNTUACION', r'[,;:]'),
            ('CADENA', r'"[^"]*"'),
            ('ESPACIO', r'\s+'),
            ('COMENTARIO', r'//.*|/\*[\s\S]*?\*/'),
        ]
        
        # Compilar patrones
        self.patterns = [(name, re.compile(pattern)) for name, pattern in self.token_patterns]
    
    def analyze(self):
        lines = self.text.split('\n')
        tokens_por_linea = {}
        errores_lexicos = []
        
        for line_num, line in enumerate(lines, 1):
            position = 0
            tokens_linea = []
            
            while position < len(line):
                match = None
                token_type = None
                
                # Buscar el siguiente token
                for name, pattern in self.patterns:
                    match = pattern.match(line, position)
                    if match:
                        token_type = name
                        break
                
                if match:
                    value = match.group(0)
                    if token_type not in ['ESPACIO', 'COMENTARIO']:
                        tokens_linea.append({
                            'tipo': token_type,
                            'valor': value,
                            'posicion': position
                        })
                    position = match.end()
                else:
                    # Carácter no reconocido - error léxico
                    errores_lexicos.append({
                        'linea': line_num,
                        'valor': line[position],
                        'posicion': position
                    })
                    position += 1
            
            if tokens_linea:
                tokens_por_linea[str(line_num)] = tokens_linea
        
        return tokens_por_linea, errores_lexicos 