var board = {'grid':[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']};
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
		if($('#' + e.target.id).text() == ' '){
			$('#' + e.target.id).text('X');
			board.grid[e.target.id] = 'X';
			var grid = JSON.stringify(board['grid']);
			console.log(grid);
			console.log('run 4');
			// $.post('http://localhost:5000/ttt/play', $.param(board, true), (data) => {
			$.post('http://localhost:5000/ttt/play', $.param({'move':e.target.id}, true), (data) => {
				sleep(500).then(() => {
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
					}
				});
			});
		}
	});


	$('#submit').click((e)=>{
		$('.boxes').css('display', 'grid');
	});
});
