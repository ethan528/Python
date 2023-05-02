import {
    launch,
    goto,
    checkPopup,
    evalCode,
    evalSigungu,
    closeAlert,
    getPageLength,
    getData,
} from "./module/crawler.js"

async function main () {
    console.log("start")

    await launch()

    await goto()

    await checkPopup()

    await evalCode("seoul")

    await evalSigungu("songpa_gu")

    await closeAlert()

    await getPageLength()

    await getData()

    console.log("end")
}

main()