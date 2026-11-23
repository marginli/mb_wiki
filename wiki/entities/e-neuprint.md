---
title: neuPrint 連結體查詢介面（neuPrint）
created: 2026-11-24
updated: 2026-11-24
tags: [entity, active, cross-domain]
confidence: medium
---

# neuPrint 連結體查詢介面（neuPrint）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **連結體（connectome）**：用電子顯微鏡（電顯）逐一追蹤神經元、畫出的接線圖，可數出兩顆細胞之間有幾個突觸。
- **hemibrain**：一隻成年雌果蠅半邊中央腦的電顯緻密重建，是本庫各篇經 neuPrint 查到的那份資料集。見 [[e-hemibrain]]。
- **Neo4J 圖資料庫**：以「節點＋邊」儲存資料的資料庫，neuPrint 的後端（[[s-li-2020-mb-connectome]] 「本頁用語」）。
- **neuprint-python／neuprintr**：從 Python 或 R 程式查詢 neuPrint 的套件。
- **Traced**：neuPrint 給每顆神經元的追蹤狀態欄位；庫內兩篇以「只取 Traced」當排除規則。
- **標記**：`※ 推論`＝本庫推得、原文沒明說；`？待查`＝要靠其他資料確認。

## 是什麼

**neuPrint（<https://neuprint.janelia.org>）是查詢 hemibrain 的網頁介面，後端是一個 Neo4J 圖資料庫。** 庫內五篇的連結數字都是經它取得的，但五篇用的是三種不同的入口：網頁介面本身、R 的 `neuprintr`、Python 的 `neuprint-python`。

**這一頁只寫介面層，不寫資料集。** 資料集涵蓋哪半邊腦、哪些腦區沒重建、各篇用了哪個版本、重建完整度如何，全部寫在 [[e-hemibrain]]；這一頁寫的是「怎麼問」以及「問法本身強加了什麼」——欄位、門檻、版本標籤、命名的壽命。兩頁要查的是不同的問題：**一個數字對不對，先問資料集；兩個數字能不能比，先問介面。**

[[s-li-2020-mb-connectome]] 的資料庫欄另記下了 neuPrint 的保存承諾：**hemibrain:v1.1 該版本永久保留、整個服務至少維持 10 年，底層資料為 CC-BY，並提供把全部或部分資料複製到自己電腦的程序；登入用任何 Google 帳號。**

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-li-2020-mb-connectome]] | hemibrain:v1.1。骨架用 R natverse 下載（`neuprintr::neuprint_read_neurons` 或 `hemibrainr`），連結表用 `neuprintr::neuprint_connection_table`，**只取右半腦**；**只用狀態為 Traced 的具名神經元**，有 ID 但不接任何具名神經元的 small fragments 全部排除 | 整篇蕈狀體連結體分析的資料底；1,927 顆 KC、34 型 MBON、40 個 DAN 亞型都由這些查詢產生 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | v1.2.1，`neuprint-python`；**只取狀態為 Traced 的 KC**，限接到 M4、M6、α′3 三型 MBON 者 | 每個 KC 釋放點的突觸後夥伴數眾數 3–4 個 |
| [[s-yamada-2023-second-order-conditioning]] | 連結資料取自 neuPrint 的 hemibrain（另給資料集 DOI 10.25378/janelia.12818645.v1，**未寫版本號**），只用右半腦，理由是左半腦重建不完整 | MBON-α1 →（SMP353／SMP354）→ SMP108 → 多型獎賞 DAN 的兩跳路徑；並以 hemibrain 的型別細胞總數當品系涵蓋率的分母 |
| [[s-aso-2023-upwind-neurons]] | 連結體取自 neuPrint 的 hemibrain（只用右半腦），**版本號未寫**；以 [[e-mcfo]] 單細胞影像比對找出品系標到的細胞 | SS33917 對到 11 顆、5 型；MBON-α1 → SMP354 共 268 個突觸 |
| [[s-ganguly-2024-visual-inputs-to-kc]] | `neuprint-python` 0.4.25；neuPrint 只當**第二個入口**，主資料來自 FlyWire 的 Codex | 把 FlyWire 的 VPN／LVIN 以 NBLAST 對 hemibrain 全庫比對，檢查主要視覺輸入在第二隻腦裡是不是同一批（見 [[e-nblast]]） |

各篇引用的數字見 [[numbers]]。

## 引用時的陷阱

1. **「取自 neuPrint」不是出處，版本才是。** 五篇裡只有兩篇寫出版本（v1.1、v1.2.1），兩篇完全沒寫、一篇只給資料集 DOI。**版本是 neuPrint 這一側的標籤，論文不寫就追不回去**，不同版本的突觸數是否可比，庫內沒有來源說過：`？待查`。
2. **`Traced` 是介面給的欄位，不是生物學分類。** [[s-li-2020-mb-connectome]] 與 [[s-pribbenow-2022-postsynaptic-plasticity]] 都拿它當排除規則，而排除「追蹤未完成」只會往下壓夥伴數，不會往上（`※ 推論`：重建不完整只會漏算；兩篇都沒有討論這個方向）。
3. **型名會改，細胞 ID 不會。** [[s-li-2020-mb-connectome]] 的方法節自己說明了為什麼每顆神經元要有一個永久的數字 ID（一般 8–10 位數）：**細胞型的指派預期會隨新的生物學資訊不斷更新**。所以「SMP354」這種型名在跨論文比對時要連版本一起引，ID 才是穩定的鍵。
4. **同一個介面可以被當主資料、也可以被當對照，而兩者的證據強度不同。** [[s-ganguly-2024-visual-inputs-to-kc]] 用它只是為了在第二隻腦上覆核，主資料在別處；把這種用法引成「該篇用 hemibrain 做的」會高估它。
5. **查詢要 Google 帳號登入。** 資料是 CC-BY、也提供離線複製的程序，但網頁查詢本身不是匿名的（[[s-li-2020-mb-connectome]] 資料庫欄）。**要重跑一篇論文的查詢，先確認自己拿得到的是哪一版的離線副本。**

## 相關

- 資料集本身：[[e-hemibrain]]（範圍、版本與重建完整度寫在那裡，不在這頁）
- 另一份體積與它的追蹤平台：[[e-fafb]]、[[e-catmaid]]
- 方法：[[e-nblast]]、[[c-neurotransmitter-prediction]]
- 細胞：[[e-kenyon-cell]]、[[e-mbon]]、[[e-dopaminergic-neuron]]
- 來源：[[s-li-2020-mb-connectome]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-yamada-2023-second-order-conditioning]]、[[s-aso-2023-upwind-neurons]]、[[s-ganguly-2024-visual-inputs-to-kc]]
- 待開頁面：`e-flywire`（FlyWire 全腦連結體）、`e-codex`（FlyWire 的查詢介面，與 neuPrint 平行）、`e-natverse`（natverse／`neuprintr` 工具組）
