# 05-sort-desc-js

## Objetivo
Ordenar um array em ordem decrescente sem usar `.sort()`.

## Exemplo
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

const arr = [3, 9, 2, 7];
console.log(quickSortDesc(arr));

```
