export class Matrix {
  constructor(array) {
    this.lines = array.split("\n");
  }

  get rows() {
    return this.lines.map((line) => line.split(" ").map((y) => parseInt(y)));
  }

  get columns() {
    let temp = [];
    let column = [];
    const rL = this.rows[0].length;
    const cL = this.rows.length;
    for (let i = 0; i < rL; i++) {
      for (let j = 0; j < cL; j++) {
        temp.push(this.rows[j][i])
      }
      column.push(temp)
      temp = [];
    }
    return column;
  }
}