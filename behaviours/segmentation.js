
function segment(dataImage,document,ctx,prompt){
    console.log("send image reached");
    var headers = {"Content-Type": "image/jpeg"} ;
    var prompt_pathimage = {
        "prompt" : prompt,
        "prompt_label" : [1],
        "img_path" : "./images/temp_image.jpg"
        }
    const formData = new FormData();

    formData.append("image", dataImage);
    formData.append("prompt", prompt_pathimage['prompt'] );
    formData.append("prompt_label", prompt_pathimage['prompt_label']) ;

    // call machine learning model through rest api
    fetch( 'http://127.0.0.1:8000/upload_image/', {
            method: "POST",
            mode: 'cors',
            headers : {} ,
            body : formData
        })
        .then(response => response.blob())
        .then(Imdata => {
            draw_mask(Imdata,ctx);
        })
        .catch(error => {
            document.getElementById('messages').value = error ;
        });
}

function draw_mask(Imagedata,ctx){
    var mask = Imagedata ;
    const image = new Image();
    image.src = URL.createObjectURL(mask);
    image.onload = function() {
        ctx.drawImage(image, 0, 0);
    };
    document.getElementById('messages').value = "loaded" ;
}