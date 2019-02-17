var board = {'grid':[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 'model':[0,0,0,0,0,0,0,0,0]};
// var boardModel = [0,0,0,0,0,0,0,0,0];
const sleep = (milliseconds) => {
  return new Promise(resolve => setTimeout(resolve, milliseconds))
};
var gameover = false;



$(function(){
	console.log(board);
	$('.box-item').click((e)=>{
		if(gameover){
			return;
		}
		if($('#' + e.target.id).text() == ' ')
		{
			$('#' + e.target.id).text('X');

			board.grid[e.target.id] = 'X';
			board.model[e.target.id] = 1;
			var grid = JSON.stringify(board['grid']);
			console.log(grid);
			console.log('run 3');
			$.post('http://130.245.170.88/ttt/play', $.param(board, true), (data) => {
				/*optional stuff to do after success */
				sleep(500).then(() => {
					//TODO don't allow user to click open boxes when game is over
					if(data.winner != ''){
						switch(data.winner){
							case 'X':
							case 'O':
								$('#winner').text(data.winner + ' is the winner!');
								gameover = true;
								break;
							case ' ':
								$('#winner').text('Tie!');
								gameover = true;
						}
					}
					for(let i = 0; i < data.grid.length; i++){
						$('#' + i).text(data.grid[i]);
						board.grid[i] = data.grid[i];
						board.model[i] = data.model[i];
					}
				});
			});
		}
	});


	$('#submit').click((e)=>{
		$('.boxes').css('display', 'grid');
	});
});
