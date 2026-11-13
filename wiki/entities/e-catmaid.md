---
title: CATMAID 電顯追蹤平台（CATMAID）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# CATMAID 電顯追蹤平台（CATMAID）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **電顯（電子顯微鏡，electron microscopy, EM）**：解析度比光學顯微鏡高得多，看得到單一突觸。把腦切成極薄的連續切片逐張拍攝，再把同一條神經纖維在相鄰切片中一張張連起來，叫「追蹤」或「重建」。
- **連結體（connectome）**：用電顯逐一追蹤神經元、畫出的接線圖，可數出兩顆細胞之間有幾個突觸。
- **FAFB**：一顆成年雌果蠅全腦的連續切片穿透式電顯影像（Zheng et al. 2018）。
- **MBON、MB2ON**：蕈狀體輸出神經元（MBON）；MB2ON 是 Eschbach 2021 對「MBON 下游神經元」的稱呼。
- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造，見 [[e-mushroom-body]]。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認。

## 是什麼

**CATMAID 是一套在網頁上多人協作、在電顯影像中逐條追蹤神經元並標註突觸的軟體。** 它本身不是資料：庫內兩篇用它處理的是兩份不同的電顯影像——成蟲全腦 FAFB 與一隻一齡幼蟲的完整中樞神經系統。兩篇都說明是以 CATMAID 標註或手動重建（Eschbach 2021 寫明「手動重建」）。庫內另一套成蟲連結體 [[e-hemibrain]] 則是經 neuPrint 網站查詢，各篇沒有用 CATMAID 處理它。CATMAID 的全名，庫內兩篇來源都沒有展開：？待查。

## 版本與規模（庫內用到的資料）

| 資料 | 來源 | 內容 |
|---|---|---|
| FAFB（成蟲雌腦） | Felsenberg 2018 | 只追蹤與論點有關的三型 MBON（MVP2、M4β′、M6），不是整腦連結體 |
| 一齡幼蟲完整中樞神經系統 | Eschbach 2021 | 孵化約 6 小時的雌幼蟲，解析度 3.8 × 3.8 × 50 nm，首次發表於 Ohyama et al. 2015 |

CATMAID 的軟體版本，兩篇都沒寫：？待查。

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-felsenberg-2018-memory-extinction]] | 在 FAFB 上以 CATMAID 追蹤 MVP2（即 [[e-mbon-gamma1pedc]]）、M4β′、M6；至少兩位各有超過 500 小時追蹤經驗的審核者校對 | MVP2 → M6 右側 17、左側 16、→ M4β′ 47 個突觸；M6 上的突觸位置靠近樹突根部，兩種連接方式不同 |
| [[s-eschbach-2021-learned-innate-valence-integration]] | 在幼蟲電顯資料上以 CATMAID 手動重建 24 型 MBON 的全部下游；左右兩側對應神經元各自獨立重建，互相比對 | 「可靠連結」定為左右各 ≥ 3 個突觸、合計 ≥ 10 個，得 167 對 MB2ON；引 Schneider-Mizell 2016 的單一突觸偽陽性率 0.0167 |

## 已知的問題

- **追蹤會漏也會錯，數字帶誤差。** Felsenberg 2018 自己給了突觸數的上下界（例如 M4β′ 46–50.8）；該來源頁指出上界的算法約為「× 1.083」而非「÷ 0.917」，差距小於 1 個突觸。MVP2 → M6 左側的突觸數，方法表寫 16、補充圖 S4B 寫 15（⚠️ 該篇自身不一致，見 [[s-felsenberg-2018-memory-extinction]]）。
- **電顯看得到接點，看不到正負號。** 「MVP2 抑制 M4β′／M6」來自 MVP2 是 GABA 能與其他篇的活化實驗，不是 CATMAID 重建本身。
- **幼蟲與成蟲不能直接對照。** Eschbach 2021 的 24 型 MBON 與區室是幼蟲的；它們與成蟲（Felsenberg 2018 的 FAFB、或 [[e-hemibrain]]）的型別如何對應，兩篇都沒有交代（※ 推論：名稱不能直接套用；？待查）。
- **工作量分配不均。** Eschbach 2021 致謝列出重建工作量（Feng Li 9%、Avinash Khandelwal 8% 等），是多人共建，個別神經元由誰校對，論文沒有逐一交代。

## 相關

- 資料集：[[e-hemibrain]]（另一套成蟲連結體）
- 細胞：[[e-mbon]]、[[e-mbon-gamma1pedc]]、[[e-mbon-gamma5beta2a]]
- 主題：[[t-mbon-dan-feedback]]、[[t-innate-learned-integration]]、[[t-memory-updating]]
- 來源：[[s-felsenberg-2018-memory-extinction]]、[[s-eschbach-2021-learned-innate-valence-integration]]
- 待開頁面：`e-fafb`、`e-banc`
