export const isPangram = (sentence) => {
  sentence = sentence.toUpperCase();
  let letter;
  for(let i = 65; i < 91; i++){
    letter = String.fromCharCode(i);
    if (!sentence.includes(letter)) return false
  }
  return true;
};