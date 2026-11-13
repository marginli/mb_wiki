---
title: 熱活化通道（dTrpA1）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# 熱活化通道（dTrpA1）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **驅動品系（driver line）**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半，兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型寫「X/+」表示只帶一個品系的對照組。
- **蕈狀體、KC、MBON、DAN、PAM／PPL1**：果蠅腦中把氣味和好壞經驗連起來的構造（[[e-mushroom-body]]）；代表氣味的 Kenyon 細胞；讀出 KC 訊號的輸出神經元（[[e-mbon]]）；送出獎賞或懲罰訊號的多巴胺神經元（[[e-dopaminergic-neuron]]），PAM 群多傳獎賞、PPL1 群多傳懲罰。
- **章魚胺（octopamine）**：另一種神經調節物，庫內與甜味獎賞有關（[[c-octopamine-reward-signal]]）。
- **CS+／CS−、US**：訓練時配了糖、電擊或人工活化的氣味，與沒配的對照氣味；US 是增強物本身。
- **PI（表現指數）**：行為分數（[[c-performance-index]]）。
- **轉殖基因的插入位置（attP16、attP18、VK00005 等）**：同一個基因放進基因組的不同位置，表現量會不同；換插入位置重做是一種獨立驗證。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值。

## 是什麼

**dTrpA1 是一個溫度敏感的陽離子通道：把表現它的神經元升到高溫，那些神經元就放電；降溫就停。** 庫內三篇都用它回答「這群神經元**夠不夠**」（充分性），正好和 [[e-shibire-ts]] 回答的「少了它行不行」（必要性）相反。[[s-burke-2012-octopamine-dopamine-reward]] 寫它在 25 °C 以上就讓神經元放電。

它最常見的用法是**把人工活化塞進制約協定裡取代真的增強物**：聞某個氣味的時候升溫，等於告訴果蠅「這個氣味有好事（或壞事）」。庫內三篇各用它取代一種增強：章魚胺神經元取代糖（Burke 2012）、PPL1-γ1pedc 取代電擊（Aso 2014b）、MBON-α1 取代糖（Ichinose 2015）。[[s-aso-2014-mbon-valence]] 另外用它做兩天的連續活化，看睡眠。

## 版本與規模（庫內各篇的溫度與時段）

| 來源 | 活化溫度 | 基線溫度 | 活化時段 | 轉殖基因版本 |
|---|---|---|---|---|
| Burke 2012 | 31 °C | 23 °C | 第二個氣味的 2 分鐘 | uas-dTrpA1；章魚胺神經元那組另以 Tdc2-LexA 驅動 lexAop-dTrpA1 |
| Aso 2014b（睡眠） | 28.5 °C | 21.5 °C | 第 4–5 天連續 2 天 | 初篩 10X UAS-dTrpA1（attP16），複篩 pJFRC124-20XUAS-IVS-dTrpA1（attP18） |
| Aso 2014b（取代電擊） | 該頁未寫：？待查 | — | 訓練時 | 同上 |
| Ichinose 2015 | 30 °C | 24 °C | 聞氣味的 1 分鐘 | UAS-dTrpA1 |

## 庫內誰用了它

| 來源 | 活化哪些神經元（品系） | 得到什麼 |
|---|---|---|
| [[s-burke-2012-octopamine-dopamine-reward]] | 章魚胺神經元（Tdc2-GAL4、Tdc2-LexA） | 不給糖也植入了欲求記憶，**而且果蠅是飽足的**：立即（3 分鐘）記憶顯著高於全部其他組（p < 0.001，n ≥ 14），30 分鐘仍顯著（p < 0.05）。在 *dumb¹*（DopR 突變）或 *oamb* 突變背景中植入不成，所以章魚胺的增強走多巴胺的下游（見 [[c-us-substitution]]） |
| [[s-aso-2014-mbon-valence]] | PPL1-γ1pedc（MB438B）取代電擊 | 3 分鐘記憶約 −0.53（對照約 0）。MB438B 依該篇表 2 也弱標 PPL1-α2α′2，效果可能部分來自這型 DAN |
| [[s-aso-2014-mbon-valence]] | 各型 MBON 連續活化兩天，量睡眠 | 初篩 12 條陽性（5 條減少睡眠、7 條增加）；換插入位置複篩，圖 12D 的 8 條都重現。減少的約 −20% 到 −30%、增加的約 +23% 到 +28%，對照約 +5%（※ 從圖判讀）。促醒的大致是「走開」那群（麩胺酸），促眠的大致是「靠近」那群 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | MBON-α1（MB310C） | 不給糖，只在聞氣味那 1 分鐘活化 MBON-α1，隔天仍偏好該氣味。作者據此說 MBON-α1 的活動本身足以觸發長期記憶，並推論它是經由迴圈帶動 PAM-α1（見 [[t-mbon-dan-feedback]]） |

數值見 [[numbers]]。

## 已知的問題

- **溫度與氣味身分共變。** [[s-burke-2012-octopamine-dopamine-reward]] 的協定是「氣味 A 在 23 °C、氣味 B 在 31 °C」，所以「果蠅學到氣味 B 配好事」與「果蠅學到氣味 B 配溫度變化」在設計上分不開。該篇做了允許溫度對照（圖 1c），但共變本身沒有解掉。
- **升溫本身改變果蠅的整體狀態。** 這對行為讀數與睡眠讀數都成立；Aso 2014b 的睡眠實驗連續兩天 28.5 °C。
- **「足以」不等於「正常情況下就是這樣做的」。** 人工活化整群細胞的強度與樣式和自然活動不同。[[s-ichinose-2015-reward-recurrent-circuit]] 的結論「MBON-α1 足以觸發 LTM」只說明充分性，迴圈那一段是推論。
- **各篇的溫度與時長都不同**（28.5、30、31 °C；1 分鐘到 2 天），所以跨篇比較活化強度沒有共同的刻度。
- **活化範圍受品系限制。** Aso 2014b 的 MB438B 也弱標到 PPL1-α2α′2；Burke 2012 的 Tdc2-GAL4 標的是章魚胺神經元整群，不是某一型。
- **兩篇的對比實驗用了不同的活化工具。** Aso 2014b 的光遺傳篩選用 [[e-cschrimson]]、雌蠅、25 °C、數十秒，睡眠用 dTrpA1、處女雌蠅、28.5 °C、兩天，品系也不完全重疊（睡眠用 MB077C、光遺傳用 MB077B）。「促醒＝走開、促眠＝靠近」是兩組獨立實驗的類比，不是同一組果蠅的結果。
- **⚠️ Ichinose 2015 的方法有一處缺單位**：dTrpA1 實驗的氣味杯直徑寫作「3 mm and 5」，第二個值沒有單位（該頁第五節第 9 條）。

## 相關

- 工具：[[e-shibire-ts]]（相反方向的操作）、[[e-cschrimson]]、[[e-p2x2]]、[[e-split-gal4]]、[[e-t-maze]]
- 細胞：[[e-mbon-alpha1]]、[[e-ppl1-gamma1pedc]]、[[e-pam-alpha1]]、[[e-dopaminergic-neuron]]
- 概念：[[c-us-substitution]]、[[c-octopamine-reward-signal]]、[[c-appetitive-memory]]、[[c-valence-coding]]
- 主題：[[t-mbon-dan-feedback]]、[[t-mbon-to-action]]
- 來源：[[s-burke-2012-octopamine-dopamine-reward]]、[[s-aso-2014-mbon-valence]]、[[s-ichinose-2015-reward-recurrent-circuit]]
- 待開頁面：`e-tdc2-gal4`、`e-mb310c`、`e-mb438b`、`c-sleep-regulation`
