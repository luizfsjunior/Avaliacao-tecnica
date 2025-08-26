function cleanObject(obj) {
  return Object.fromEntries(
    Object.entries(obj).filter(([_, v]) => v != null)
  );
}

const exemplo = {a: 1, b: null, c: undefined, d: 2};
console.log(cleanObject(exemplo));
