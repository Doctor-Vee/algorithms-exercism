export const validate = (x) => {
  const numstr = x.toString();
  const pow = numstr.length;
  let sum = 0;

  for (let i = 0; i < pow; i++)
  {
    sum+= Math.pow(parseInt(numstr[i]), pow);
  }
  return sum == x ? true : false;
};