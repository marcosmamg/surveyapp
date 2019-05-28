$.getJSON('/survey/userresponse/summary' ,function(data) {
	var categories = [];
	jQuery.each(data, function(i, val) {
		categories.push(val.question_text);
	});

	var correct_responses = [];
	jQuery.each(data, function(i, val) {
		correct_responses.push(val.total_correct);
	});

	var incorrect_responses = [];
	jQuery.each(data, function(i, val) {
		incorrect_responses.push(val.total_incorrect);
	});
	console.log(data);
	Highcharts.chart('container', {
		chart: {
			type: 'column'
		},
		title: {
			text: 'Survey App Summary Responses'
		},
		subtitle: {
			text: 'Source: Django Survey App by Marcos Moreno'
		},
		xAxis: {
			categories,
			
			crosshair: true
		},
		yAxis: {
			min: 0,
			title: {
				text: 'Correct and Incorrect responses'
			}
		},
		tooltip: {
			headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
			pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
				'<td style="padding:0"><b>{point.y:.1f}</b></td></tr>',
			footerFormat: '</table>',
			shared: true,
			useHTML: true
		},
		plotOptions: {
			column: {
				pointPadding: 0.2,
				borderWidth: 0
			}
		},
		series : [
			 {
				name: 'Correct responses',
				data: correct_responses 
					

			},

			{
				name: 'Incorrect responses',
				data: incorrect_responses

			},
	
	]
	});
});