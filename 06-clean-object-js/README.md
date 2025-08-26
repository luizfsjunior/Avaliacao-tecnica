# 06-clean-object-js

## Objetivo
Remover propriedades de um objeto com valor `null` ou `undefined`.

## Exemplo
```js
function cleanObject(obj) {
  return Object.fromEntries(
    Object.entries(obj).filter(([_, v]) => v != null)
  );
}
console.log(cleanObject({a: 1, b: null, c: undefined, d: 2})); // {a: 1, d: 2}
```
