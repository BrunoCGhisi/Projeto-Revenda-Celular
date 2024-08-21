// VO = Value Object, isso é um objeto que VAI ser percorrido pela WEB, é uma boa prática declarar dessa forma
// Estou tipando Category VO com as variaveis que ficam dentro da tabela Categoria
// Nesse caso:

export type ModelVO = {
    id: string  //Se torna uma string
    nome: string     //Se torna uma string
}

//proximo passo é index.ts