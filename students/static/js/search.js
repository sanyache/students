var searchStudent = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('q'),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  prefetch: '/students/search/?q=%QUERY',
  remote: {
    url: '/students/search/?q=%QUERY',
    wildcard: '%QUERY'
  }
});

$('#search_student .typeahead').typeahead({
  //hint:true,
  //highlight: true,
  //autoselect: true,
  minLength:1,
  limit: 10,
}, {
  name: 'searchStudent',
  displayKey: 'q',
  source: searchStudent,
  templates:{
    empty: 'Не має в базі',
  }
});