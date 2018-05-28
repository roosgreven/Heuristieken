
/* 
This function sets variables for width and height, makes scalers
	of the bar chart. Loads the data and converts the data into 
	a more workable set.
	Args:
		titleName: name of the title of the graph 
		numberOfHouses: number of houses in the neighbourhood
*/
function createPlot(titleName, numberOfHouses) {

	numberOfHouses = parseInt(numberOfHouses)

	// clear all svgs
	d3.selectAll(".chart").remove();

	d3.select("#chart").append("svg").attr("class", "chart")

	// set margins, width and height
	var margin = {top: 50, right: 200, bottom: 170, left: 80},
		width = 800 - margin.left - margin.right,
		height = 500 - margin.top - margin.bottom;

	// attribute width and height to chart
	var chart = d3.select(".chart")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
		// append g to set the chart at the right spot
		.append("g")
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
	
	// scale the name values on range
	var x = d3.scale.ordinal()
		.rangeRoundBands([0, width], .1);
	
	// scale the datapoints on range 
	var y = d3.scale.linear()
		.range([height, 0]);

	// set color range
	var color = d3.scale.ordinal()
	.range(["blue", "red", "orange", "green"]);

	// variable to draw the x axis below the bars, correctly scaled
	var xAxis = d3.svg.axis()
		.scale(x)
		.orient("bottom");

	// variable to draw the y axis on the left side, correctly scaled
	var yAxis = d3.svg.axis()
		.scale(y)
		.orient("left");

	// load the data 
	d3.json(String(numberOfHouses) + "water.json", function(error, data) {

		// alert if there is an error and return to stop the script
		if (error) {
			alert("Data file not found or not valid: " + error);
			return;
		};

		// variables for start en end of chart
		var startChart;
		var endChart;

		// make start and end dependent on number of houses
		if (numberOfHouses == 20) {

			startChart = 7500000;

			endChart = 11000000;
		}

		else if (numberOfHouses == 40) {

			startChart = 15000000;
			endChart = 18000000;
		}

		else {

			startChart = 22500000;
			endChart = 25000000;		
		}

		// calculate range of values
		var valueRange = endChart - startChart;

		var steps = 20

		// calculate ranges of charts
		oneStep = valueRange / steps;

		var valueRanges = []

		// loop over all ranges
		for (let i = 0; i < steps; i++) {

			// add ranges to array with all ranges of groups
			valueRanges.push(String((startChart + i * oneStep) / 1000000) + "-" 
				+ String((startChart + (i + 1) * oneStep) / 1000000))
		}

		// object to save values
		const counts = {};

		// arrays to save values
		thisArray = [];
		dataArray = [];

		// loop over all sorts
		Object.keys(data).forEach(function(key) {

			// object for each sort in array
			counts[key] = {};

			// for each value of sort
			data[key].forEach(function(d) {

				// decide what group value will be in
				let group = Math.floor((d - startChart) / oneStep);

				// add each group to object
				if (!counts[key][valueRanges[parseInt(group)]]) {
					counts[key][valueRanges[parseInt(group)]] = 0;
				}

				// count all values in that group
				counts[key][valueRanges[parseInt(group)]] ++;				
			});
			
			// loop over all values in sort
			Object.keys(counts[key]).forEach(function(d) {

				// convert frequencies to percentages
				counts[key][d] = parseFloat((counts[key][d] / 50).toFixed(1));

				// add range and percentage as object to an array
				thisArray.push({"range": d, "percentage": counts[key][d]});
			
			});

			// add array with ranges and percentages as object to general array
			dataArray.push({"sort": key, "values": thisArray})

			// empty array
			thisArray = [];
			
		});

		// add the title of the graph
		document.getElementById("graphTitle").innerHTML = "<h2><b>" + titleName + "</b>";

		// call the function to draw the bar chart
		drawBarChart(dataArray, valueRanges);
	});

	/* 
	This function sorts data, completes the scalers draws x and y axis 
	of the bar chart with the right text and draws bars. 
	Args:
		data: list of objects. Each object contains a name and a value. 
		valueRanges: array with all ranges of values

	*/
	function drawBarChart(data, valueRanges) {

		//console.log(data)

		// set domains of x and y scalers
		x.domain(valueRanges);
		
		y.domain([ 
			d3.min(data, function (c) { 
				return d3.min(c.values, function (d) { return d.percentage; });
			}),
			d3.max(data, function (c) { 
				return d3.max(c.values, function (d) { return d.percentage; });
			})
		]);

		// set domain of color scaler
		color.domain(data.map(function(d) { return d.sort}))

		// draw x axis with value ranges and tick marks
		chart.append("g")
			.attr("class", "x axis")
			.attr("transform", "translate(0," + height + ")")
			.call(xAxis)
			.selectAll("text")
				.style("text-anchor", "end")
				.attr("dx", "-.8em")
				.attr("dy", ".5em")
				.attr("transform", function(d) { return "rotate(-65)" });

		// add name for the x axis
		chart.append("text")
			.attr("x", width / 2.5)
			.attr("y", height + margin.bottom / 1.5)
			.style("font", "18px sans-serif")
			.text("Value in millions");
			
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
				.text("Frequency in %");
		
		// get the sorts
		const sorts = data.map(x => x.sort);
		console.log(data);


		// draw the bars
		d3.map(data, function(data) {
			console.log(data);
			chart.selectAll(".bar" + sorts.indexOf(data.sort))
			.data(data.values)
			.enter().append("rect")
				.attr("class", "bar" + data.sort)
				.attr("y", function(d) { return y(d.percentage)})
				.attr("x", function(d) { 
					return x(d.range) + x.rangeBand() / sorts.length * sorts.indexOf(data.sort) - (width / 20 / 2)
				})
				.attr("width", x.rangeBand() / sorts.length)
				.attr("height", function(d) { return height - y(d.percentage) })
				.style("fill", color(data.sort))
		});

	// draw legend
	drawLegend(data, sorts)
	};



	/*
	This function creates a legend. It sets it at right position 
	and scales. 
	Args:
		data: list of objects
		sorts: array of sorts 
	*/

	drawLegend = function(data, sorts) {

		// set sizes for legend
		var legendRectSize  = 15;
		var legendSpacing = 6;
		
		// ordinal scaler to set colors
		var legendColor = d3.scale.ordinal()
		.domain(sorts)
		.range(["blue", "red", "orange", "green"]);

		// add an svg for the legend
		var theLegend = chart.append("svg")
			.attr("width", width + 250)
			.attr("height", height)
			.append("g")
				.attr("transform", "translate(" + width + ", 50)");

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
				return "translate(" + horz + "," + vert + ")"; });

		// add rectangles for color
		legend.append("rect")
			.attr("width", legendRectSize)
			.attr("height", legendRectSize)
			.style("fill", legendColor)
			.style("stroke", legendColor);

		// add the text per block
		legend.append("text")
			.attr("x", legendRectSize + legendSpacing)
			.attr("y", legendRectSize - legendSpacing)
			.style("font", "sans-serif")
			.text(function(d) { return d; });
	};
};