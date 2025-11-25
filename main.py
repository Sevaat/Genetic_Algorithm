from typing import List
from src.evolutionary_algorithm import EvolutionaryAlgorithm


def main():
    def user_function(param: List[str]):
        return sum([float(p) for p in param])

    EvolutionaryAlgorithm.classical_genetic_algorithm(user_function)


if __name__ == '__main__':
    main()
