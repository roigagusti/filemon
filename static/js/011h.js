// 0. Càrrega inicial
//$(document).ready(function(){
  //$('#menu-responsive').load('templates/sections/responsive-menu.html');
//});

// 1. Si és webApp
if (window.navigator.userAgent.indexOf('iPhone') != -1) {
    if (window.navigator.standalone == true) {
      $("header").removeClass("hidden");
    }
}

// 2. Fer blur en responsive
function changeBlur(){
    $("div.responsive-blur").hasClass("hidden") ? $("div.responsive-blur").removeClass("hidden") : $("div.responsive-blur").addClass("hidden");
    $("div.menu").hasClass("hidden") ? $("div.menu").removeClass("hidden") : $("div.menu").addClass("hidden");
}

// 3. Activar i desactivar inputs de formulari
function activate(id){
  $(id).removeClass('hidden');
}
function deactivate(id){
  $(id).addClass('hidden');
}
function change(id1,id2){
  if($(id1).hasClass('hidden')){
      activate(id1);
      deactivate(id2);
  }
}

function SPS(){
  if($('#crearDuplicar').hasClass('hidden')){
    $('#crearDuplicar').removeClass('hidden');
  }
  if($('#shortName').hasClass('hidden')){
    $('#shortName').removeClass('hidden');
  }
  if($('#description').hasClass('hidden')){
    $('#description').removeClass('hidden');
  }
  if($('#detailComposition').hasClass('hidden')){
    $('#detailComposition').removeClass('hidden');
  }
  if($('#ipuntComposicio').hasClass('hidden')){
    $('#ipuntComposicio').removeClass('hidden');
  }
  if($('#gralForm').hasClass('hidden')){
    $('#gralForm').removeClass('hidden');
  }
}
function SPSname(value){
    document.getElementById("SPSname").textContent=value;
}


// 4. Sel·leccionar file al clicar Attach. Not in use
$("p#selectFile").click(function(){
    document.getElementById("filedetail").click();
  });