$('#search_form').submit(function(e) {
    $.post('/students/student_search/', $(this).serialize(), function(data) {
        $('.search-result').html(data);
    });
    e.preventDefault();
});