const html5Qrcode = new Html5Qrcode('reader');
const qrCodeSuccessCallback = (decodedText, decodedResult) => {
    if (decodedText) {
        document.getElementById("qr").value = decodedText;
        html5Qrcode.stop();
        document.qrform.submit();
    }
};

const config = { fps: 10, qrbox: { width: 250, height: 250 } };
html5Qrcode.start({ facingMode: 'environment' }, config, qrCodeSuccessCallback);
