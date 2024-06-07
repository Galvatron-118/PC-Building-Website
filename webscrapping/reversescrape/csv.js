onload = fetch("./partsdemo.csv").then(res => {
    return res.text()
}).then(data => {
    let result = data.split(/\r?\n|\r/).map(e => {
        return e.split(";")
    })
    result.forEach(e => {
        let m = e.map(e => {
           return `<td>${e}</td>`; 
        }).join("")
        console.log(m);
        let ce = document.createElement("tr");
        ce.innerHTML = m;
        if (ce.innerText != "") {
            document.querySelector("tr").appendChild(ce);
        }

    })
})