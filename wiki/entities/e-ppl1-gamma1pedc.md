---
title: PPL1-γ1pedc 多巴胺神經元（PPL1-γ1pedc, MB-MP1）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: medium
---

# PPL1-γ1pedc 多巴胺神經元（PPL1-γ1pedc, MB-MP1）


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

**PPL1-γ1pedc 是一型傳遞懲罰的多巴胺神經元（DAN），把多巴胺送進蘑菇體的 γ1pedc 區室。** 名字分兩段：PPL1 是它所屬的 DAN 細胞群（以細胞體所在位置命名，這一群多傳遞懲罰）；γ1pedc 是它支配的區室，在 γ 葉最靠近根部的一格一帶（區室見 [[c-mb-compartment]]；字尾 pedc 的意思，本庫來源都沒有解釋：？待查）。舊名 MB-MP1（Hige 2015、Felsenberg 2017 都列出這個對照）。同一格裡接收 KC 訊號的輸出神經元是 [[e-mbon-gamma1pedc]]。本頁也收錄**專門標記它的品系 MB320C**：依 Hige 2015，MB320C「只標一顆 PPL1-γ1pedc 神經元」（text.txt 第 194–195 行）；左右腦是否各一顆，原文沒說：？待查。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 說明 |
|---|---|---|
| **MB320C**（split-GAL4；TH-p65ADZp／22B12-ZpGAL4DBD） | Hige 2015 自述「we created」；Aso 2016 圖 1C 圖說把其影像指向 Aso et al. 2014a | 只標這一型 |
| VT045661-LexA | Aso 2016 圖 4A | 另一套表現系統，用來與 α1 的 DAN 同時活化 |
| c061-GAL4;MBGAL80 | Felsenberg 2017 延伸圖 6f | 用於阻斷 MB-MP1 |
| MB504B、TH-GAL4 | Felsenberg 2017 延伸圖 6b–c；Hige 2015 | 涵蓋它的較廣品系（見 [[e-mb504b]]、[[e-th-gal4]]） |

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-hige-2015-heterosynaptic-plasticity]] | MB320C 驅動 CsChrimson，氣味配光，活體記錄 MBON-γ1pedc；行為上以光代替電擊 | 配對氣味的放電降 80% ± 5.7%、電荷降 90% ± 3.7%；逆向配對無效；學會迴避並類化到相似氣味 |
| [[s-aso-2016-dan-cell-type-rules]] | MB320C 驅動 CsChrimson，十個時間差的行為掃描與多種更新協定 | 光在氣味開始後 0–20 s → 嫌惡（PI 最低約 −0.45）；早 20–60 s → 喜好（約 +0.15）；學得快、1 天後幾乎消失、未配對 DAN 活化削弱記憶最多、只記得最後一組配對 |
| [[s-felsenberg-2017-re-evaluation]] | c061-GAL4;MBGAL80 驅動 shi^ts1 阻斷；在體成像它對氣味的反應 | 單獨阻斷不影響糖獎賞記憶的消退（延伸圖 3c）；訓練後對 CS+、CS− 的反應與假訓練無差異（延伸圖 4f） |

數值見各來源頁與 [[numbers]]。Felsenberg 2018 只經由 MB504B（含這一型在內的四型 PPL1）阻斷，沒有單獨操作它，不列入表。

## 已知的問題

- **逆向配對：突觸不變，行為卻能反轉。** Hige 2015 的逆向（光比氣味早約 2.0–0.5 s）突觸不變；Aso 2016 在早 10 s 也無效，早 20–60 s 才出現喜好。兩者都不是在同一條件下同時量突觸與行為；與 Handler 2019 的 γ4 結果並列見 [[syn-contradictions]] 1.1。
- **「一顆」只是品系的描述。** Hige 的單顆標記影像在補充圖 S1A：？待查。Aso 2016 圖 4A 改用 VT045661-LexA，兩種品系的表現量是否相近，該篇沒比較。
- **單獨阻斷無效不等於不參與。** Felsenberg 2017 中 MB504B（四型一起）阻斷能部分擋住消退，個別型別阻斷都不能；正文推測 MB-MP1 可能參與寫下消退記憶，但成像的 PPL1 細胞沒有指認型別。
- **行為與生理不是同一批果蠅。** Hige 2015 的突觸與行為用不同光協定；Aso 2016 全是行為。

## 相關

- 同格輸出：[[e-mbon-gamma1pedc]]；同群其他型：[[e-ppl1-gamma2alpha1]]；細胞群：[[e-dopaminergic-neuron]]
- 品系：[[e-split-gal4]]、[[e-mb504b]]、[[e-mb099c]]、[[e-th-gal4]]；工具：[[e-cschrimson]]、[[e-shibire-ts]]
- 概念：[[c-cs-us-timing]]、[[c-kc-mbon-plasticity]]、[[c-us-substitution]]
- 主題：[[t-timing-rules]]、[[t-memory-updating]]；矛盾：[[syn-contradictions]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2017-re-evaluation]]
