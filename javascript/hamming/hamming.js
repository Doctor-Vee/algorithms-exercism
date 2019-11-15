export const compute = (strandA, strandB) => {

  let count = 0;
  if (strandA.length == 0 && strandB.length == 0) return 0;
  if (strandA.length == 0) throw new Error("left strand must not be empty");
  if (strandB.length == 0) throw new Error("right strand must not be empty");
  if (strandA.length !== strandB.length) throw new Error("left and right strands must be of equal length");

  for(let i = 0; i < strandA.length; i++){
    if (strandA[i] !== strandB[i]) count += 1;
  }
  return count;
};