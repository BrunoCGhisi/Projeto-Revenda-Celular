// VO = Value Object, isso é um objeto que VAI ser percorrido pela WEB, é uma boa prática declarar dessa forma
// Estou tipando Category VO com as variaveis que ficam dentro da tabela Categoria
// Nesse caso:

export type ProductVO = {
    id: string  //Se torna uma string
    descricao: string     //Se torna uma string
    idmarca: string     //Se torna uma string
    valor: string     //Se torna uma string
    foto1: string  //Se torna uma string
    foto2: string     //Se torna uma string
}
//proximo passo é index.ts
