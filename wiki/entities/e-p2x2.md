---
title: ATP 門控通道 P2X2（化學活化，chemogenetic activation）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: high
---

# ATP 門控通道 P2X2（化學活化，chemogenetic activation）


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

P2X2 是一種遇到 ATP 就打開的離子通道。用驅動品系（見 [[e-split-gal4]]）讓選定的神經元多帶這個通道，再用玻璃細管把 ATP 送到這些神經元附近，就只有帶通道的那幾顆被活化（Cohn 2015 的術語表；Handler 2019 稱為化學遺傳 chemogenetic 活化）。它是光遺傳（[[e-cschrimson]]）之外的另一種「用人工方法叫醒特定神經元」的工具，常用在把腦取出來的離體製備（[[c-ex-vivo-explant]]），以代替真的獎賞或懲罰（見 [[c-us-substitution]]）。本庫兩篇都出自同一實驗室（Ruta 實驗室）。

## 版本與規模（刺激參數）

| 項目 | Cohn 2015 | Handler 2019 |
|---|---|---|
| 表現 P2X2 的細胞 | 58E02 所標的 DAN（含 γ4、γ5，γ3 標記不穩定）；γ2 DAN；γ2、γ3、γ4、γ5 各一型 MBON | R58E02-LexA（基因型表標「γ4–5 DANs」）；73F07-LexA（γ2 DAN） |
| ATP 與電極 | 2 mM ATP，7–10 MΩ 玻璃管；放在中葉背側、DAN 樹突與 MBON 軸突所在處 | 2 mM ATP，7–10 MΩ；放在中葉背側的上內側前大腦（引 Cohn 2015） |
| 怎麼送出 | 正壓脈衝；**時長與壓力主文未寫**（？待查） | 離子導入（iontophoresis）：5 × 100 ms，間隔 20 ms，2.5–5 V（約 0.6 s）；在體實驗 4 × 100 ms |
| 製備 | 離體與在體 | 離體為主；在體（圖 3F、S4E–F） |

參數見 [[numbers]]。

## 庫內誰用了它

| 來源 | 活化誰 | 用來做什麼 |
|---|---|---|
| [[s-cohn-2015-coordinated-neuromodulation]] | γ4/γ5 DAN、γ2 DAN；單一 γ MBON | 單獨活化 DAN（與 KC 刺激相隔 > 45 s）讓本格 KC→MBON 突觸增強（例：γ4 MBON EPSC 約 1.5 → 16 pA，圖判讀）；與 KC 刺激相隔 < 500 ms 則減弱；活化任一 γ MBON 都改變各格 DAN 的活動（見 [[t-mbon-dan-feedback]]） |
| [[s-handler-2019-dopamine-receptor-timing]] | PAM（γ4/γ5）、γ2 DAN | 改變 DAN 與 KC 刺激的時間差（−6 到 +6 s），量 γ4 MBON 突觸、KC 軸突 cAMP、內質網鈣與多巴胺釋放（見 [[c-cs-us-timing]]） |

## 已知的問題

- **刺激強度兩篇無法比對。** Cohn 主文沒有給 ATP 噴注的時長與壓力，所以 Handler 用「較強或較長的多巴胺釋放」解釋 Cohn 的 > 45 s 增強，無從核對；兩篇的時間尺度差異見 [[syn-contradictions]] 1.3。
- **ATP 噴在同一處，需要「無 P2X2」對照。** Cohn 主文只在 KC 末梢成像（圖 5C）報了不帶 P2X2 的對照；DAN 成像（圖 3）沒有同樣的對照，ATP 本身是否直接影響附近 DAN：？待查（該來源頁 3.3）。Handler 在部分實驗直接量 DAN 的鈣，確認電極位置能活化 DAN（方法）。
- **被活化的範圍取決於品系。** R58E02 的標記範圍各篇說法不同（見 [[e-r58e02]] 與 [[syn-contradictions]] 1.5）；Cohn 的 58E02 對 γ3 標記不穩定，「活化 γ4/γ5 DAN」有時也包括 γ3。
- **不是自然刺激。** 活化樣式與真實獎懲引起的 DAN 放電未必相同；P2X2 表現量兩篇都沒寫：？待查。

## 相關

- 工具：[[e-cschrimson]]、[[e-r58e02]]、[[e-gcamp]]
- 概念：[[c-us-substitution]]、[[c-ex-vivo-explant]]、[[c-kc-mbon-plasticity]]、[[c-cs-us-timing]]
- 細胞：[[e-dopaminergic-neuron]]、[[e-mbon-gamma4]]
- 主題：[[t-timing-rules]]、[[t-mbon-dan-feedback]]；矛盾：[[syn-contradictions]]
- 來源：[[s-cohn-2015-coordinated-neuromodulation]]、[[s-handler-2019-dopamine-receptor-timing]]
