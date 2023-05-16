class Graph {
	constructor() {
		this.edges = {};
	}

	addEdge(node1, node2) {
		this.edges[node1] = [...(this.edges[node1] || []), node2];
	}

	hasPathDFS(startNode, endNode, visited = {}) {
		if (startNode === endNode) return true;
		visited[startNode] = true;
		return (this.edges[startNode] || []).some((node) => !visited[node] && this.hasPathDFS(node, endNode, visited));
	}
}

// Example
const graph =  new Graph();

graph.addEdge('A', 'B');
graph.addEdge('B', 'C');
graph.addEdge('C', 'D');

console.log(graph.hasPathDFS('A', 'D'));	// true
console.log(graph.hasPathDFS('D', 'A'));	// false
