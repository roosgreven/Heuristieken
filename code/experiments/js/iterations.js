
/* 
This function sets variables for width and height, makes scalers
of the line chart, draws the lines

Args:
	titleName: name of the title of the graph 
	numberOfHouses: number of houses in the neighbourhood
*/ 
function createPlot(titleName, numberOfHouses) {

	// clear all svgs
	d3.selectAll(".chart").remove();

	d3.select("#chart").append("svg").attr("class", "chart")


	// add the title of the graph
	document.getElementById("graphTitle").innerHTML = "<h2><b>" + titleName + "</b>";

	// set margins, width and height
	var margin = {top: 50, right: 250, bottom: 170, left: 120},
		width = 900 - margin.left - margin.right,
		height = 500 - margin.top - margin.bottom;

	// attribute width and height to chart
	var chart = d3.select(".chart")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
		.append("g")
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	// scale the temperature and dates on range 
	var y = d3.scale.linear()
		.rangeRound([height, 0]);

	var x = d3.scale.linear()
		.range([0, width]);

	// set color scaler
	var color = d3.scale.ordinal() 
		.range(["red", "blue"]);

	// give correct values for line
	var line = d3.svg.line()
		.x(function(d) { return x(d.iteration) })
		.y(function(d) { return y(d.value) });

	// variable to draw the x axis below the graph, correctly scaled
	var xAxis = d3.svg.axis()
		.scale(x)
		.orient("bottom");

	// variable to draw the y axis on the left side, correctly scaled
	var yAxis = d3.svg.axis()
		.scale(y)
		.orient("left");

	// load json data
	d3.json("../data/iterations/" + String(numberOfHouses) + "_iterations.json", function(error, data) {

		// when there is an error, throw error and stop script
		if (error) {
			alert("error" + error);
			return;
		};


		

		// call function to draw graph
		drawLineGraph(data);		
	});

	/* 
	This function creates filtered data, sets domains for scalers, 
	adds the axes, draws the lines, makes the lines interactive, 
	by displaying the correct values for that spot and displaying
	a vertical line and circle that follow the mouse. Finally calls 
	a function to draw the legend.
	Takes in list of objects. Each object contains the average temperatures 
	for Chicago, Vancouver and De Bilt per day.
	*/

	drawLineGraph = function(data) {

		// define values of x axis to filter data on
		var label = 'iteration';

		// variable for filtered data without the label
		var varNames = d3.keys(data[0])
			.filter(function(key) { return key !== label; });

		// create an object with the filtered data 
		var dataArray = varNames.map(function (name) {
			return {
				name: name,
				values: data.map(function (d) {
					return {iteration: d[label], value: d[name] };
				})
			};
		});

		console.log(dataArray)

		// set the domain of the color scaler
		color.domain(varNames);

		// set domains of x and y scalers
		x.domain(d3.extent(data, function(d) { return d.iteration}));
		y.domain([ 
			d3.min(dataArray, function (c) { 
				return d3.min(c.values, function (d) { return d.value; });
			}),
			d3.max(dataArray, function (c) { 
				return d3.max(c.values, function (d) { return d.value; });
			})
		]);

		// draw x axis with names of countries and tick marks
		chart.append("g")
			.attr("class", "x axis")
			.attr("transform", "translate(0," + height + ")")
			.call(xAxis)
			.selectAll("text")	
				.style("text-anchor", "end")
				.attr("dx", "-.8em")
				.attr("dy", ".15em")
				.attr("transform", function(d) { return "rotate(-65)" });

		// add name for the x axis at the right position
		chart.append("text")
			.attr("x", width / 2.3)
			.attr("y", height + 75)
			.style("font", "18px sans-serif")
			.text("Iterations");

		// draw y axis with numbers and tick marks, name for x axis (rotated and at right position)
		chart.append("g")
			.attr("class", "y axis")
			.call(yAxis)
			.append("text")
				.attr("class", "values")
				.attr("transform", "rotate (-90)")
				.attr("y", -100)
				.attr("x", - height + (height / 2.5))
				.style("font", "18px sans-serif")
				.text("Value in millions \u20ac");

		// add group elements to the chart for the lines
		var series = chart.selectAll(".series")
			.data(dataArray)
			.enter().append("g")
				.attr("class", "series");

		// append path to draw the line
		series.append("path")
			.attr("class", "line")
			.attr("d", function(d) { return line(d.values); })
			.style("stroke", function (d) { return color(d.name); })
			.attr('stroke-width', 1)
			.attr('fill', 'none');

		drawLegend(data);
	};


	/*
	This function creates a legend. It sets it at right position 
	and scales. 
	Args:
		data: list of objects
		sorts: array of sorts 
	*/

	drawLegend = function(data) {
		console.log(data)

		// set sizes for legend
		var legendRectSize  = 2;
		var legendSpacing = 6;
		
		// ordinal scaler to set colors
		var legendColor = d3.scale.ordinal()
		.domain(["Simulated Annealing", "Hillclimber"])
		.range(["red", "blue"]);

		// add an svg for the legend
		var theLegend = chart.append("svg")
			.attr("width", width + 350)
			.attr("height", height)
			.append("g")
				.attr("transform", "translate(" + (width + 100) + ", 50)");

		// add space for legend and set it at the right spot
		var legend = theLegend.selectAll(".legend")
			.data(legendColor.domain())
			.enter().append("g")
			.attr("class", "legend")
			.attr("transform", function(d, i) {
				var height = legendRectSize + legendSpacing;
				var offset =  height * legendColor.domain().length / 2;
				var horz = -2 * legendRectSize;
				var vert = i * height - offset;
				return "translate(" + horz + "," + (vert * 3) + ")"; });

		// add rectangles for color
		legend.append("rect")
			.attr("width", legendRectSize * 10)
			.attr("height", legendRectSize)
			.style("fill", legendColor)
			.style("stroke", legendColor);

		// add the text per block
		legend.append("text")
			.attr("x", (legendRectSize * 10) + legendSpacing)
			.attr("y", legendRectSize)
			.style("font", "sans-serif")
			.text(function(d) { return d; });
	};
};


