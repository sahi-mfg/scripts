"""
On définit la  valuation p-adique pour p nombre premier et n entier naturel non nul.

Si p divise n, on note v_p(n) le plus grand entier k tel que p^k divise n.
Si p ne divise pas n, on pose v_p(n) = 0.

L'entier v_p(n) est appelé valuation p-adique de n.
"""

from math import sqrt


def est_premier(n: int) -> bool:
    """
    Détermine si un entier est premier ou non

    Args:
        n : int : Entier à vérifier

    Returns:
        bool : True si l'entier est premier, False sinon
    """
    if n < 2:
        return False
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def liste_premiers(n: int) -> list:
    """
    Retourne la liste des nombres premiers inférieurs à n

    Args:
        n : int : Limite supérieure

    Returns:
        list : Liste des nombres premiers inférieurs à n
    """
    return [p for p in range(2, n) if est_premier(p)]


def valuation_p_adique(n: int, p: int) -> int:
    """
    Calcule la valuation p-adique d'un entier n

    Args:
        p : int : Nombre premier
        n : int : Entier naturel non nul

    Returns:
        int : Valuation p-adique de n
    """
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def val(n: int, p: int) -> int:
    """Calcul de la valuation p-adique de manière recursive

    Args:
        n : int : Entier naturel non nul
        p : int : Nombre premier

    Returns:
        int : Valuation p-adique de n
    """
    if n % p == 0:
        return 1 + val(n // p, p)
    return 0


def decomposition_facteurs_premiers(n: int) -> list[list[int]]:
    """
    Décompose un entier en facteurs premiers

    Args:
        n : int : Entier à décomposer

    Returns:
        dict : Dictionnaire des facteurs premiers
    """
    facteurs = [
        [p, valuation_p_adique(n, p)]
        for p in liste_premiers(n)
        if valuation_p_adique(n, p) > 0
    ]
    return facteurs


def main() -> None:
    n = 289
    for p in liste_premiers(n):
        print(f"v_{p}({n}) = {valuation_p_adique(n, p)}")
    print(f"Décomposition en facteurs premiers: {decomposition_facteurs_premiers(n)}")


if __name__ == "__main__":
    main()
