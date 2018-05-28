/* 
Name: Roos Greven
11436700
Homework week 5: make an interactive line graph with D3.
*/

/* 
This function creates the plot, draws the lines, 
makes it interactive by displaying values and drawing 
a line and a circle and adds the legend. Takes in a year,
which is later used to load the correct dataset. Finally
calls a function to draw the lines.
*/ 
function createPlot(titleName, numberOfHouses) {

	// clear all svgs
	d3.selectAll(".chart").remove();

	d3.select("#chart").append("svg").attr("class", "chart")


	// add the title of the graph
	document.getElementById("graphTitle").innerHTML = "<h2><b>" + titleName + "</b>";

	// set margins, width and height
	var margin = {top: 50, right: 180, bottom: 170, left: 120},
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
	d3.json(String(numberOfHouses) + "_iterations" + ".json", function(error, data) {

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
			.attr("y", height + 65)
			.style("font", "18px sans-serif")
			.text("Iterations");

		// draw y axis with numbers and tick marks, name for x axis (rotated and at right position)
		chart.append("g")
			.attr("class", "y axis")
			.call(yAxis)
			.append("text")
				.attr("class", "values")
				.attr("transform", "rotate (-90)")
				.attr("y", -80)
				.attr("x", - height + (height / 2.5))
				.style("font", "18px sans-serif")
				.text("Value");

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

		// add the correct description for the lines at the right spot 
		series.append("text")
			.datum(function(d) {
				return {
					name: d.name,
					value: d.values[d.values.length - 1]
				};
			})
			.attr("transform", function(d) {
				return "translate(" + (width + 5) + "," + y(d.value.value) + ")";
			})
			.attr("x", 0)
			.attr("dy", ".35em")
			.attr("class", "linetext")
			.text(function(d) {
				return d.name;
			});

	};
};


