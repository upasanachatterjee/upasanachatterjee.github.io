var round = 0;
var board = new Array(9).fill(false);
var xBoard = new Array(9).fill(false);
var oBoard = new Array(9).fill(false);
var finishedGame = false;

function reset() {
    round = 0;
    board = new Array(9).fill(false);
    xBoard = new Array(9).fill(false);
    oBoard = new Array(9).fill(false);
    finishedGame = false;
    document.getElementById("winner").innerText = "";
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const box = "b_" + i.toString() + j.toString();
            const box_element = document.getElementById(box);
            box_element.innerHTML = "";
        }
    }
}   

function makeMove(x, y, roboMove=false) {
    if (isValidMove(x, y)) {
        const box = "b_" + x.toString() + y.toString();
        const player = getPlayer();
        const box_element = document.getElementById(box);
        box_element.innerHTML = player;
        const cellPlayed = getCell(x,y);
        storeMove(cellPlayed, player);
        if (getWin(player)) {
            return;
        }
        if (getStalemate()) {
            return;
        }
        incrementPlayer();

        if (!roboMove) {
            const move = getValidMove();
            makeMove(move[0], move[1], true);
        }
    }
}

function getWin(player) {
    const board = getPlayerBoard(player);
    const horizontalWin = getHorizontalWin(board);
    const verticalWin = getVerticalWin(board);
    const diagonalWin = getDiagonalWin(board);
    if (horizontalWin || verticalWin || diagonalWin) {
        endGame(player);
        return true;
    }
    return false;
}

function getStalemate() {
    if (board.every(cell => cell === true)) {
        endGame();
        return true;
    }
    return false;
}

// HELPERS

function getValidMove() {
    let move = Math.floor(Math.random() * 9);
    while (board[move]) {
        move = Math.floor(Math.random() * 9);
    }
    const y = move % 3;
    const x = (move - y) / 3;
    return [x, y];

}

function endGame(player) {
    let text = "";
    if (player) {
        text = player + " wins!";
    }
    else {
        text = "Stalemate!"
    }
    
    document.getElementById("winner").textContent = text;
    finishedGame = true;
}

function getHorizontalWin(board) {
    for (let i = 0; i < 3; i++) {
        if (board[getCell(i, 0)] && board[getCell(i, 1)] && board[getCell(i, 2)]) {
            return true;
        }
    }
    return false;
}

function getVerticalWin(board) {
    for (let j = 0; j < 3; j++) {
        if (board[getCell(0, j)] && board[getCell(1, j)] && board[getCell(2, j)]) {
            return true;
        }
    }
    return false;
}

function getDiagonalWin(board) {
    if (board[getCell(0, 0)] && board[getCell(1, 1)] && board[getCell(2, 2)]) {
        return true;
    }
    if (board[getCell(0, 2)] && board[getCell(1, 1)] && board[getCell(2, 0)]) {
        return true;
    }
    return false;
}

function getPlayerBoard(player) {
    return player === "X" ? xBoard : oBoard;
}

function storeMove(cell, player) {
    board[cell] = true;
    switch (player) {
        case "X":
            xBoard[cell] = true;
            break;
        case "O":
            oBoard[cell] = true;
            break;
    }
}
function incrementPlayer() {
    round++;
}
function getPlayer() {
    return round % 2 == 0 ? "X" : "O";
}

function getCell(x, y) {
    return 3*x + y;
}

function isValidMove(x, y) {
    const cell = getCell(x, y);
    const cellFilled = board[cell];
    return !cellFilled && !finishedGame;
}