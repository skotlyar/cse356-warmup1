
$(function(){
	$('#submit').click((e)=>{
		var user = $('#user').text();
		var pass = $('#pass').text();

		var json = {}
		json.username = user
		json.password = pass
		var stringJson = JSON.stringify(json);

		$.post('http://localhost:5000/login', stringJson, (data, status, xhr) => {
			var cookie = Cookies.get('username');
			console.log("hello");
		});
	});
});