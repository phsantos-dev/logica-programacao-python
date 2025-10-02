class Pessoa:
    """Classe que representa uma pessoa simples com nome, idade e gênero."""
    def __init__(self, nome: str, idade: int, genero: str) -> None:
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def cumprimentar(self) -> str:
        """Retorna uma saudação com o nome da pessoa."""
        return f"Olá, meu nome é {self.nome}."

    def aniversario(self) -> None:
        """Aumenta a idade em 1 (simula o aniversário)."""
        self.idade += 1

    def __str__(self) -> str:
        return f"{self.nome} — {self.idade} anos — {self.genero}"


def main() -> None:
    # Entrada de dados (quem executa o programa responde)
    nome = input("Qual seu nome? ")
    # Validação simples da idade (evita digitar texto)
    while True:
        try:
            idade = int(input("Qual sua idade? "))
            break
        except ValueError:
            print("Por favor, digite um número inteiro para a idade.")

    genero = input("Qual seu gênero? (ex: Masculino, Feminino, Outro) ")

    p = Pessoa(nome, idade, genero)

    print(p.cumprimentar())
    print(f"Idade atual: {p.idade} anos")
    p.aniversario()
    print(f"Idade após aniversário: {p.idade} anos")
    print("Resumo:", p)


if __name__ == "__main__":
    main()
