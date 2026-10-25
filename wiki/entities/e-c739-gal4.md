---
title: c739-GAL4 驅動品系（c739-GAL4）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, cross-domain]
confidence: medium
---

# c739-GAL4 驅動品系（c739-GAL4）


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

一個讓外加基因只在 **α/β 型 Kenyon 細胞**（[[e-kenyon-cell]]，軸突走 α 葉與 β 葉的那一類 KC）表現的驅動品系（驅動品系的原理見 [[e-split-gal4]]）。它是一般的 GAL4，不是 split-GAL4；Ichinose 2015 說它以「增強子陷阱」（enhancer trap，一種製作驅動品系的方法）得來。本庫兩篇都用它代表「α/β KC」，但一篇用它看細胞內的訊號分子，另一篇用它關掉這群細胞或降低其中的受體。

## 版本與規模

| 來源 | 搭配的效應基因 | 對照品系 |
|---|---|---|
| Tomchik 2009 | UAS-Epac1-camps（cAMP 感測器，見 [[e-epac-camp-sensor]]）；這一組改用插在第 3 號染色體的另一個感測器轉基因品系 | 同篇另以 238Y（三類 KC）、c305a（α′/β′）、1471（γ）標其他 KC |
| Ichinose 2015 | UAS-shibire<sup>ts1</sup>（[[e-shibire-ts]]）；UAS-DopR1-RNAi | 第二個 α/β KC 品系 MB008B（split-GAL4）並用 |

## 庫內誰用了它

| 來源 | 用來做什麼 | 得到什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | 離體腦中量 α/β KC 軸突（α 葉）與樹突（萼部）的 cAMP | 乙醯膽鹼＋多巴胺配對約為兩者單獨相加的 1.25 倍（協同較 238Y 的約 1.53 小）；多巴胺在葉部可靠地提高 cAMP，在萼部有升有降（見 [[c-coincidence-detection]]） |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 訓練時、訓練後 1 h 關掉 α/β KC 的輸出；在 α/β KC 降低多巴胺受體 DopR1（[[e-dopamine-receptor]]） | 訓練時阻斷：24 小時記憶約 0.15，對照約 0.42、0.44（n＝7）；訓練後 1 h 阻斷剩約 15%；降低 DopR1 後 LTM 約 0.13，對照約 0.43–0.53（皆圖判讀；見 [[c-memory-consolidation]]） |

數值見 [[numbers]]。

## 已知的問題

- **「α/β KC」是品系的標記範圍。** 涵蓋多少顆、是否漏標或多標到別的細胞，兩篇正文都沒有給數字：？待查。Ichinose 用 MB008B 重做是為了互相印證；兩個品系方向一致，但損害幅度不同（訓練時阻斷 c739 約 0.15、MB008B 約 0.26）。
- **樣本數不平衡。** Ichinose 2015 圖 7B 的 c739 兩組 n＝7，MB008B 兩組 n＝18–19，同樣的星號背後效果大小不同。
- **同一品系的對照值批次間差很多**：c739/+ 在 Ichinose 圖 9E 約 0.58、圖 9F 約 0.44。
- **Tomchik 的 c739 組同時換了驅動品系與感測器插入位置**，用來排除插入位置造成的假象；協同方向一致、幅度較小。

## 相關

- 細胞：[[e-kenyon-cell]]；品系：[[e-split-gal4]]
- 工具：[[e-epac-camp-sensor]]、[[e-shibire-ts]]、[[e-dopamine-receptor]]
- 概念：[[c-coincidence-detection]]、[[c-camp-signaling]]、[[c-memory-consolidation]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-ichinose-2015-reward-recurrent-circuit]]
