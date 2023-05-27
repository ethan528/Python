import puppeteer from "puppeteer-core"
import os from "os"

const winUrl = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
const currentOs = os.type()
const launchConfig = {
    headless: false,
    dafultViewport: null,
    ingnoreDefaultArgs: ["--disable-extensions"],
    args: ["--no-sandvbox", "--disable-setuid-sandbox",
    "--disable-notifications","--disable-extensions"],
    executablePath: currentOs == "Darwin" ? macUrl:
    winUrl
}

let browser
let page
let pageNum

const launch = async () => {
    browser = await puppeteer.launch(launchConfig)
    const pages = await browser.pages()
    page = pages[0]
}

const goto = async () => {
    await page.goto("https://www.pharm114.or.kr/main.asp")
}

const checkPopup = async function () {
    const pages = await browser.pages()
    console.log(pages.length, "닫기전")
    await pages.at(-1).close()
    console.log(pages.length, "닫기후")
}

const evalCode = async sido => {
    await page.evaluate((sido) => {
        const selector = `#continents > li.${sido} > a`
        document.querySelector(selector).click()
    }, sido)
}

const evalSigungu = async sigungu => {
    const selector = `#continents > li.${sigungu} > a`
    await page.waitForSelector(selector)

    await page.evaluate((selector) => {
        document.querySelector(selector).click()
    }, selector)
}

const closeAlert = async () => {
    await page.on("dialog", async function(dialog){
        await dialog.accept()
    })
}

const getPageLength = async () => {
    const pagingSelector = `body > table:nth-child(2) > tbody > tr > td:nth-child(1) > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(5) > td > table:nth-child(5) > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(3)")`

    await page.waitForSelector(pagingSelector)

    pageNum = await page.evaluate((pagingSelector) => {
        const pageLength = document.querySelector(pagingSelector).children.length
        return pageLength
    }, pagingSelector)

    console.log("pageNum:", pageNum)
}

const getData = async => {
    var trArr = Array.from(document.querySelectorAll("#printZone > table:nth-child(2) > tbody tr"))

    var data = trArr.map(el => {
        consloe.log(el)
        debugger
        return {
            addr: el.querySelector(".class_addr")?.innerText,
            tel: el.querySelectorAll("td")[3]?.innerText
        }
    })
    console.log(data)
}

export {
    launch,
    goto,
    checkPopup,
    evalCode,
    evalSigungu,
    closeAlert,
    getPageLength,
    getData
}