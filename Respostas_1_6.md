# Avaliação Técnica de Lógica e Desenvolvimento

## 1. Webhook Leads
**Pergunta:**
Um cliente envia um formulário com 3 campos: nome, email e telefone. O webhook recebe os dados no seguinte formato: `{ "full_name": "Maria Oliveira", "contact": { "email": "maria@teste.com", "phone": "11999998888" } }`. Queremos salvar isso em uma tabela de banco de dados chamada leads, que possui as colunas: nome, email, telefone. Explique como você faria o mapeamento entre os campos recebidos e as colunas da tabela.

**Resposta:**
Para salvar os dados corretamente, eu pego o valor de `full_name` e coloco na coluna `nome`, o `contact.email` vai para a coluna `email` e o `contact.phone` para `telefone`. Faço essa conversão direto na API, extraindo cada campo do JSON e salvando no banco.

---

## 2. Fanout APIs
**Pergunta:**
Um fluxo precisa enviar os mesmos dados para 3 APIs diferentes. Porém, se uma API falhar, o processo não pode parar — é necessário continuar tentando as outras e apenas registrar o erro ocorrido. Como você estruturaria essa lógica?

**Resposta:**
Utilizo um loop para enviar os dados para cada API. Se uma falhar, registro o erro (em log ou banco) e continuo o envio para as demais. Assim, o processo é resiliente e não interrompe o fluxo por falhas pontuais.

---

## 3. Bulk Sender
**Pergunta:**
Você recebeu uma lista com 1.000 leads em JSON. A API de destino só aceita receber 100 leads por vez. Como garantir que todos os 1.000 leads sejam enviados, sem perda e sem repetição?

**Resposta:**
Divido a lista em lotes de 100 usando slicing e envio cada lote sequencialmente. Dessa forma, todos os leads são enviados, sem repetição ou perda.

---

## 4. Compare Equality (JavaScript)
**Pergunta:**
Explique a diferença entre usar `==` e `===` em JavaScript, e mostre um exemplo.

**Resposta:**
O operador `==` compara os valores, mas converte o tipo se necessário. Já o `===` compara valor e tipo, sem conversão. Por exemplo:
```js
1 == '1' // true
1 === '1' // false
```

---

## 5. Sort Desc
**Pergunta:**
Dado o array abaixo: `const arr = [3, 9, 2, 7];` Reordene os números em ordem decrescente, sem usar `.sort()`.

**Resposta:**
Como nao sera utilizado o `.sort()`, irei para uma abordagem de um algoritmo de ordenação.
Utilizo, para maior eficiência, o algoritmo quicksort in-place, que tem complexidade média O(n log n) e não duplica o array.
Primeiro, ele escolhe um elemento do array para ser o “pivô” (geralmente o último da lista). Depois, ele separa os outros elementos em dois grupos: os maiores que o pivô e os menores. Para ordenação decrescente, os maiores ficam à esquerda e os menores à direita.
Feito isso, ele coloca o pivô no meio desses dois grupos, na posição correta. Aí, ele repete esse processo para cada grupo, dividindo e organizando até que todo o array esteja em ordem.
Exemplo:
```js
function quickSortDesc(array, left = 0, right = array.length - 1) {
  if (left < right) {
    const pivotIndex = partition(array, left, right);
    quickSortDesc(array, left, pivotIndex - 1);
    quickSortDesc(array, pivotIndex + 1, right);
  }
  return array;
}
function partition(array, left, right) {
  const pivot = array[right];
  let i = left;
  for (let j = left; j < right; j++) {
    if (array[j] > pivot) {
      [array[i], array[j]] = [array[j], array[i]];
      i++;
    }
  }
  [array[i], array[right]] = [array[right], array[i]];
  return i;
}
```

---

## 6. Clean Object
**Pergunta:**
Escreva uma função que receba um objeto e remova todas as propriedades que tenham valor null ou undefined.

**Resposta:**
Uso o `Object.entries` para pegar todas as propriedades e filtro só as que têm valor diferente de `null` ou `undefined`. Depois reconstruo o objeto com `Object.fromEntries`. Exemplo:
```js
function cleanObject(obj) {
  return Object.fromEntries(
    Object.entries(obj).filter(([_, v]) => v != null)
  );
}
```

---

## 7. Atividade Prática - Catálogo de Países
**Extra:**
Implementei uma API completa em FastAPI + PostgreSQL, com endpoints para listar, buscar e avaliar países, consumindo a REST Countries e persistindo avaliações. O código está organizado em pastas separadas, com Docker e scripts de teste para facilitar o uso e validação.
