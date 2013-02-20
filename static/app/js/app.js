
$('input.search-query').keydown(function(event) {
    if (event.keyCode == 13) {
	var query = $('input.search-query').val();
	$('#container').load(
	    "/search/?ajax&query=" + encodeURIComponent(query),
	    function() {
		$("#container").find("hr").first().
		    before("<h1>search result for " + query + "</h1>");
	    }
	);
	return false;
    }
});
