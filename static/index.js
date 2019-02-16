$(function(){
	$('.box-item').click((e)=>{
		$('#' + e.target.id).text('0');
	});
	$('#submit').click((e)=>{
		$('.boxes').css('display', 'grid');
	});
});