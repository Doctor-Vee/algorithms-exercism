export const gigasecond = (date) => {
  const giga = date.getTime() + 1000000000000
return new Date(giga);
};