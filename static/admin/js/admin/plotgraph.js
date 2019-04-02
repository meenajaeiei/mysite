	var endpoint = '/api/chart/data'
	var defaultData = []
	var labels = [];

	$.ajax({
		method: "GET",
		url: endpoint,
		success: function (data) {
			labels = data.labels
			defaultData = data.default


			var ctx = document.getElementById("fat").getContext('2d');
			var myChart = new Chart(ctx, {
				type: 'scatter',
				data: {
					datasets: [{
						label: labels,
						data: defaultData,
						backgroundColor: ['red'],
						pointBorderWidth: 2, pointRadius: 2,
						pointHoverBorderWidth: 2, pointHoverRadius: 2,
					}]
				}
			},

			options = {
				scales: {
					yAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
						}
					}]
				}
			})

			var ctx2 = document.getElementById("bmi").getContext('2d');
			var myChart2 = new Chart(ctx2, {
				type: 'scatter',
				data: {
					datasets: [{
						label: labels,
						data: defaultData,
						backgroundColor: ['red'],
						pointBorderWidth: 2, pointRadius: 2,
						pointHoverBorderWidth: 2, pointHoverRadius: 2,
					}]
				}
			},

			options = {
				scales: {
					yAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
						}
					}]
				}
			})

			var ctx3 = document.getElementById("muscle").getContext('2d');
			var myChart3 = new Chart(ctx2, {
				type: 'scatter',
				data: {
					datasets: [{
						label: labels,
						data: defaultData,
						backgroundColor: ['red'],
						pointBorderWidth: 2, pointRadius: 2,
						pointHoverBorderWidth: 2, pointHoverRadius: 2,
					}]
				}
			},

			options = {
				scales: {
					yAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
						}
					}]
				}
			})




		}
	})


	function test(){
		window.defaultData = []
		console.log(window.defaultData)
	}