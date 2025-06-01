class Parser:
    def __init__(self, tokens_por_linea):
        self.tokens_por_linea = tokens_por_linea
        self.errores = []
        self.arbol = []
        self.current_line = 1
        self.current_token_index = 0

    def parse(self):
        for linea, tokens in self.tokens_por_linea.items():
            self.current_line = int(linea)
            self.current_token_index = 0

            while self.current_token_index < len(tokens):
                try:
                    nodo = self.parse_statement(tokens)
                    if nodo:
                        nodo['linea'] = self.current_line
                        self.arbol.append(nodo)
                except SyntaxError as e:
                    self.errores.append({
                        'linea': self.current_line,
                        'mensaje': str(e)
                    })
                    self.current_token_index += 1  # Para evitar bucle infinito

        return self.arbol, self.errores

    def parse_statement(self, tokens):
        if self.current_token_index >= len(tokens):
            return None

        token = tokens[self.current_token_index]

        if token['tipo'] == 'IDENTIFICADOR':
            nodo = self.parse_variable_declaration(tokens)

            # Validar punto y coma al final
            if self.current_token_index < len(tokens):
                final_token = tokens[self.current_token_index]
                if final_token['tipo'] == 'PUNTUACION' and final_token['valor'] == ';':
                    self.current_token_index += 1  # Consumir ;
                else:
                    raise SyntaxError("Se esperaba ';' al final de la línea")
            else:
                raise SyntaxError("Se esperaba ';' al final de la línea")

            return nodo

        raise SyntaxError("Se esperaba una declaración con identificador al inicio")

    def parse_variable_declaration(self, tokens):
        identificador = tokens[self.current_token_index]
        self.current_token_index += 1

        if self.current_token_index < len(tokens) and tokens[self.current_token_index]['valor'] == '=':
            self.current_token_index += 1
            valor = self.parse_expression(tokens)
            return {
                'tipo': 'declaracion_variable',
                'identificador': identificador['valor'],
                'valor': valor
            }

        raise SyntaxError(f"Se esperaba '=' después del identificador {identificador['valor']}")

    def parse_expression(self, tokens):
        if self.current_token_index >= len(tokens):
            return None

        # Primer operando
        left_token = tokens[self.current_token_index]
        if left_token['tipo'] not in ['NUMERO', 'CADENA', 'IDENTIFICADOR']:
            raise SyntaxError(f"Token inesperado: {left_token['valor']}")

        if left_token['tipo'] in ['NUMERO', 'CADENA']:
            left_node = {'tipo': 'literal', 'valor': left_token['valor'], 'tipo_dato': left_token['tipo']}
        else:
            left_node = {'tipo': 'identificador', 'valor': left_token['valor']}

        self.current_token_index += 1

        # Si no hay más tokens o el siguiente no es operador, devuelve operando simple
        if self.current_token_index >= len(tokens):
            return left_node

        op_token = tokens[self.current_token_index]

        if op_token['tipo'] != 'OPERADOR':
            return left_node

        operador = op_token['valor']
        self.current_token_index += 1

        # Segundo operando
        if self.current_token_index >= len(tokens):
            raise SyntaxError("Se esperaba un operando después del operador")

        right_token = tokens[self.current_token_index]

        if right_token['tipo'] not in ['NUMERO', 'CADENA', 'IDENTIFICADOR']:
            raise SyntaxError(f"Token inesperado: {right_token['valor']}")

        if right_token['tipo'] in ['NUMERO', 'CADENA']:
            right_node = {'tipo': 'literal', 'valor': right_token['valor'], 'tipo_dato': right_token['tipo']}
        else:
            right_node = {'tipo': 'identificador', 'valor': right_token['valor']}

        self.current_token_index += 1

        return {
            'tipo': 'operacion',
            'operador': operador,
            'izquierda': left_node,
            'derecha': right_node
        }
