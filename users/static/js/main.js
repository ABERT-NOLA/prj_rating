design = document.getElementById('design').innerHTML
usability = document.getElementById('usability').innerHTML
content = document.getElementById('content').innerHTML

let starPercent = (number) => {
    const percent = `${number * 10}%`
    return percent
}
document.getElementById('star-inner-design').style.width= starPercent(design)
document.getElementById('star-inner-us').style.width = starPercent(usability)
document.getElementById('star-inner-con').style.width = starPercent(content)
console.log(starPercent(design))
