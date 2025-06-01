from flask import Flask, render_template, request, jsonify
from lexer import Lexer
from parser import Parser
from turing_machine import TuringMachine
from collections import defaultdict

app = Flask(__name__)

STUDENT_INFO = {
    "name": "Eduardo Almeida Pavon",
    "professor": "Ingeniero Kevin David Molina Gomez",
    "semester": "6 Semestre de 2025"
}

@app.route('/')
def index():
    return render_template('index.html', student_info=STUDENT_INFO)

@app.route('/api/lexer', methods=['POST'])
def lexer_analysis():
    code = request.json.get('code', '')

    lexer = Lexer(code)
    tokens_por_linea, errores_lexicos = lexer.analyze()

    tokens = []
    for line_num, line_tokens in tokens_por_linea.items():
        for token in line_tokens:
            tokens.append({
                'type': token['tipo'],
                'value': token['valor'],
                'linea': int(line_num)
            })

    if errores_lexicos:
        return jsonify({
            'error': 'Errores léxicos encontrados',
            'tokens': tokens,
            'errors': errores_lexicos
        }), 400

    return jsonify({'tokens': tokens})

@app.route('/api/parser', methods=['POST'])
def parser_analysis():
    try:
        tokens = request.json.get('tokens', [])

        tokens_por_linea = defaultdict(list)
        for token in tokens:
            linea = str(token.get('linea', 1))
            tokens_por_linea[linea].append({
                'tipo': token['type'],
                'valor': token['value']
            })

        parser = Parser(tokens_por_linea)
        arbol_sintactico, errores_sintacticos = parser.parse()

        if errores_sintacticos:
            return jsonify({
                'success': False,
                'message': errores_sintacticos
            })

        return jsonify({
            'success': True,
            'message': 'Análisis sintáctico exitoso'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': [{'linea': 0, 'mensaje': f'Error interno del servidor: {str(e)}'}]
        }), 500

@app.route('/api/simulate_mt', methods=['POST'])
def simulate_mt():
    try:
        tape = request.json.get('tape', '')

        transition_function = {
            ('q0', '0'): ('q0', '0', 'R'),
            ('q0', '1'): ('q0', '1', 'R'),
            ('q0', '_'): ('q_check', '_', 'L'),

            ('q_check', '0'): ('q_reject', '0', 'R'),
            ('q_check', '1'): ('q_accept', '1', 'R'),

            ('q_accept', '_'): ('q_accept', '_', 'R'),
            ('q_reject', '_'): ('q_reject', '_', 'R'),
        }
        final_states = {'q_accept'}

        tm = TuringMachine(
            tape=tape,
            final_states=final_states,
            transition_function=transition_function
        )

        accepted, final_tape = tm.run()

        return jsonify({
            'final_tape': final_tape,
            'message': 'Aceptado' if accepted else 'No aceptado'
        })

    except Exception as e:
        return jsonify({'error': f'Error interno: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
