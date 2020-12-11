"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    T=float(input("Qual a temperatura em grau Celsius ?\n"))
    F=T*9/5+32
    print(f"A temperatura em Fahrenheit é {F}.")

if __name__ == '__main__':
    main()
