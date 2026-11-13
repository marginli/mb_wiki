---
title: DPM 神經元（dorsal paired medial neuron, MB-DPM）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# DPM 神經元（dorsal paired medial neuron, MB-DPM）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突排成幾條「葉」（α、β、γ 等），每條葉切成一格一格的「區室」（[[e-mushroom-body]]、[[c-mb-compartment]]）。
- **內在神經元（intrinsic neuron）**：Aso 2014a 對「整顆都在蕈狀體內、廣泛支配它」的神經元的分類；DPM 與 APL 屬此類，不分區室。
- **MBON、DAN**：蕈狀體輸出神經元；多巴胺神經元。
- **cAMP**：細胞內的第二傳訊者，多巴胺與章魚胺經受體提高它，是學習訊號的一環（[[c-camp-signaling]]）。
- **Epac1-camps、ΔR/R0**：遇 cAMP 改變顏色比例的螢光感測器；ΔR/R0＝顏色比例相對基線的變化率（[[e-epac-camp-sensor]]）。
- **c316**：Tomchik 2009 用來在 DPM 表現感測器的驅動品系。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認。

## 是什麼

**DPM 是一型廣泛支配整個蕈狀體各葉的大型內在神經元。** Aso 2014a 寫它是血清素性（serotonergic）的 MB-DPM，與 MB-APL 同屬兩型內在神經元，投射不分區室；以 PA-GFP 照整條葉時在同側找到單獨一顆。Tomchik 2009 與 Gervasi 2010 的介紹稱它為「一對」。Tomchik 2009 的討論另提到 DPM「被認為會釋放一種能提高 cAMP 的胜肽」，作為 KC 回饋的假說，該篇沒有檢驗。

## 版本與規模

| 項目 | 數值 | 來源 |
|---|---|---|
| 顆數 | PA-GFP 在照射同側找到 1 顆；介紹中稱「一對」 | Aso 2014a 圖 4；Tomchik 2009、Gervasi 2010 |
| cAMP 成像 n | 每組 5 | Tomchik 2009 圖 4C |
| RNA 定序取樣 | 每重複 56 ± 18 顆（與 APL 同列） | Aso 2019（見 [[numbers]]） |

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | c316 驅動 Epac1-camps，在 α 葉記錄 DPM 神經突對多巴胺與章魚胺的 cAMP 反應（離體腦、給藥劑量反應） | 只在 1 mM 與 10 mM 才有反應；1 mM 時章魚胺大於多巴胺（p ＝ 0.034，n ＝ 5；見 [[numbers]]）。量它的理由是 DPM 支配 KC 軸突、可能回饋給 KC |
| [[s-aso-2014-mb-architecture]] | 解剖普查：PA-GFP 反查蕈狀體葉的輸入、圖 12 的分區矩陣 | 列為兩型內在神經元之一（血清素性），廣泛支配蕈狀體、不分區室；PA-GFP 照整條葉時找到的 8 顆單獨細胞之一 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | 手挑或 FACS 分選 DPM 細胞做 RNA 定序，作為各型細胞表現譜的一部分 | 每重複 56 ± 18 顆；來源頁沒有記錄 DPM 的個別表現結果：？待查 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | [[e-hemibrain]] v1.2.1 分析：KC 每個釋放點的突觸後夥伴 | DPM 是與 M4、M6、α′3 MBON 共用 KC 釋放點的對象之一（圖 10h） |

只提及、未使用的：Hige 2015（作者保留「DPM 等 KC 以外的元件也可能貢獻 MBON 上的突觸變化」的可能）、Gervasi 2010（討論中列舉 DPM 垂直分支的記憶痕跡，支持 α 葉的角色）。

## 已知的問題

- **生理濃度未知。** Tomchik 2009 的 DPM 反應閾值在 mM 級，而該篇沒有估計多巴胺在組織內的實際濃度，所以 DPM 在正常情況下是否受多巴胺調節，回答不了；局部給藥的濃度也不等於組織內濃度（見 [[numbers]]）。
- **傳遞物質的說法不同層次。** Aso 2014a 寫血清素性；Tomchik 2009 的假說是 DPM 釋放提高 cAMP 的胜肽。兩者可以並存（※ 推論：一顆神經元可同時用兩種傳遞物質，庫內 Aso 2019 即為多巴胺神經元共用一氧化氮的例子），但庫內沒有一篇同時檢驗兩者：？待查。不列為矛盾。
- **跨品系幅度不能比。** Tomchik 2009 五個驅動品系表現強度不同、未校正；DPM（c316）的反應幅度只能在同品系內比多巴胺與章魚胺。
- **「可能回饋給 KC」是假說。** Tomchik 2009 用它解釋 *rut¹* 突變中殘餘的 cAMP，論文沒有檢驗；Hige 2015 的保留也只是可能性。

## 相關

- 同類：[[e-apl-neuron]]；蕈狀體：[[e-mushroom-body]]、[[e-kenyon-cell]]
- 概念與工具：[[c-camp-signaling]]、[[e-epac-camp-sensor]]、[[e-rutabaga]]
- 資料：[[e-hemibrain]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-aso-2014-mb-architecture]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-hige-2015-heterosynaptic-plasticity]]（只提及）、[[s-gervasi-2010-pka-dynamics]]（只提及）
- 待開頁面：`e-c316-gal4`、`e-pa-gfp`
