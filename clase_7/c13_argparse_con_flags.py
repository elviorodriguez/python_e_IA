# -*- coding: utf-8 -*-

def func_B(x, y, resta=False):
    if resta:
        print(x, "-", y, "=", x - y)
    else:
        print(x, "+", y, "=", x + y)

if __name__ == "__main__":
    
    # Permite interpretar argumentos de CLI
    import argparse
    parser = argparse.ArgumentParser()
    
    # Argumentos obligatorios
    parser.add_argument("x", type=float, help="Primer número")
    parser.add_argument("y", type=float, help="Segundo número")

    # Opción booleana
    parser.add_argument(
        "--resta", action="store_true",
        help="Realiza una resta en lugar de una suma"
    )
    
    # Interpretar los argumentos
    args = parser.parse_args()
    
    # Usar los argumentos
    func_B(args.x, args.y, args.resta)

