const textArea = document.getElementById('textarea');
const run = document.getElementById('run');
const code = `print('hello world)`

var myCodeMirror = CodeMirror.fromTextArea(textArea, {
    value: 'print(\'hello world\')',
    lineNumbers: true,
    theme: 'dracula',
    keyMap: 'sublime',
    mode: 'python',
    autoCorrect:true,
    autoCloseBrackets: true,
    extraKeys: {"Ctrl-Space": "autocomplete"},
});

myCodeMirror.on('change', () => {
    textArea.value=myCodeMirror.getValue();
    // console.log(myCodeMirror.getValue());
});

//Timer
var timeLeft = 30*60;
var elem = document.getElementById('time');
var timerId = setInterval(countdown, 1000);

function countdown() {
    if (timeLeft == -1) {
        clearTimeout(timerId);
        doSomething();
    }
    else {
        elem.innerHTML = `${(timeLeft%60)}`;
        timeLeft--;
    }
}
