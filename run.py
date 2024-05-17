from src import clear


def main():
    
    def clean_empty_lines(lines: list[str]):  return [line for line in lines if line != []]

    raw_lines = []
    new_lines = [['']]

    with open("output.txt", 'r') as output: raw_lines = output.readlines()

    processed = clear.cleared(clean_empty_lines(raw_lines))

    new_lines.append(processed.one_line)
    new_lines.append('\n\n')
    new_lines.append(processed.lines)

    with open("output.txt", 'w') as output:
        for line in new_lines:  output.write(line)


if __name__=='__main__':    main()