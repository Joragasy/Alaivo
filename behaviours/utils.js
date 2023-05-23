
function api_connexion_test(document){
    var headers = {} ;
    fetch('http://127.0.0.1:8000/',{
            method : "GET",
            mode: 'cors',
            headers: headers
        })
        .then((response) => {
            if (!response.ok) {
                throw new Error(response.error)
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('messages').value = data.message;
            prompt = [] ;
        })
        .catch(function(error) {
            document.getElementById('messages').value = error;
         });
}

function drawCoordinates(x,y,document,ctx_prompt){	
    console.log(x,y);
    document.getElementById('messages').value = x + "  " + y ;
    var pointSize = 4 ;
    ctx_prompt.fillStyle = "red"; 
    ctx_prompt.beginPath();
    ctx_prompt.arc(x, y, pointSize, 0, Math.PI * 2, true);
    ctx_prompt.stroke();
}

function getPosition(event, canvas){
    var rect = canvas.getBoundingClientRect();
    var x = event.clientX - rect.left;
    var y = event.clientY - rect.top;
    return [x , y] ;
}

function getShape(arr) {
    if (!Array.isArray(arr)) {
        // Not an array
        return [];
    }
    const shape = [];
    let current = arr;
    while (Array.isArray(current)) {
        shape.push(current.length);
        current = current[0];
    }
    return shape;
}