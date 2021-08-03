function onEditButtonClick(tagToInsert) {
    const textArea = document.getElementById("text");
    const start = textArea.selectionStart;
    const finish = textArea.selectionEnd;
    if (start && finish) {
        const wordToWrap = textArea.value.substring(start, finish);
        const wrappedWord = wrapStringIntoTheTag(tagToInsert, wordToWrap);
        textArea.value = textArea.value.substring(0, start) + wrappedWord + textArea.value.substring(finish);
    }
}

function wrapStringIntoTheTag(tag, str) {
    return `<${tag}>${str}</${tag}>`
}
