function listAttachments(caller) {
   $.get( "functions/attachments", function( data ) {
     var obj = jQuery.parseJSON( data );
     var element = $( caller).parent()
     billTemplateStart(element)
     obj.forEach(function(entry) {
          billTemplateMiddle(element, entry)
      });
      billTemplateEnd(element)
   })
}

function billTemplateStart(element){
  element.empty()
  element.append('<ul class="list-group')
}
function billTemplateEnd(element){
  element.append('</ul>')
}
function billTemplateMiddle(element,entry)
{
  element.append('<li class="list-group-item">' + entry +'</li>')
}
