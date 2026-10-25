---
title: T 迷宮（T-maze）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: high
---

# T 迷宮（T-maze）


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

測果蠅學到什麼的標準裝置：一群果蠅被送到 T 字形岔路的中央，兩條岔路各通一種氣味，讓牠們在限定時間內選邊，再數兩邊各有幾隻，換算成一個分數（表現指數，見 [[c-performance-index]]）。訓練通常也在同一套管子裡進行：讓果蠅聞一個氣味時給電擊或糖（CS+），聞另一個時不給（CS−）。一次測驗得到的是**一群**果蠅的一個分數，所以統計的 n 是「群」不是「隻」。本庫另有一種不同的裝置，四象限嗅覺競技場，見 [[e-olfactory-arena]]。

## 版本與規模（各篇的協定）

| 來源 | 增強訊號 | 每群 | 測驗 | 分數 |
|---|---|---|---|---|
| Tomchik 2009 | 電擊；氣味與電擊各 60 s（引 Tully & Quinn 1985） | ？待查 | 訓練後 3 分鐘 | P.I.：0＝一半一半，1＝全部選對 |
| Ichinose 2015 | 乾燥蔗糖紙；兩氣味各 1 min | 約 50 隻 | 2 分鐘，取後 60 s；5 min（STM）或 24 h（LTM） | 學習指數 LI，偏好指數公式未寫 |
| Felsenberg 2017 | 乾蔗糖；CS− 2 min → 空氣 30 s → CS+ 2 min | 50–100 隻 | 2 分鐘；訓練後 6 h（部分 3 h、24 h） | PI，公式只引 Krashes & Waddell 2008 |
| Felsenberg 2018 | 90 V 電擊 12 下；CS+ 1 min → 空氣 45 s → CS− 1 min | 約 80–100 隻 | 2 分鐘；訓練後 60 min | P.I.＝（CS+ 臂數 − CS− 臂數）÷ 總數 |

參數見 [[numbers]]。

## 庫內誰用了它

| 來源 | 用來量什麼 | 得到什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | 痕跡制約（氣味結束後空白一段才電擊）的行為時間窗 | 同時給約 0.72，trace 0／15／30／45 s 約 0.47／0.22／0.13／0.05，倒序約 0.04（n＝6，圖判讀） |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 以 [[e-shibire-ts]] 在不同時段關掉迴路後的 STM 與 LTM；類化（換成相似氣味測，見 [[c-odor-generalization]]） | 訓練時與訓練後 1 h 內需要 PAM-α1、MBON-α1、α/β KC，只影響 LTM（見 [[c-memory-consolidation]]） |
| [[s-felsenberg-2017-re-evaluation]] | 訓練後再聞 CS+ 或 CS−（不給糖）之後的 6 h 記憶 | 再聞 CS+ → 消退（PI 約 0.3 → 約 0）；再聞 CS− → 再鞏固（見 [[c-memory-extinction]]、[[c-memory-consolidation]]） |
| [[s-felsenberg-2018-memory-extinction]] | 嫌惡記憶在再聞 CS+ 之後的 60 min 記憶 | 消退只消掉約三分之一到一半的躲避（例：約 −0.39 → −0.20，圖判讀） |

Handler 2019 不用 T 迷宮，只在正文把它當成對照，說自己的小室能反覆訓練與測驗；它的裝置與指標見 [[c-performance-index]]。

## 已知的問題

- **正負號約定不一致，跨篇並列前要先對齊。** Tomchik 2009：正值＝避開被電的氣味（1＝全部選對）。Felsenberg 2018：（CS+ − CS−）÷ 總數，**躲 CS+ 是負值**。Felsenberg 2017：正值＝偏向 CS+（糖獎賞）。Ichinose 2015：LI 正值＝選配糖的氣味，但換算公式沒寫。四篇中只有 Felsenberg 2018 寫出公式。
- **公式與上下限未寫的，只能做同篇內的相對比較**（Tomchik、Ichinose、Felsenberg 2017）。
- **氣味互換取平均。** Ichinose、Felsenberg 2017／2018 都讓兩種氣味輪流當 CS+，兩組平均成一個 n；Tomchik 的作法：？待查。
- **測驗時點不同**：3 分鐘、5 分鐘、60 分鐘、6 小時、24 小時都有，「記憶強弱」不能跨篇比。
- 每群隻數與 n 的單位，Tomchik 2009 沒寫清楚（見 [[c-performance-index]] 陷阱 3）。

## 相關

- 概念：[[c-performance-index]]、[[c-memory-extinction]]、[[c-memory-consolidation]]、[[c-cs-us-timing]]、[[c-odor-generalization]]
- 工具：[[e-shibire-ts]]、[[e-olfactory-arena]]
- 主題：[[t-timing-rules]]、[[t-memory-updating]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-handler-2019-dopamine-receptor-timing]]
