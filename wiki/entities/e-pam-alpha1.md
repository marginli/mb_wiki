---
title: PAM-α1 多巴胺神經元（PAM-α1）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: medium
---

# PAM-α1 多巴胺神經元（PAM-α1）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蘑菇體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ2、α1）；細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PAM、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PAM 群多傳遞獎賞，PPL1 群（Handler 2019 寫作 PPL）多傳遞懲罰。
- **MBON**：蘑菇體輸出神經元，接收 KC 的訊號、推動果蠅靠近或走開；學習改變的是 KC→MBON 突觸的強弱。
- **CS+／CS−、順向／逆向**：訓練時配了糖、電擊或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。順向配對＝氣味先、多巴胺後；逆向配對＝多巴胺先、氣味後。
- **PI（表現指數）、LI（學習指數）**：行為分數。一群果蠅在兩種氣味間選擇，換算成一個數；多數篇落在 −1 到 +1（Hige 2015 的刻度不同），0＝沒有偏好，正負號的意思各篇不同（見 [[c-performance-index]]）。
- **消退、再鞏固**：學會後再聞 CS+ 卻沒有糖或電擊，學到的反應減弱，叫消退（[[c-memory-extinction]]）；記憶被叫出來後暫時變得不穩定、再重新存好，叫再鞏固（[[c-memory-consolidation]]）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半（AD 與 DBD），兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型寫「X/+」表示只帶一個品系的對照組。
- **活化與阻斷工具**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；P2X2 遇到 ATP 讓神經元放電（[[e-p2x2]]）；shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]），全程維持低溫的「允許溫度對照」用來排除品系本身的效果。
- **讀數與製備**：ΔF/F0＝螢光相對刺激前基線的變化比例（0.5＝亮了 50%），以遇鈣變亮的 GCaMP 量神經元活動（[[e-gcamp]]）；離體＝把腦取出泡在養液裡做實驗（[[c-ex-vivo-explant]]），活體＝活果蠅固定後打開頭殼看。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「text.txt 第 N 行」＝本庫保存的論文全文文字檔的行號；「該頁」指表格同一列的來源頁。

## 是什麼

**PAM-α1 是 PAM 群（多傳遞獎賞）中的一型多巴胺神經元（DAN），把多巴胺送進蘑菇體 α 葉最靠近根部的 α1 區室。** 名字前段 PAM 是細胞群（以細胞體位置命名），後段 α1 是它支配的區室（見 [[c-mb-compartment]]）。同一格的輸出神經元是 MBON-α1；Ichinose 2015 發現 MBON-α1 的末梢回到 PAM-α1 的樹突旁，構成一個迴圈（見 [[t-mbon-dan-feedback]]）。本庫兩篇用它，結論都指向「較慢、較穩的獎賞記憶」。PAM-α1 有幾顆細胞，Ichinose 2015 沒有給（該來源頁搜尋原文後確認）。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 用途 |
|---|---|---|
| MB299B（split-GAL4） | Ichinose 2015（引 Aso 2014a、Yamagata 2015） | 阻斷（shi）、降低 NMDA 受體（RNAi） |
| R72D01-LexA | Ichinose 2015 | 與 MBON-α1 雙標記、GRASP 解剖 |
| MB043C（split-GAL4） | Aso 2016 | 驅動 CsChrimson，以光代替糖 |
| R58E02-GAL4／-LexA | Aso 2016、Felsenberg 2017 | 涵蓋它在內的大範圍 PAM（見 [[e-r58e02]]） |

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-ichinose-2015-reward-recurrent-circuit]] | 訓練時、訓練後 1 小時、測試時分別以 shi 阻斷；在 PAM-α1 降低 NMDA 受體次單元 dNR-1 或 dNR-2 | 訓練時阻斷：24 h 記憶剩約 18%，5 分鐘記憶不顯著；訓練後立刻阻斷 1 h 也傷 24 h 記憶，22 h 後阻斷不傷；測試時阻斷不顯著（n 小）；降低 NMDA 受體傷 24 h 記憶（皆 ※ 從圖判讀，見該頁 3.3–3.9） |
| [[s-aso-2016-dan-cell-type-rules]] | MB043C 以光代替糖訓練，比較學習與更新規則；與 PPL1-γ1pedc 同時活化 | 學得比 γ1pedc 慢；未配對 DAN 活化幾乎不削弱記憶（比值約 0.9，五組中的例外）；反轉配對後淨偏好約 0.1；能同時記住兩組配對；與 γ1pedc 合併時即時嫌惡、1 天後喜好約 +0.27 |

數值見各來源頁與 [[numbers]]。

## 已知的問題

- **兩篇把 α1 的特殊性連在一起，但沒有檢驗因果。** Aso 2016 引 Ichinose 2015 的迴圈來解釋「α1 不被未配對 DAN 削弱」，只是並列；Ichinose 2015 的迴圈本身也只有解剖與行為證據，沒有量到 MBON-α1 興奮 PAM-α1（見 [[s-ichinose-2015-reward-recurrent-circuit]] 第五節）。
- **「多巴胺在訓練後持續釋放」是模型。** Ichinose 2015 用它解釋為什麼訓練後 1 小時內關掉 PAM-α1 也會傷 24 小時記憶（見上表）；但該篇沒有量多巴胺，圖題的「dopamine release」是推論。
- **陰性結果樣本小。** 測驗時阻斷 PAM-α1 不影響記憶（即「提取記憶不需要 PAM-α1」），這組的 n 為 7、7、10，對照分數也偏低。
- **兩篇的飢餓與訓練條件不同**：Ichinose 用真糖、T 迷宮、餓到死亡率 5–15%；Aso 用光、競技場，圖 2、3 是否先餓未說明，圖 4 餓 48 小時。數值不宜跨篇比。
- **RNAi 降低程度未驗證**（Ichinose 2015）。

## 相關

- 細胞群：[[e-dopaminergic-neuron]]；同格輸出：[[e-mbon]]；其他型：[[e-ppl1-gamma1pedc]]
- 品系：[[e-split-gal4]]、[[e-r58e02]]；工具：[[e-shibire-ts]]、[[e-cschrimson]]
- 概念：[[c-memory-consolidation]]、[[c-us-substitution]]
- 主題：[[t-mbon-dan-feedback]]、[[t-memory-updating]]
- 來源：[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]
