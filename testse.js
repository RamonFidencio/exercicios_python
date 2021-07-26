let line = gets()

line.split("");
let H = parseInt(line[0]);
let P = parseInt(line[1]);

let media = H*P;       
let mediaFinal = media/12;

console.log(mediaFinal.toFixed(3));