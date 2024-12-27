const scrollBtn = document.querySelector(".btnToTop")
const rootEl = document.documentElement
document.addEventListener("scroll",showBtn)
scrollBtn.addEventListener("click",scrollToTop)

function showBtn(){
     const scrollTotal = rootEl.scrollHeight - rootEl.clientHeight
     if(rootEl.scrollTop/scrollTotal > 0.49){
        scrollBtn.classList.add("show-btnToTop")
     }else{
        scrollBtn.classList.remove("show-btnToTop")
     }
}

function scrollToTop(){
    rootEl.scrollTo({
        top:0,
        behavior:"smooth"
    })
}