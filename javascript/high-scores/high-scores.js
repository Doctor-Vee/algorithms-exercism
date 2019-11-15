export class HighScores {
  constructor(input) {
    this.input =[];
    input.forEach((value)=>this.input.push(value));
    this.last = input[input.length-1]
    this.sorted = input.sort((a,b)=>b-a);
  }

  get scores() {
    return this.input
  }

  get latest() {
    return this.last;
  }

  get personalBest() {
    return this.sorted[0]
  }

  get personalTopThree() {
    return this.sorted.slice(0, 3);
  }
}


console.log((new HighScores([10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]).personalTopThree))