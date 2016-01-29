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

function loadAddBill(){
  $('#page-wrapper').empty();
  $('#page-wrapper').load('shtml/addBill.html', populateTenants);
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
    console.log(result)
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
      //insert a final checkbox for deletion
      headerString += '<th>' + '<input type="checkbox" id="checkBoxClient" class="styled">' + '</th>'
      headerString += '</tr>'
    }

    headerString += '</tbody>'
    //console.log(headerString)
    $("#billTable").append(headerString)

};

function loadTenants(){
  $.get( "/functions/viewTenants", insertTableElements)
};

function populateTenants() {
  $.getJSON( "/functions/viewTenants", populateTenantsDropdown)
};

function populateTenantsDropdown(data) {
  for(i=0; i<data.length; i++)
  {
    $("#peopleDropdown").append('<option value="' + data[i].people_email + '">' + data[i].people_name + '</option>')
  }
};

/////additional functionaity
$(document).on('click','#deleteClient',function(e){
  var selected = [];
  $('#billTable input:checked').each(function() {
      // this should be the email
      selected.push($(this).parent().parent().contents()[2].innerText);
  });
  console.log(selected)
});
