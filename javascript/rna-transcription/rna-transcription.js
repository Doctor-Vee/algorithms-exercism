export const toRna = (dna) => {
  let rna = ""
  for (const alpha of dna) {
    // rna += alpha
    switch (alpha) {
      case "G":
        rna += "C";
        break;
      case "C":
        rna += "G";
        break;
      case "T":
        rna += "A";
        break;
      case "A":
        rna += "U";
        break;
    }
  }
  return rna;
};

console.log(toRna("G"))