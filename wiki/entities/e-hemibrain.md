---
title: hemibrain 連結體資料集（hemibrain）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# hemibrain 連結體資料集（hemibrain）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **連結體（connectome）**：用電子顯微鏡（電顯）逐一追蹤神經元、畫出的接線圖，可數出兩顆細胞之間有幾個突觸。
- **neuPrint、neuprint-python**：neuPrint 是查詢 hemibrain 的網站；neuprint-python 是從程式查詢它的工具。
- **KC、MBON、DAN**：蕈狀體（mushroom body）裡代表氣味的 Kenyon 細胞；讀出 KC 訊號的輸出神經元；送出多巴胺、代表獎賞或懲罰的多巴胺神經元（PAM 群多為獎賞、PPL1 群多為懲罰）。見 [[e-kenyon-cell]]、[[e-mbon]]、[[e-dopaminergic-neuron]]。
- **區室（compartment）**：KC 軸突排成的幾條「葉」沿長度切成的一格一格，例如 α1、γ1pedc；細胞以所在區室命名（[[c-mb-compartment]]）。
- **型名（例如 SMP354）、編號（例如 MBON07）**：hemibrain 的型名多以所在腦區開頭（SMP＝上內側前大腦）；MBON07、PAM11 這類是它給的編號，Yamada 2023 對照為 MBON07＝MBON-α1、PAM11＝PAM-α1。
- **傳遞物質預測**：用訓練好的神經網路，從突觸的電顯影像判斷它用哪一種神經傳遞物質。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值。

## 是什麼

**hemibrain 是一份以電顯重建的成年果蠅半腦連結體（Scheffer et al. 2020），經 neuPrint 網站查詢。** 庫內五篇用它：兩篇模型拿它定接線或分區，三篇拿它找實驗中的細胞彼此怎麼接。它只涵蓋半邊中央腦（Minnick 2026 的說明），而且庫內兩篇（Aso 2023、Yamada 2023）只用右半腦，Yamada 2023 的理由是左半腦重建不完整。Aso 2014a 寫成時它還不存在，該篇來源頁只在限制中提到「要到 2020 年的 hemibrain 才能回答哪些重疊是真突觸」，沒有使用。

## 版本與規模

| 來源 | 寫明的版本 | 用到的範圍 |
|---|---|---|
| Huang 2024 | v1.2.1 | γ1、α2、α3 三個模組的九神經元接線 |
| Pribbenow 2022 | v1.2.1（neuprint-python） | 只取狀態為 Traced 的 KC，接到 M4、M6、α′3 三型 MBON 者 |
| Yamada 2023 | 只給資料集 DOI 10.25378/janelia.12818645.v1，未寫版本號 | 右半腦；396 型中間神經元（與 MBON 及 DAN 合計至少 100 個突觸） |
| Aso 2023 | 未寫（該頁標 ？待查） | 右半腦；與 UpWiN 任一顆有 ≥ 20 個連結的上下游 |
| Minnick 2026 | 未寫 | 只用它的區室對應表；模擬本身跑的是另一份連結體 BANC |

整份資料集有多少神經元、多少突觸，庫內沒有任何來源頁寫出：？待查。各篇引用的數字見 [[numbers]]（Pribbenow 2022、Aso 2023、Yamada 2023、Minnick 2026 各節）。

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-huang-2024-dopamine-memory-dynamics]] | 依 v1.2.1 定模型接線，兩神經元間少於 5 個突觸設為 0；非零權重全由擬合決定，不參考突觸數 | 接線顯示 γ1pedc 的 MBON 有一條抑制性連線接到 α3 的 DAN，作者據此推論並檢驗「訓練後它放鬆對 α3 DAN 的抑制」 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | v1.2.1，對每個接到 M4、M6、α′3 MBON 的 KC 釋放點，數它同時接到幾個突觸後對象 | 眾數 3–4 個，比例約 0.30–0.35（※ 從圖判讀）；共同接收者含其他 KC、MBON、DAN、[[e-apl-neuron]] 與 [[e-dpm-neuron]] |
| [[s-yamada-2023-second-order-conditioning]] | 右半腦查 MBON-α1 到 DAN 的兩跳路徑，配合傳遞物質預測；並以 hemibrain 的型別細胞總數當作品系涵蓋率的分母 | 主路 MBON-α1 →（SMP353／SMP354）→ SMP108 → 多型獎賞 DAN，兩層都是乙醯膽鹼性；品系標到的細胞數對 hemibrain 總數：α1 5／7、γ5＋β′2a 16／30、β1＋β2 12／22、γ4 11／23 |
| [[s-aso-2023-upwind-neurons]] | 以 MCFO 單細胞影像（[[e-mcfo]]）比對 hemibrain 神經元，找出品系 SS33917 標到的細胞並查其上下游 | 對到 11 顆、5 型：SMP353（1）、SMP354（3）、SLP400（3）、SLP399（2）、SMP348（2）；MBON-α1 → SMP354 共 268 個突觸 |
| [[s-minnick-2026-untrained-connectome]] | 借用 hemibrain 的區室圖，決定 BANC 模型中哪些 KC→MBON 連結可塑 | 可塑的是嫌惡區室的 8,377 條（MBON11–14、16–20、23、25、28、30、32–35，共 50 顆） |

## 已知的問題

- **只用右半腦。** Yamada 2023 的 SMP108 左右各一顆、軸突跨到對側（圖 4E、F），但連結數只取自右半腦，跨側輸入在資料裡看不到；行為與生理實驗卻是雙側的腦。
- **只取 Traced 的細胞會低估。** Pribbenow 2022 排除未完成追蹤的 KC，夥伴數可能偏低（※ 推論：重建不完整只會漏算，不會多算；該篇未討論）。
- **拿 A 資料集的分區表標 B 資料集。** Minnick 2026 用 hemibrain 區室圖選 BANC 的可塑連結，兩者型別是否一一吻合，該篇沒有交代：？待查。
- **接線不等於權重。** Huang 2024 只用 hemibrain 決定「接不接」，強弱全靠擬合；不能把該模型的權重讀成突觸數的結果。
- **型別細胞數當分母要小心。** Yamada 2023 的「5／7」是本庫推論的讀法（※ 推論，見該頁）：品系標到 5 顆、hemibrain 該型共 7 顆。
- **版本不一。** 五篇中只有兩篇寫明 v1.2.1；其餘三篇的突觸數無法確定與 v1.2.1 可比。

## 相關

- 另一套連結體與工具：[[e-catmaid]]（FAFB 與幼蟲電顯的追蹤平台）、[[e-mcfo]]
- 細胞：[[e-mbon-alpha1]]、[[e-mbon-gamma1pedc]]、[[e-kenyon-cell]]、[[e-apl-neuron]]、[[e-dpm-neuron]]
- 概念：[[c-second-order-conditioning]]、[[c-sparse-coding]]
- 主題：[[t-mbon-dan-feedback]]、[[t-mbon-to-action]]
- 來源：[[s-huang-2024-dopamine-memory-dynamics]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-yamada-2023-second-order-conditioning]]、[[s-aso-2023-upwind-neurons]]、[[s-minnick-2026-untrained-connectome]]、[[s-aso-2014-mb-architecture]]（只提及）
- 待開頁面：`e-banc`、`e-flywire`、`e-fafb`、`e-neuprint`、`c-neurotransmitter-prediction`
