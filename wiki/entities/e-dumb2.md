---
title: dumb² 等位基因（*dumb²*）
created: 2026-11-21
updated: 2026-11-21
tags: [entity, active, cross-domain]
confidence: medium
---

# *dumb²* 等位基因（*dumb²*）

**多巴胺受體 DopR（DopR1、dumb）的一個 PiggyBac 插入無效突變；插入的片段帶 UAS，所以同一個等位基因既是突變、又能被 GAL4 把受體叫回來表現。** 這個雙重性質是它在庫內的全部價值：它讓「全身沒有受體」與「只在某一群細胞有受體」可以在同一個遺傳背景下比較。庫內兩篇用它。

## 是什麼

PiggyBac 是一種轉位子；它插進 *DopR* 基因後讓該基因失效，而插入片段本身帶著 UAS 序列，於是有 GAL4 的細胞會由這個插入處表現 DopR。所以一次雜交就能得到四種基因型：純突變、只帶 GAL4、救援（突變 ＋ GAL4）、野生型。受體本身見 [[e-dopamine-receptor]]。

**它是全身性的突變。** 救援的範圍由 GAL4 決定，庫內兩篇用的都是 [[e-mb247-gal4]]（KC）。

## 版本與規模

| 來源 | 怎麼寫它 | 救援用的驅動品系 |
|---|---|---|
| Vogt 2014 | 「DopR null mutant *dumb²*（which also allows *dumb* expression via GAL4）」 | MB247-GAL4，正文只寫「in the KCs」，未說涵蓋哪幾類 KC |
| Ichinose 2015 | *dumb²*，在它的背景下以 MB247 驅動 UAS-DopR1 | MB247-GAL4；親本為 *UAS-DopR1;;dumb²* 或 Canton-S 雌 × *MB247-GAL4;dumb²* 或 *dumb²* 雄 |

數值見 [[numbers]]。

## 庫內誰用了它

| 來源 | 量什麼 | 得到什麼 |
|---|---|---|
| [[s-vogt-2014-shared-visual-olfactory-circuits]] | **顏色**制約的欲求與嫌惡記憶（立即測，n ＝ 8–16） | *dumb²* 兩種記憶皆近零（野生型 +0.22／−0.21 → −0.01／−0.01）；KC 中補回 DopR⁺ 後**嫌惡回復到約 97%、欲求只回到約 58%**（本庫計算）。**關鍵對照**：表 1 顯示 *dumb²* 與救援組的天生電擊迴避**都**異常（−0.289 與 −0.255，野生型 −0.471），但救援組的記憶回來了，所以記憶缺陷不是感覺缺陷 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 獎賞的長期記憶（氣味，24 小時） | 在 *dumb²* 背景下以 MB247 在 KC 補回 DopR1，長期記憶與野生型「無顯著差異」，但柱高約為野生型七成、n ＝ 7 |

## 已知的問題

- **救援的「完整度」在兩篇都沒有被檢定。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 的星號只畫在「突變 vs 救援」之間，沒有檢定「救援 vs 野生型」，而欲求只回到約 58%；論文寫成 restores both forms。[[s-ichinose-2015-reward-recurrent-circuit]] 的救援組約七成也寫成無顯著差異。**「救回來了」與「回到原水準」不是同一句話。**
- **缺一個對照，而它決定救援能不能歸給補回的受體。** 應有的對照是「*dumb²* 同型合子、只帶 MB247-GAL4、不帶 UAS-DopR1」，[[s-ichinose-2015-reward-recurrent-circuit]] 沒有做。少了它，就無法排除 MB247 的插入本身讓突變果蠅的記憶變好。該篇另一組（*dumb²*/+ 雜合子帶 MB247，約 0.29）**不是**突變果蠅，不能當這個對照。
- **它同時造成感覺缺陷。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 的表 1 顯示 *dumb²* 的天生電擊迴避受損。該篇用救援組把這個干擾排除掉了（見上表），但**任何只有突變組、沒有救援組的實驗，都無法分開感覺與記憶**。
- **救援的解析度只到「KC」。** 兩篇都用 MB247，而 MB247 標了幾顆 KC、涵蓋哪幾類，兩篇都沒有量（見 [[e-mb247-gal4]]）。所以「DopR 在 KC 上接收這個訊號」成立，「DopR 在 α/β KC 上」不是由救援實驗支持的——[[s-ichinose-2015-reward-recurrent-circuit]] 的 α/β 專一性來自另兩條品系的 RNAi（[[e-c739-gal4]]、[[e-mb008b]]）。
- **它只動 DopR1 這一個受體。** KC 上還有 Dop1R2／DopR2（[[s-handler-2019-dopamine-receptor-timing]]、[[s-kaldun-2025-dop1r2-memory-phases]]），*dumb²* 的結果不能推廣到「多巴胺受體」整體。

## 相關

- 受體：[[e-dopamine-receptor]]
- 驅動品系：[[e-mb247-gal4]]、[[e-c739-gal4]]、[[e-mb008b]]、[[e-split-gal4]]
- 細胞：[[e-kenyon-cell]]
- 概念：[[c-appetitive-memory]]、[[c-camp-signaling]]
- 來源：[[s-vogt-2014-shared-visual-olfactory-circuits]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-kaldun-2025-dop1r2-memory-phases]]
- 待開頁面：`e-dop1r2`、`e-piggybac`
