let getData
const randomWordData = async  () => {
    let res = await fetch('./data.json')
    if(!res.ok){
        throw new Error
    }
    let data =await res.json()
    return data
}
    getData = await randomWordData()
    console.log(getData.activity[1])