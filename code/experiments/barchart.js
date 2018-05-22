/* 
Name: Roos Greven
11436700
Homework week 3: make an interactive bar chart with D3.
*/

function createPlot(algorithmToCompare, side, titleName) {

	// add the title of the graph
	document.getElementById("graphTitle" + side).innerHTML = "<h2><b>" + titleName + "</b>";

	// clear all svgs
	d3.selectAll("." + side + "Chart").remove();

	d3.select("#" + side + "Chart").append("svg").attr("class", side + "Chart")

	// set margins, width and height
	var margin = {top: 50, right: 30, bottom: 170, left: 80},
		width = 550 - margin.left - margin.right,
		height = 500 - margin.top - margin.bottom;

	// attribute width and height to chart
	var chart = d3.select("." + side + "Chart")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
		// append g to set the chart at the right spot
		.append("g")
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	// scale the datapoints on range 
	var y = d3.scale.linear()
		.range([height, 0]);

	// scale the name values on range
	var x = d3.scale.ordinal()
		.rangeRoundBands([0, width], .1);

	// variable to draw the x axis below the bars, correctly scaled
	var xAxis = d3.svg.axis()
		.scale(x)
		.orient("bottom");

	// variable to draw the y axis on the left side, correctly scaled
	var yAxis = d3.svg.axis()
		.scale(y)
		.orient("left");

	// load the data 
	d3.json(algorithmToCompare + ".json", function(error, data) {

		// alert if there is an error and return to stop the script
		if (error) {
			alert("Error: " + error);
			return;
		};

		// call the function to draw the bar chart
		drawBarChart(data);
	});

	/* 
	This function sorts data, completes the scalers draws x and y axis 
	of the bar chart with the right text, draws bars and makes the bars 
	interactive by changing color and displaying the value on mouse hover. 
	Takes in list of objects. Each object contains a name and a value. 

	*/
	var drawBarChart = function(data) {

	    // set correct domains of x and y scaler
		x.domain(data.map(function(d) { return d.range }));
		y.domain([d3.min(data, function(d) { return d.frequency }), d3.max(data, function(d) { return d.frequency })]);
			
		// draw x axis with value ranges and tick marks
		chart.append("g")
			.attr("class", "x axis")
			.attr("transform", "translate(0," + height + ")")
			.call(xAxis)
			.selectAll("text")	
				.style("text-anchor", "end")
				.attr("dx", "-.8em")
				.attr("dy", ".15em")
				.attr("transform", function(d) { return "rotate(-65)" });

		// add name for the x axis
		chart.append("text")
			// set at the right position
			.attr("x", width / 2.5)
			.attr("y", height + margin.bottom / 1.05)
			.style("font", "18px sans-serif")
			.text("Values");
			
		// draw y axis with numbers, tick marks and name y axis
		chart.append("g")
			.attr("class", "y axis")
			.call(yAxis)
			.append("text")
				.attr("class", "values")
				.attr("transform", "rotate (-90)")
				.attr("y", - margin.left / 1.5)
				.attr("x", - height + 60)
				.style("font", "18px sans-serif")
				.text("Frequency");
			
		// draw the bars
		chart.selectAll(".bar")
			.data(data)
			.enter().append("rect")
				.attr("class", "bar")
				.attr("y", function(d) { return y(d.frequency) })
				.attr("x", function(d) { return x(d.range) })
				.attr("width", x.rangeBand())
				.attr("height", function(d) { return height - y(d.frequency) })
				// function for changes when mouse hovers over bar
				.on("mouseover", function(d) {
						chart.append("text")
						.attr("id", "interactivity")
						.attr("y", y(d.frequency) - 15)
						.attr("x", x(d.range) + 10)
						.style("text-anchor", "middle")
						.style("font", "10px sans-serif")
						.text(d.frequency);
					d3.select(this)
						.style("fill", "darkblue")
				})
				// function to go back to normal when mousehover is over
				.on("mouseout", function(d) {
					d3.select(this)
						.style("fill", "steelblue")
					d3.select("#interactivity").remove();
				});
	};
};