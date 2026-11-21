---
title: MB247-GAL4 驅動品系（MB247-GAL4）
created: 2026-11-21
updated: 2026-11-21
tags: [entity, active, cross-domain]
confidence: medium
---

# MB247-GAL4 驅動品系（MB247-GAL4）

**庫內兩篇用來代表「KC」的一般 GAL4 品系，兩篇都拿它做同一件事：在 Kenyon 細胞裡把多巴胺受體補回去。** 它標到的範圍被描述成 α/β 與 γ 葉，但**沒有任何一篇量過它標了幾顆 KC**，而這件事直接造成庫內一個無法檢驗的解釋（見「已知的問題」）。

## 是什麼

MB247 是一段蕈狀體的調控序列，用它做成的工具在庫內有三個版本，**不可互換**：

| 版本 | 做什麼 | 庫內用例 |
|---|---|---|
| **MB247-GAL4**（本頁） | 在 KC 裡打開外加基因 | Vogt 2014、Ichinose 2015 |
| **MB247-GAL80** | 在 KC 的範圍內把別的 GAL4 **壓掉**（空間上扣除，**不是**溫控版，見 [[e-gal80ts]]） | Vogt 2014 圖 5A 的關鍵對照；[[s-aso-2014-mb-architecture]] |
| **MB247-switch** | 餵 RU-486 才打開，操作限成蟲期 | [[s-aso-2019-nitric-oxide-cotransmitter]] |

另有 **mb247-DsRed**（讓蕈狀體帶紅色螢光當地標，[[s-dylla-2017-trace-conditioning-dan-plasticity]]），那是報導基因不是驅動品系。

## 版本與規模（各篇怎麼描述它標到誰）

| 來源 | 寫法 | 標到誰（依該篇） |
|---|---|---|
| Vogt 2014 | MB247-GAL4 | 正文寫 α/β 與 γ 葉的 KC；救援實驗的文字只寫「in the KCs」，未說涵蓋哪幾類。**沒有給顆數** |
| Ichinose 2015 | MB247-GAL4 | 正文只寫「in KCs」，**沒說只限 α/β**；該篇的 α/β 專一性來自另兩條品系（[[e-c739-gal4]]、[[e-mb008b]]）的 RNAi |

**兩篇都沒有量它標了幾顆 KC**：？待查。數值見 [[numbers]]。

## 庫內誰用了它

| 來源 | 讓 KC 帶上什麼 | 得到什麼 |
|---|---|---|
| [[s-vogt-2014-shared-visual-olfactory-circuits]] | (1) UAS-DopR⁺（在 *dumb²* 背景下救援，見 [[e-dumb2]]）；(2) UAS-shi<sup>ts1</sup>（阻斷 KC 輸出），全程、只在訓練、或只在測驗 | (1) *dumb²* 的兩種**顏色**記憶皆近零（+0.22／−0.21 → −0.01／−0.01），KC 中補回 DopR⁺ 後**嫌惡回復到約 97%、欲求只回到約 58%**（本庫計算；論文只寫 restores both forms，且只檢定「突變 vs 救援」）。(2) 全程阻斷：兩種顏色記憶都受損（圖 5A）。分時段：嫌惡在訓練與測驗時**都**必要（−0.13 → −0.02、−0.12 → 0.00，n ＝ 10–16），欲求同樣兩段都必要（+0.10 → 0.00、+0.06 → −0.03，n ＝ 10–28） |
| [[s-ichinose-2015-reward-recurrent-circuit]] | UAS-DopR1（在 *dumb²* 背景下救援） | 救援組的獎賞長期記憶與野生型「無顯著差異」，但**柱高約為野生型七成、n ＝ 7**，而且缺「*dumb²* 同型合子只帶 MB247、不帶 UAS」這個對照。另一組（*dumb²*/+ 雜合子帶 MB247）約 0.29，比救援組還低 |

## 已知的問題

- **「α/β＋γ」這個描述不足以預測結果。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 正文把 MB247 與 201y-GAL4 都描述成標 α/β 與 γ 葉，但訓練期阻斷的結果**相反**：MB247 顯著受損（圖 8E），201y 完全沒有效果（圖 8G）。論文唯一的解釋是 201y 標的是「較小的一組 KC」，而該篇**沒有量過任何一條品系標了幾顆 KC**，所以這個解釋在該篇內不可檢驗。**引用「阻斷 α/β＋γ」時一定要寫出用的是哪一條品系。**
- **驅動品系本身帶來的背景效應可以很大。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 圖 5A 的 +/MB247 嫌惡對照是全篇最深的一根柱（−0.235），比 shi/+（−0.125）深了近一倍。**所以唯一可用的比較是「實驗組對同組的兩個對照」**，不是跨圖比絕對值。
- **救援的完整度在兩篇都沒有被檢定。** Vogt 2014 只檢定「突變 vs 救援」，沒有檢定「救援 vs 野生型」；Ichinose 2015 的救援組約為野生型七成卻寫成無顯著差異（n ＝ 7）。**兩篇都在「restores」這個詞上把部分救援與完全救援抹平了。** 可能的原因（MB247 不涵蓋全部 KC、或 DopR 在蕈狀體外也參與）兩篇的資料都分不出來：？待查。
- **測驗時阻斷讓分數越過零點，論文未置一詞。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 圖 8L：測驗時阻斷 MB247，欲求 LI 變成 **−0.03**（避開配過糖的顏色）。檢定只做了「實驗組 vs 兩個對照」，沒有做「實驗組 vs 零」。
- **MB247-GAL80 的存在是一把雙面刃。** 它讓 201y 那一組能做出「可以失敗而沒有失敗」的對照（[[s-vogt-2014-shared-visual-olfactory-circuits]] 圖 5A 最右組，兩種記憶完全回復），但同一篇的五條 split-GAL4 沒有任何等價對照。見 [[e-split-gal4]]。

## 相關

- 細胞：[[e-kenyon-cell]]、[[e-mushroom-body]]
- 其他 KC 品系：[[e-ok107-gal4]]、[[e-c739-gal4]]、[[e-c305a-gal4]]、[[e-238y-gal4]]、[[e-mb008b]]；品系原理見 [[e-split-gal4]]
- 工具與受體：[[e-dopamine-receptor]]、[[e-dumb2]]、[[e-shibire-ts]]、[[e-gal80ts]]
- 概念：[[c-acquisition-vs-retrieval]]、[[c-mb-compartment]]
- 來源：[[s-vogt-2014-shared-visual-olfactory-circuits]]、[[s-ichinose-2015-reward-recurrent-circuit]]
- 待開頁面：`e-mb247-gal80`、`e-mb247-switch`、`e-201y-gal4`、`e-mb247-dsred`
