var board = {'grid':[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']};



$(function(){
	console.log(board);
	$('.box-item').click((e)=>{
		if($('#' + e.target.id).text() == ' ')
		{
			$('#' + e.target.id).text('X');

			board['grid'][e.target.id] = 'X';
			var grid = JSON.stringify(board['grid']);
			console.log(grid);
			
			var request = $.ajax({
				url: "http://localhost:5000/ttt/play",
				type: "POST",
				data: grid
			});

			request.done(function(grid) {
				console.log("Success");

				// Take the returned json and iterate through the elements and update the UI
				board[msg] = 'O';
				$('#'+msg).text('O');
			});

			request.fail(function(jqXHR, textStatus) {
				alert( "Request failed: " + textStatus );
			});
		}
	});


	$('#submit').click((e)=>{
		$('.boxes').css('display', 'grid');
	});
});