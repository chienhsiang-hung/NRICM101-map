# 臺灣清冠一號地圖 Taiwan NRICM101 Map

![](https://img.shields.io/github/license/chienhsiang-hung/NRICM101-map)
![](https://img.shields.io/github/languages/count/chienhsiang-hung/NRICM101-map)
![](https://img.shields.io/github/languages/top/chienhsiang-hung/NRICM101-map)
![](https://img.shields.io/website?url=https%3A%2F%2Fchienhsiang-hung.github.io%2FNRICM101-map%2F)
![](https://img.shields.io/github/deployments/chienhsiang-hung/NRICM101-map/github-pages)
![](https://img.shields.io/github/deployments/chienhsiang-hung/NRICM101-map/Production)
![](https://img.shields.io/github/languages/code-size/chienhsiang-hung/NRICM101-map)
![](https://img.shields.io/github/repo-size/chienhsiang-hung/NRICM101-map)
![](https://img.shields.io/github/v/release/chienhsiang-hung/NRICM101-map?include_prereleases)
![](https://img.shields.io/github/discussions/chienhsiang-hung/NRICM101-map)
![](https://img.shields.io/github/checks-status/chienhsiang-hung/NRICM101-map/main)

> 家人同事染疫 與 網友確診搜索公費清冠一號並能視訊看診之中醫上困難
>
> 決定製作清冠地圖 供大家免費查閱


**[臺灣清冠一號地圖 Taiwan NRICM101 Map](https://chienhsiang-hung.github.io/NRICM101-map/)**

**初次使用因資料量龐大約需等待4~6秒載入診所資訊 ( 資料庫每20分鐘更新一次 )*


利用國家中醫藥研究所與中醫師公會全國聯合會合作建置公費清冠一號醫療資訊平台 - **公費清冠一號 (供全台民眾查詢)**，供中醫視訊診療需求之COVID-19確診病患、家屬透過 [臺灣清冠一號地圖 Taiwan NRICM101 Map](https://chienhsiang-hung.github.io/NRICM101-map/) ，查詢提供公費清冠ㄧ號之中醫醫療院所名單及當日公費清冠ㄧ號庫存量，以利民眾獲得所需醫療資訊。

如有任何使用建議歡迎 [到此提出](https://github.com/chienhsiang-hung/NRICM101-map/issues) 謝謝


## 使用API獲取清冠地圖
![image](https://user-images.githubusercontent.com/77676044/185618824-43733399-98c7-4ecf-b56d-3e40b6cb4fac.png)
*(update frequency - 20min)*
```
GET https://nricm101-map.chienhsiang-hung.eu.org/api/get
Return .json
```
[清冠地圖API](https://nricm101-map.chienhsiang-hung.eu.org/api/get) 開放給民眾免費使用

資料量大 (全台中醫資料) [清冠地圖API](https://nricm101-map.chienhsiang-hung.eu.org/api/get) 平均讀取時間為4~6秒。已開放`'Access-Control-Allow-Origin'` to `'*'` ，歡迎其他前端接取免費測試。唯因系統只有一人維護還請大家斟酌使用，不便之處敬請見諒😅


## 待新增Features
- 搜尋地址 (When Device Local Info Failed)
- 搜尋診所
- 公費圖層 (Filter)
- TBD


## 介紹文章
[家人染疫後 我做了一個清冠地圖 - 洪健翔 Hung, Chien-hsiang - Medium](https://hungchienhsiang.medium.com/%E5%AE%B6%E4%BA%BA%E6%9F%93%E7%96%AB%E5%BE%8C-%E6%88%91%E5%81%9A%E4%BA%86%E4%B8%80%E5%80%8B%E6%B8%85%E5%86%A0%E5%9C%B0%E5%9C%96-584350009dee)


## #Resources
[臺灣清冠一號地圖 Taiwan NRICM101 Map](https://chienhsiang-hung.github.io/NRICM101-map/) 搭配資料來源 [「清冠一號動態表」](https://docs.google.com/spreadsheets/d/e/2PACX-1vQjf_HNeEZKM-XJX-q5v4cfNrB3kcv4gOT8kFbV9rurfoX_H5Qv9112Pv0PgYNFSzbReyNlQkLrJib3/pubhtml)

- [Leaflet - a JavaScript library for interactive maps](https://leafletjs.com/)

- [OpenStreetMap](https://www.openstreetmap.org/copyright)

- [Copied icon PNG and SVG Vector](https://uxwing.com/copied-icon/)

- [Instruction icon PNG and SVG Vector](https://uxwing.com/instruction-icon/)

- [Modal · Bootstrap](https://getbootstrap.com/docs/4.0/components/modal/#via-data-attributes)

網站聲明請參閱[免責聲明| 臺灣清冠一號地圖 Taiwan NRICM101 Map](https://chienhsiang-hung.github.io/NRICM101-map/immunity.html)


## 一杯咖啡支持更新
感謝有您的支持讓地圖能夠穩定持續更新。

[Chien-Hsiang Hung (buymeacoffee.com)](https://www.buymeacoffee.com/abcdefg2981)

[Buy Chien-Hsiang Hung a Coffee. ko-fi.com/chienhsianghung - Ko-fi ❤️](https://ko-fi.com/chienhsianghung)
