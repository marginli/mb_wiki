---
title: PAM-α1 多巴胺神經元（PAM-α1）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# PAM-α1 多巴胺神經元（PAM-α1）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ2、α1）；細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PAM、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PAM 群多傳遞獎賞，PPL1 群（Handler 2019 寫作 PPL）多傳遞懲罰。
- **MBON**：蕈狀體輸出神經元，接收 KC 的訊號、推動果蠅靠近或走開；學習改變的是 KC→MBON 突觸的強弱。
- **CS+／CS−、順向／逆向**：訓練時配了糖、電擊或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。順向配對＝氣味先、多巴胺後；逆向配對＝多巴胺先、氣味後。
- **PI（表現指數）、LI（學習指數）**：行為分數。一群果蠅在兩種氣味間選擇，換算成一個數；多數篇落在 −1 到 +1（Hige 2015 的刻度不同），0＝沒有偏好，正負號的意思各篇不同（見 [[c-performance-index]]）。
- **消退、再鞏固**：學會後再聞 CS+ 卻沒有糖或電擊，學到的反應減弱，叫消退（[[c-memory-extinction]]）；記憶被叫出來後暫時變得不穩定、再重新存好，叫再鞏固（[[c-memory-consolidation]]）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半（AD 與 DBD），兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型寫「X/+」表示只帶一個品系的對照組。
- **活化與阻斷工具**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；P2X2 遇到 ATP 讓神經元放電（[[e-p2x2]]）；shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]），全程維持低溫的「允許溫度對照」用來排除品系本身的效果。
- **讀數與製備**：ΔF/F0＝螢光相對刺激前基線的變化比例（0.5＝亮了 50%），以遇鈣變亮的 GCaMP 量神經元活動（[[e-gcamp]]）；離體＝把腦取出泡在養液裡做實驗（[[c-ex-vivo-explant]]），活體＝活果蠅固定後打開頭殼看。
- **舊名與新名**：Aso 2014a（[[s-aso-2014-mb-architecture]]）以前，蕈狀體的細胞型多用 Tanaka 2008 的舊名（MB-MP1、MB-V2α 等），同一顆細胞在不同論文裡名字不同；Aso 2014a 改以所在區室命名，並在表 1 給出新舊名對照。
- **二階制約**：先讓氣味 S1 預告糖，再讓新氣味 S2 只配 S1、不給糖，果蠅也會偏好 S2；教學訊號來自已存在的記憶（[[c-second-order-conditioning]]）。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「text.txt 第 N 行」＝本庫保存的論文全文文字檔的行號；「該頁」指表格同一列的來源頁。

## 是什麼

**PAM-α1 是 PAM 群（多傳遞獎賞）中的一型多巴胺神經元（DAN），把多巴胺送進蕈狀體 α 葉最靠近根部的 α1 區室。** 名字前段 PAM 是細胞群（以細胞體位置命名），後段 α1 是它支配的區室（見 [[c-mb-compartment]]）。同一格的輸出神經元是 [[e-mbon-alpha1]]；Ichinose 2015 發現 MBON-α1 的末梢回到 PAM-α1 的樹突旁，構成一個迴圈（見 [[t-mbon-dan-feedback]]）。本庫用它做實驗的三篇（Ichinose 2015、Aso 2016、Yamada 2023），結論都指向「較慢、較穩的獎賞記憶」。名稱與形態的原始出處是 Aso 2014a：表 1 記每半腦 **6 顆以上**，舊名寫「subset of MB-MVP1, MB-VP1」，也就是它在舊命名裡只是 MB-MVP1 這群細胞的一部分（作者註明對照是「最可能的對應」）。Yamada 2023 圖 2A 寫 MB043C 每半腦標到 5 顆、hemibrain 電顯資料中這一型共 7 顆（※ 推論：依該篇圖說對「5／7」的解釋）。Ichinose 2015 沒有給細胞數（該來源頁搜尋原文後確認）。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 用途 |
|---|---|---|
| MB043B、MB299B（split-GAL4） | Aso 2014a 表 1 | 表 1 列為這一型的品系 |
| MB299B（split-GAL4） | Ichinose 2015（引 Aso 2014a、Yamagata 2015） | 阻斷（shi）、降低 NMDA 受體（RNAi） |
| R72D01-LexA | Ichinose 2015 | 與 MBON-α1 雙標記、GRASP 解剖 |
| MB043C（split-GAL4） | Aso 2016；Yamada 2023 | 驅動 CsChrimson，以光代替糖；Yamada 另以它表現 TNT 阻斷。**與表 1 的 MB043B 是同一對增強子、AD 插在不同位置的兩個品系，不能當成同一個品系引用**（Aso 2014a） |
| MB043-split-LexA | Yamada 2023（新做） | 只在它表現 ChrimsonR，用於電生理實驗 |
| R58E02-GAL4／-LexA | Aso 2016、Felsenberg 2017 | 涵蓋它在內的大範圍 PAM（見 [[e-r58e02]]） |

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-aso-2014-mb-architecture]] | 命名與形態的原始出處（表 1、圖 14O） | 每半腦 6 顆以上；表 1 品系 MB043B、MB299B；末梢略超出 [[e-mbon-alpha1]] 樹突的範圍，延伸到柄的遠端（「DAN 與 MBON 完全對齊」的例外）。PA-GFP 追蹤所用的 NSyb-QF 在它表現很低，所以 split-GAL4 有沒有把它標齊，該篇無法判斷 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 訓練時、訓練後 1 小時、測試時分別以 shi 阻斷；在 PAM-α1 降低 NMDA 受體次單元 dNR-1 或 dNR-2 | 訓練時阻斷：24 h 記憶剩約 18%，5 分鐘記憶不顯著；訓練後立刻阻斷 1 h 也傷 24 h 記憶，22 h 後阻斷不傷；測試時阻斷不顯著（n 小）；降低 NMDA 受體傷 24 h 記憶（皆 ※ 從圖判讀，見該頁 3.3–3.9） |
| [[s-aso-2016-dan-cell-type-rules]] | MB043C 以光代替糖訓練，比較學習與更新規則；與 PPL1-γ1pedc 同時活化 | 學得比 γ1pedc 慢；未配對 DAN 活化幾乎不削弱記憶（比值約 0.9，五組中的例外）；反轉配對後淨偏好約 0.1；能同時記住兩組配對；與 γ1pedc 合併時即時嫌惡、1 天後喜好約 +0.27 |

| [[s-yamada-2023-second-order-conditioning]] | MB043C 以光代替糖寫入一階（S1）記憶，再測它能否教出二階制約（[[c-second-order-conditioning]]）；MB043-split-LexA 在電生理實驗中只活化它；MB043C ＋ TNT 阻斷；比較各品系寫下的記憶動態（圖 8） | 一天後才做二階制約時，兩組受測的獎賞 DAN 中只有它仍能教出二階記憶（約 0.46，p ＝ 0.0046；PAM-γ5＋β′2a 約 0.14，不顯著）；阻斷後一天後的 S1 偏好（約 0.50 對 0.81）與二階記憶（約 0.19 對 0.43）都下降；與 SMP108、SMP353/354 相比，它寫下的記憶學得最慢、記得最久、最抗「只活化 DAN」的削弱（皆 ※ 從圖判讀）。**注意**：圖 6 中 MB043C 活化時 β1 也有明顯的多巴胺釋放（約 α1 峰值的四成，※ 從圖判讀），論文沒有討論 |

數值見各來源頁與 [[numbers]]。

## 已知的問題

- **兩篇把 α1 的特殊性連在一起，但沒有檢驗因果。** Aso 2016 引 Ichinose 2015 的迴圈來解釋「α1 不被未配對 DAN 削弱」，只是並列；Ichinose 2015 的迴圈本身也只有解剖與行為證據，沒有量到 MBON-α1 興奮 PAM-α1（見 [[s-ichinose-2015-reward-recurrent-circuit]] 第五節）。
- **「多巴胺在訓練後持續釋放」是模型。** Ichinose 2015 用它解釋為什麼訓練後 1 小時內關掉 PAM-α1 也會傷 24 小時記憶（見上表）；但該篇沒有量多巴胺，圖題的「dopamine release」是推論。
- **陰性結果樣本小。** 測驗時阻斷 PAM-α1 不影響記憶（即「提取記憶不需要 PAM-α1」），這組的 n 為 7、7、10，對照分數也偏低。
- **兩篇的飢餓與訓練條件不同**：Ichinose 用真糖、T 迷宮、餓到死亡率 5–15%；Aso 用光、競技場，圖 2、3 是否先餓未說明，圖 4 餓 48 小時。數值不宜跨篇比。
- **RNAi 降低程度未驗證**（Ichinose 2015）。
- **Yamada 2023 的「老師」與 MB043C 的專一性。** 該篇以 MB043C 為 α1 的工具，但同一品系活化時 β1 也釋放多巴胺（該篇圖 6，本庫稽核）；「老師是 α1」的結論在這一點上要打折。圖 8 的記憶持久度上，α1 與 γ5、β′2a 的差別也不顯著（見 [[s-yamada-2023-second-order-conditioning]] 第五節）。

## 相關

- 細胞群：[[e-dopaminergic-neuron]]；同格輸出：[[e-mbon-alpha1]]、[[e-mbon]]；其他型：[[e-ppl1-gamma1pedc]]
- 品系：[[e-split-gal4]]、[[e-r58e02]]；工具：[[e-shibire-ts]]、[[e-cschrimson]]、`e-tnt`
- 概念：[[c-memory-consolidation]]、[[c-us-substitution]]、[[c-second-order-conditioning]]、[[c-appetitive-memory]]
- 主題：[[t-mbon-dan-feedback]]、[[t-memory-updating]]
- 來源：[[s-aso-2014-mb-architecture]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-yamada-2023-second-order-conditioning]]
