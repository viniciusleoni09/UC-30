programa{
    funcao inicio() {
        real valorCasa,Salario,prestacao
        inteiro anos,meses

        escreva("qual o valor da casa :")
        leia(valorcasa)

        escreva("qual e o seu salario:")
        leia(salario)

        escreva("Em quantos anos voce dejesa pagar:")
        leia(anos)

        meses= anos* 12
        prestacao = valorCasa / meses

        escreva("O valor da prestação e " , prestacao)

        se( pretacao <= salario * 0.30) {
            escreva("emprestimo aprovado  \n")
        } senao{
            escreva("emprestimo não aprovado \n")
        }
        

    }
}