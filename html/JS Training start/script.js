let i = 1

for (i; i < 10; i++){
    console.log("ich wurde das " + i + ". mal gezählt")
}
console.log("ich bin fertig")


console.log("__________________________")
console.log("__________________________")

let listProgramming = [
    "C#",
    "C++",
    "Python",
    "Javascript",
];

for (x of listProgramming){
    console.log("Eintrag index " + listProgramming.indexOf(x)+ " = " + x )
}

console.log("__________________________")
console.log("__________________________")

let count = 200
while(count <= 210){
    console.log("die zahl ist " + count)
    count++
}
