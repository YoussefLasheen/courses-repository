//Call the makeGrid() function and give it the "w" and "h" values from the sizePicker Object when the User clicks the Submit button Object
document.getElementById('sizePicker').onsubmit = function () {
    event.preventDefault();
    const height = document.getElementById('inputHeight').value;
    const width = document.getElementById('inputWidth').value;
    makeGrid(height, width);
};
document.getElementById('defaultsScreenButton').onclick = function () {
    makeDefaultTable();
};

function makeGrid(w, h) {
    const pixelCanvas = document.getElementById("pixelCanvas");
    const numberOfRows = pixelCanvas.rows.length;
    //Delete the pervious table to not duplicATE
    for (let i = 0; i < numberOfRows; i++) {
        pixelCanvas.deleteRow(0);
    }
    //Making of the table
    for (let i = 0; i < h; i++) {
        //Add the columns first
        const x = pixelCanvas.insertRow(i);
        //Then loop for the cells
        for (let j = 0; j < w; j++) {
            const c = x.insertCell(j);
            console.log(c);
            paintCell(c);
        }
    }
    // Your code goes here!
}


//Add the coloring function for the table
function paintCell(c) {
    const colorPicker = document.getElementById("colorPicker");
    c.onclick = function () {
        color = document.getElementById("colorPicker").value;
        this.style.backgroundColor = color;
    }
}
//Add a default table with default colors to display "THANK YOU" Message
function makeDefaultTable() {
    //Add the dimensions of the cells you want to fill
    var defaultCells =
        [[0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0],
        [0, 5, 0], [0, 6, 0], [0, 9, 0], [0, 12, 0],
        [0, 15, 0], [0, 16, 0], [0, 17, 0], [0, 18, 0],
        [0, 21, 0], [0, 22, 0], [0, 23, 0], [0, 24, 0],
        [0, 27, 0], [0, 29, 0], [1, 1, 0], [1, 2, 0],
        [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0],
        [1, 9, 0], [1, 12, 0], [1, 15, 0], [1, 18, 0],
        [1, 21, 0], [1, 24, 0], [1, 27, 0], [1, 29, 0],
        [2, 3, 0], [2, 4, 0], [2, 9, 0], [2, 12, 0],
        [2, 15, 0], [2, 18, 0], [2, 21, 0], [2, 24, 0],
        [2, 27, 0], [2, 29, 0], [3, 3, 0], [3, 4, 0],
        [3, 9, 0], [3, 10, 0], [3, 11, 0], [3, 12, 0],
        [3, 15, 0], [3, 16, 0], [3, 17, 0], [3, 18, 0],
        [3, 21, 0], [3, 24, 0], [3, 27, 0], [3, 28, 0],
        [4, 3, 0], [4, 4, 0], [4, 9, 0], [4, 10, 0],
        [4, 11, 0], [4, 12, 0], [4, 15, 0], [4, 18, 0],
        [4, 21, 0], [4, 24, 0], [4, 27, 0], [4, 28, 0],
        [5, 3, 0], [5, 4, 0], [5, 9, 0], [5, 12, 0],
        [5, 15, 0], [5, 18, 0], [5, 21, 0], [5, 24, 0],
        [5, 27, 0], [5, 29, 0], [6, 3, 0], [6, 4, 0],
        [6, 9, 0], [6, 12, 0], [6, 15, 0], [6, 18, 0],
        [6, 21, 0], [6, 24, 0], [6, 27, 0], [6, 29, 0],
        [7, 3, 0], [7, 4, 0], [7, 9, 0], [7, 12, 0],
        [7, 15, 0], [7, 18, 0], [7, 21, 0], [7, 24, 0],
        [7, 27, 0], [7, 29, 0], [11, 9, 0], [11, 13, 0],
        [11, 16, 0], [11, 17, 0], [11, 18, 0], [11, 19, 0],
        [11, 20, 0], [11, 24, 0], [11, 27, 0], [12, 9, 0],
        [12, 13, 0], [12, 16, 0], [12, 20, 0], [12, 24, 0],
        [12, 27, 0], [13, 9, 0], [13, 10, 0], [13, 11, 0],
        [13, 12, 0], [13, 13, 0], [13, 16, 0], [13, 20, 0],
        [13, 24, 0], [13, 27, 0], [14, 11, 0], [14, 16, 0],
        [14, 20, 0], [14, 24, 0], [14, 27, 0], [15, 11, 0],
        [15, 16, 0], [15, 20, 0], [15, 24, 0], [15, 27, 0],
        [16, 11, 0], [16, 16, 0], [16, 20, 0], [16, 24, 0],
        [16, 27, 0], [17, 11, 0], [17, 16, 0], [17, 20, 0],
        [17, 24, 0], [17, 27, 0], [18, 11, 0], [18, 16, 0],
        [18, 20, 0], [18, 24, 0], [18, 27, 0], [19, 11, 0],
        [19, 16, 0], [19, 17, 0], [19, 18, 0], [19, 19, 0],
        [19, 20, 0], [19, 24, 0], [19, 25, 0], [19, 26, 0],
        [19, 27, 0]
    ];
    makeGrid(30, 20);
    for (let i = 0; i <= defaultCells.length; i++) {
        q = document.getElementById('pixelCanvas').rows[defaultCells[i][0]].cells[defaultCells[i][1]];
        color = document.getElementById("colorPicker").value;
        q.style.backgroundColor = color;

    }
}
makeDefaultTable(); 