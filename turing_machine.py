class TuringMachine:
    def __init__(self, tape, blank_symbol='_', initial_state='q0', final_states=None, transition_function=None):
        self.tape = list(tape)
        self.blank_symbol = blank_symbol
        self.head = 0
        self.state = initial_state
        self.final_states = final_states if final_states else set()
        self.transition_function = transition_function if transition_function else {}

    def step(self):
        if self.head < 0:
            self.tape.insert(0, self.blank_symbol)
            self.head = 0
        elif self.head >= len(self.tape):
            self.tape.append(self.blank_symbol)

        current_symbol = self.tape[self.head]
        action = self.transition_function.get((self.state, current_symbol))

        if action is None:
            return False

        new_state, new_symbol, direction = action

        self.tape[self.head] = new_symbol
        self.state = new_state
        if direction == 'R':
            self.head += 1
        elif direction == 'L':
            self.head -= 1
        else:
            raise ValueError("Dirección inválida, debe ser 'L' o 'R'")

        return True

    def run(self, max_steps=1000):
        steps = 0
        rejected_states = {'q_reject'}
        while self.state not in self.final_states and self.state not in rejected_states and steps < max_steps:
            if not self.step():
                break
            steps += 1
        accepted = self.state in self.final_states
        return accepted, ''.join(self.tape).rstrip(self.blank_symbol)


# Definición máquina para aceptar cadenas que terminan en 1 y rechazar si terminan en 0
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

# Ejemplo de uso
if __name__ == "__main__":
    tm = TuringMachine(
        tape="1010",  # Aquí prueba con cadena que termina en 0 (rechazado)
        final_states=final_states,
        transition_function=transition_function
    )
    aceptado, cinta_final = tm.run()
    print(f"Aceptado: {aceptado}, Cinta final: {cinta_final}")
