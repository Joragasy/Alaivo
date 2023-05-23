
document.addEventListener('DOMContentLoaded', function() {
  var download_bouton = document.getElementById('download');
  var capture_bouton = document.getElementById('capture');

  var canvas_capture = document.getElementById("captured_images");
  var ctx = canvas_capture.getContext("2d");

  // var prompt_mark_canvas = document.getElementById("prompt_mark");
  // var ctx_prompt = prompt_mark_canvas.getContext("2d");

  // var mask_canvas = document.getElementById("mask");
  // var ctx_mask = mask_canvas.getContext("2d");

  var remove_prompt = document.getElementById("removeprompt");

  var extract_bouton = document.getElementById("extract");
  var prompt = [] ;

  var extract = 0 ;
  capture_bouton.addEventListener('click', function() {
    console.log("capture bouton clicked") ;
    document.getElementById('download').style.color = "#ff0000" ;
    capture(ctx);
    api_connexion_test(document);
    prompt = [] ;
  });

  remove_prompt.addEventListener('click' , function() {
    prompt = [] ;
    ctx_prompt.clearRect(0, 0, prompt_mark_canvas.width, prompt_mark_canvas.height);
    //ctx_prompt.globalAlpha = 0;
    //ctx_prompt.canvas.hidden = true;
  });

  download_bouton.addEventListener('click', function(){
    const link = document.createElement("a");
    link.href = canvas_capture.toDataURL();
    link.download = "canvas_image.png";
    link.click();
  });
  
  canvas_capture.addEventListener('click',function(e){
    console.log("canvas clicked");
    let coords = [] ;
    coords= getPosition(e, canvas_capture); // get x,y coords
    //drawCoordinates(coords[0],coords[1],document,ctx);
    prompt.push([coords[0],coords[1]]);
  });

  extract_bouton.addEventListener('click', function(e){
     document.getElementById('messages').value = "Extraction ...";
     canvas_capture.toBlob(function(blobImage) {
         segment(blobImage,document,ctx,prompt);
     }, "image/jpeg");
     
  });

});