/*jslint vars: true, plusplus: true, devel: true, nomen: true, indent: 4, maxerr: 50 */
/*global define */

var neighbour = function (x, y) {
    // Given coordinate values, makes a location object
    "use strict";
	return {x: x, y: y};
};

var getNeighbours = function (array, location) {
    /* Returns an array containing location objects for all neighbours of the 
     * cell at array[location.y][location.x]
     */
    "use strict";
	var neighbours = [];
	if (location.x !== 0) {
        // left
		neighbours.push(neighbour(location.x - 1, location.y));
	}
	if (location.y !== 0) {
        // above
		neighbours.push(neighbour(location.x, location.y - 1));
	}
	if (location.y !== 0 && location.x !== 0) {
        // left-above
		neighbours.push(neighbour(location.x - 1, location.y - 1));
	}
	if (location.x < array[0].length - 1) {
        // right
		neighbours.push(neighbour(location.x + 1, location.y));
	}
	if (location.y < array.length - 1) {
        // below
		neighbours.push(neighbour(location.x, location.y + 1));
	}
	if (location.y < array.length - 1 && location.x < array[0].length - 1) {
        // right-below
		neighbours.push(neighbour(location.x + 1, location.y + 1));
	}
	if (location.x !== 0 && location.y < array.length - 1) {
        // left-below
		neighbours.push(neighbour(location.x - 1, location.y + 1));
	}
	if (location.y !== 0 && location.x < array[0].length - 1) {
        // right-above
		neighbours.push(neighbour(location.x + 1, location.y - 1));
	}
	return neighbours;
};

var transition = function (state, aliveNeighbours) {
    /* State transition function: returns new state given a current state and number
     * of alive neighbours
     */
    "use strict";
    if (state === 1) {
        if (aliveNeighbours < 2 || aliveNeighbours > 3) {
            return 0;
        } else {
            return 1;
        }
    } else {
        if (aliveNeighbours === 3) {
            return 1;
        } else {
            return 0;
        }
    }
};

var getAliveNeighbours = function (array, location) {
    // Returns the number of alive neighbours for a given location object (coordinate pair)
    "use strict";
    var i, alive = 0;
    var neighbours = getNeighbours(array, location);
	for (i = 0; i < neighbours.length; i++) {
        var coord = neighbours[i];
        if (array[coord.y][coord.x] === 1) {
            alive++;
        }
    }
    return alive;
};

var getNewState = function (array, location) {
    // Returns the next state (1 or 0) for a given location object (coordinate pair)
    "use strict";
    var numAlive = getAliveNeighbours(array, location);
    return transition(array[location.y][location.x], numAlive);
};

var updateGameState = function (array) {
    // 
    "use strict";
    if (array.length <= 0 && array[0].length <= 0) {
        console.log("Invalid game board");
        return;
    }
    var previousIteration = [];
    for (var k=0; k < array.length; k++) {
        previousIteration.push(array[k].slice());
    }
    var i, j;
    
    for (i = 0; i < array.length; i++) {
        for (j = 0; j < array[0].length; j++) {
            array[i][j] = getNewState(previousIteration, {x: j, y: i});
        }
    }
    return;
};

var initialState = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
];


var gameState = initialState;

// React code

window.GameCell = React.createClass({
    render: function () {
        return (
            <div className="gameCell" style={{width:50, height:50, backgroundColor:this.props.value ? "#30D030" : "black", display:"table-cell", border:"1px solid #303030"}}></div>
        );
    }
});

window.GameRow = React.createClass({
    render: function () {
        var tags = [];
        for (var i=0; i < this.props.cells.length; i++) {
            tags.push(<GameCell key={this.props.rowNum.toString() + "," + i.toString()} value={this.props.cells[i]} style={{display:"table-row"}} colNum={i}/>);
        }
        return (
            <div className="gameRow">
                {tags}
            </div>
        );
    }
});

window.GameArray = React.createClass({
    render: function () {
        var tags = [];
        for (var i=0; i < this.props.gameState.length; i++) {
            tags.push(<GameRow key={"row" + i.toString()} cells={this.props.gameState[i]} rowNum={i}/>);
        }
        return (
            <div className="gameArray" style={{display:"table"}}>
                {tags}
            </div>
        );
    }
});

// Put functions into window namespace for HTML-embedded script
window.gameState = gameState;
window.updateGameState = updateGameState;
window.getAliveNeighbours = getAliveNeighbours;
window.transition = transition;