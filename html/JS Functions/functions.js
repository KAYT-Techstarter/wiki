function calc(number1, number2 , globalVariable) {
    let plusCount = number1 + number2
    console.log("Die Variable plusCount ist nur in der Function verfügbar daher ist der inhalt: " + plusCount)
    console.log("Das ergebniss ist " + plusCount + ". Es wurde " + number1 + " + " + number2 + " zusammen gerechnet")
    if (globalVariable == true ) {
        console.log("Die gloale Variable war True")
    }
    return plusCount
}

let globalVariable = true

calc(17, 23, globalVariable)




