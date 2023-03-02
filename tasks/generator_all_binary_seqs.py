def generate_sequences(n):
    if n == 1:
        return ['0', '1']
    else:
        previous_sequences = generate_sequences(n-1)
        new_sequences = []
        for seq in previous_sequences:
            new_sequences.append(seq+'0')
            new_sequences.append(seq+'1')
        return new_sequences


print(generate_sequences(4))
