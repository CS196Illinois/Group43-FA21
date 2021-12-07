let wrongW = "the";
const text = document.querySelectorAll('h1, h2, h3, h4, h5, p, li, td, caption, span, a,div')
for (let i=0; i < text.length; i++) {
    console.log(text[i].innerHTML);
    console.log(text[i].innerHTML.includes(wrongW));
    if (text[i].innerHTML.includes(wrongW)) {
        text[i].innerHTML = "\n<span class='heise' title=\"Big brother is watching you\">" + text[i].innerHTML + "</span>";
    }
}
