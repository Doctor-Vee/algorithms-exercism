export class Series {
  constructor(array) {
    this.series = [];
    this.all = array.split("").map((y)=>parseInt(y))
  }

  get digits() {
    return this.all;
  }

  slices(length) {
    if (length > this.digits.length) throw new Error("Slice size is too big.");
    let i = 0;
    while(i+length <= this.digits.length){
      this.series.push(this.digits.slice(i, i+length));
      i++;
    }
    return this.series;
  }
}