---
title: APL 神經元（anterior paired lateral neuron, MB-APL）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# APL 神經元（anterior paired lateral neuron, MB-APL）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突排成幾條「葉」，每條葉切成一格一格的「區室」（[[e-mushroom-body]]、[[c-mb-compartment]]）。
- **內在神經元（intrinsic neuron）**：Aso 2014a 對「整顆都在蕈狀體內、廣泛支配它」的神經元的分類；APL 與 DPM 屬此類，不分區室。
- **MBON、DAN**：蕈狀體輸出神經元；多巴胺神經元。
- **GABA、膽鹼性**：GABA 是常見的抑制性傳遞物質；膽鹼性＝用乙醯膽鹼，在果蠅中樞多為興奮性。
- **活化比例、稀疏編碼**：一種氣味讓多少比例的 KC 放電；比例小叫稀疏（[[c-sparse-coding]]）。
- **PA-GFP**：照光後才發亮的螢光蛋白，用來從一塊被照亮的區域反查有哪些神經元伸進來。
- **連結體、BANC**：用電子顯微鏡追蹤出的接線圖；BANC 是 Minnick 2026 用的雌果蠅腦＋腹神經索連結體。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認。

## 是什麼

**APL 是一型廣泛支配整個蕈狀體的大型內在神經元，在真果蠅中是 GABA 性（抑制性）的，被認為是把 KC 的氣味編碼壓稀疏的回饋來源。** Aso 2014a 把 MB-APL 與 MB-DPM 列為蕈狀體的兩型內在神經元（GABA 性），在葉內的投射不分區室；以 PA-GFP 照整條葉時，在同側找到單獨一顆 MB-APL。Tomchik 2009 的背景介紹稱它為「一對」。Minnick 2026 的連結體中有兩顆（※ 推論：即左右腦各一顆；來源頁沒有明說兩顆的位置）。

## 版本與規模

| 項目 | 數值 | 來源 |
|---|---|---|
| 顆數 | PA-GFP 在照射同側找到 1 顆；BANC 連結體 2 顆 | Aso 2014a 圖 4；Minnick 2026 |
| 對 KC 的突觸 | 22,926 個（兩顆合計） | Minnick 2026（BANC；見 [[numbers]]） |
| RNA 定序取樣 | 每重複 56 ± 18 顆（與 DPM 同列） | Aso 2019（見 [[numbers]]） |

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-aso-2014-mb-architecture]] | 解剖普查：PA-GFP 反查蕈狀體葉的輸入、圖 12 的分區矩陣 | 列為兩型內在神經元之一（GABA 性），廣泛支配蕈狀體、不分區室；PA-GFP 照整條葉時找到的 8 顆單獨細胞之一 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | 手挑或 FACS 分選 APL 細胞做 RNA 定序，作為各型細胞表現譜的一部分 | 每重複 56 ± 18 顆；來源頁沒有記錄 APL 的個別表現結果：？待查 |
| [[s-minnick-2026-untrained-connectome]] | 全連結體模擬中的一個元件；另做「沉默一顆 APL」的操作 | 兩顆都被自動預測為膽鹼性（興奮性），論文照此使用；沉默帶型別標註的那一顆，KC 活化比例 68% → 61%；一顆無標籤的 APL 經 62 個突觸驅動 MBON05 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | [[e-hemibrain]] v1.2.1 分析：KC 每個釋放點的突觸後夥伴 | APL 是與 M4、M6、α′3 MBON 共用 KC 釋放點的對象之一（圖 10h） |

Tomchik 2009 只在背景介紹提到「APL 學習後有記憶痕跡」（與 DPM、嗅葉等並列，引 Yu et al. 2003–2006、Wang et al. 2008、Liu & Davis 2009 一組文獻），本篇沒有量 APL，不列入表。

## 已知的問題

- **⚠️ Minnick 2026 把它的正負號用反了。** 該篇的連結體中，自動預測欄寫膽鹼性，註記欄卻把 GABA 列為「已驗證」，論文採用預測欄；而 Aso 2014a 與 Tomchik 2009 都寫它是 GABA 性。這是模型輸入的錯誤，不是兩份實驗觀察互相牴觸（詳見 [[s-minnick-2026-untrained-connectome]] 問題與限制 4b；登記於 [[numbers]]）。
- **「沉默 APL」只關了一半。** Minnick 2026 只沉默有標註的那一顆，另一顆照常運作，且正是校正版殘餘 MBON 輸出（MBON05）的來源；也沒有測「把 APL 改成抑制性」，該頁指出後者可能把活化比例壓得更低（※ 推論，見該頁）。
- **「壓稀疏」在庫內沒有直接證據。** 這是 Minnick 2026 與 Tomchik 2009 背景敘述中的公認說法；庫內沒有一篇直接操弄 APL 並量 KC 稀疏度的實驗（Minnick 的沉默是在錯誤正負號下做的模擬）：？待查。
- **單數與複數。** 本庫 [[c-sparse-coding]] 與 Minnick 來源頁的用語表寫「一顆」，Minnick 正文是「兩顆」；以每半腦一顆讀即不衝突（※ 推論）。

## 相關

- 同類：[[e-dpm-neuron]]；蕈狀體：[[e-mushroom-body]]、[[e-kenyon-cell]]
- 概念：[[c-sparse-coding]]
- 資料：[[e-hemibrain]]
- 來源：[[s-aso-2014-mb-architecture]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-minnick-2026-untrained-connectome]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-tomchik-2009-camp-dynamics]]（只提及）
- 待開頁面：`e-banc`、`e-pa-gfp`、`c-connectome-model`
