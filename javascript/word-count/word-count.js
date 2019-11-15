export class Words {
  count(wordly) {
    wordly = wordly.toLowerCase()
    let words = wordly.split(" ")
    return words
  }
}

let test = new Words;
console.log(test.count('go Go GO'))