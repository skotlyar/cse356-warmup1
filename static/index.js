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
			console.log('run 3');
			$.post('http://localhost:5000/ttt/play', $.param(board, true), (data) => {
				/*optional stuff to do after success */
				if(data.winner != ''){
					switch(data.winner){
						case 'X':
						case 'O':
							$('#winner').text(data.winner + 'is the winner!');
							break;
						case ' ':
							$('#winner').text('Tie!');
					}
				}
				for(let i = 0; i < data.grid.length; i++){
					$('#' + i).text(data.grid[i]);
					board.grid[i] = data.grid[i];
				}
			});
			// var request = $.ajax({
			// 	url: "http://130.245.170.88/ttt/play",
			// 	type: "POST",
			// 	data: grid
			// });

			// request.done(function(grid) {
			// 	console.log("Success");

			// 	// Take the returned json and iterate through the elements and update the UI
			// 	board[msg] = 'O';
			// 	$('#'+msg).text('O');
			// });

			// request.fail(function(jqXHR, textStatus) {
			// 	alert( "Request failed: " + textStatus );
			// });
		}
	});


	$('#submit').click((e)=>{
		$('.boxes').css('display', 'grid');
	});
});