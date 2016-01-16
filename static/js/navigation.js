function loadDash(){
  $('#page-wrapper').empty();
  $('#page-wrapper').load('shtml/dash.html');
}

function loadBill(){
  $('#page-wrapper').empty();
  $('#page-wrapper').load('shtml/bill.html');
}

function loadAddTenant(){
  $('#page-wrapper').empty();
  $('#page-wrapper').load('shtml/addTenant.html');
}

function loadViewTenant(){
  $('#page-wrapper').empty();
  $('#page-wrapper').load('shtml/viewTenant.html',loadTenants);
}

///****       **      **      **//

// user to remap names
function keyMapper(key)
{
  if(key == 'people_name')
  {
    return 'Client Name'
  }

  if(key == 'people_email')
  {
    return 'Client Email'
  }
}

function insertTableElements(data)
{
    var result = $.parseJSON( data )
    //fix fix fix check for none case
    var headerString = "<thead class='thead-default'> <tr> <th>#</th>"

    for (key in result[0])
    {
      headerString += '<th>' + keyMapper(key) + '</th>'
    }
    headerString +=" </tr>  </thead> "
    //insert in the data elements
    headerString += '<tbody>'

    for(i=0; i < result.length ;i++)
    {
      headerString += '<tr>  <th scope="row">'+i+'</th>'
      for (key in result[i])
      {
        headerString += '<th>' + result[i][key] + '</th>'
      }
      headerString += '</tr>'
    }

    headerString += '</tbody>'
    //console.log(headerString)
    $("#billTable").append(headerString)
};

function loadTenants(){
  $.get( "/functions/viewTenants", insertTableElements)
};
