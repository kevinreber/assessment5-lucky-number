function starOutGrid(grid) {
    const new_grid = [];
    const star = "*";
    console.log(grid)
    for (let row of grid) {
        // create rows for new_grid
        if (row.includes(star)) {
            changeRowToStar(row, star, new_grid);
        } else new_grid.push(row);
    }
    for (let row of grid) {
        // replace columns gor new_grid
        for (let [i, el] of row.entries()) {
            if (el === "*") {
                changeColumnToStar(i, new_grid, star);
            }
        }
    }
    return new_grid;
}

function changeRowToStar(row, star, grid) {
    // Adds row of stars into grid
    new_row = [];
    for (let el of row) {
        new_row.push(star);
    }
    grid.push(new_row);
    return grid;
}

function changeColumnToStar(index, grid, star) {
    // Replaces column of grid with stars
    for (let row of grid) {
        row.splice(index, 1, star);
    }
    return grid;
}