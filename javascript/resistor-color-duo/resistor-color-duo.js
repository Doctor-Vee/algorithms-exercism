export const value = (colorArray) => {
  const colors = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"];
  let code = colorArray.reduce((acc, value) => {
    if (acc.length < 2) {
      acc += colors.indexOf(value);
    }
    return acc;
  }, "")
  return parseInt(code);
};