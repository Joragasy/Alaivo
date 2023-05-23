
function capture(ctx){
    chrome.tabs.captureVisibleTab((screenshotUrl) => {
        let newImage = new Image();
        newImage.src = screenshotUrl ;
        newImage.onload = () => {
            ctx.drawImage(newImage, 0, 0);
        }
    });
}