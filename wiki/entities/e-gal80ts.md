---
title: 溫度開關型 GAL4 抑制蛋白（Gal80<sup>ts</sup>）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# 溫度開關型 GAL4 抑制蛋白（Gal80<sup>ts</sup>）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **GAL4／UAS、驅動品系**：果蠅的雙元表現系統。驅動品系（GAL4）決定外加基因在哪些細胞表現，UAS 決定表現什麼（[[e-split-gal4]]）。
- **GAL80**：GAL4 的抑制蛋白。有 GAL80 的細胞裡 GAL4 不作用。
- **RNAi、條件式剔除（cko）、FLP／FRT**：RNAi 降低指定基因的表現量；條件式剔除把基因在選定細胞中整段剪掉，本庫兩篇用的剪刀是翻轉酶 FLP 與它認得的 FRT 標記。
- **蕈狀體、KC、MBON、M4/6**：果蠅腦中把氣味和好壞經驗連起來的構造（[[e-mushroom-body]]）；代表氣味的 Kenyon 細胞；讀出 KC 訊號的輸出神經元；M4/6 是一群「走開」型 MBON 的舊名（見 [[e-vt1211]]）。
- **STM／LTM**：短期記憶（訓練後立刻測）／長期記憶（本庫這兩篇指 24 小時）。
- **PI、LI**：行為分數（[[c-performance-index]]）。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值。

## 是什麼

**Gal80<sup>ts</sup> 是溫度敏感版的 GAL80：低溫時它壓住 GAL4，把 GAL4 驅動的操作整個關掉；移到高溫它失效，操作才開始。** 它的用途是把基因操作限制在果蠅生命的某一段（通常是成蟲期），用來排除「從發育期就缺少這個基因」造成的腦部缺陷。庫內兩篇用它，兩篇都是拿它當**對照實驗**：主結果用的是全程作用的操作，Gal80<sup>ts</sup> 那一組只是回答「主結果會不會其實是發育缺陷」。

**不要和空間用的 GAL80 混為一談。** 庫內另有幾篇用不帶溫度開關的 GAL80 在空間上扣掉某群細胞（[[s-burke-2012-octopamine-dopamine-reward]] 與 [[s-felsenberg-2017-re-evaluation]] 的 `c061-GAL4;MBGAL80`＝用 c061 標記但擋掉蕈狀體內的表現；[[s-aso-2014-mb-architecture]] 的 MB247-GAL80、R58E02-GAL80）。那是「哪些細胞」的工具，不是「哪一段時間」的工具。

## 版本與規模（庫內兩篇的溫度與時段）

| 來源 | 壓住（低溫） | 放開（高溫） | 誘發時長 | 對照 |
|---|---|---|---|---|
| Pribbenow 2022 | 18–20 °C | 32 °C | 實驗前 3–5 天 | 全程 18–20 °C 的溫度對照（圖 2 補 2a–d，本庫未取得） |
| Kaldun 2025 | 18 °C 養到羽化 | 30 °C | 羽化後 5–7 天，第 5 天訓練、隨即測驗 | 該頁未寫（相關圖在本庫未取得的補充資料裡） |

Kaldun 2025 說明了為什麼要等這麼久：**受體的半衰期沒有人量過**，基因被剪掉之後細胞裡既有的蛋白還要多久才降解完，無法確定；既然等待時間拿不準，作者就在同一批果蠅上同時測了嫌惡 STM 與 LTM。

## 庫內誰用了它

| 來源 | 用來做什麼 | 得到什麼 |
|---|---|---|
| [[s-pribbenow-2022-postsynaptic-plasticity]] | 配 [[e-vt1211]]，只在成蟲期最後 3–5 天在 M4/6 降低 α5（立即與 3 小時）、α2（3 小時）、Dlg（3 小時） | 四組缺陷都重現（圖 2e–h）：實驗組 PI 約 0.08–0.17，兩個對照組約 0.30–0.40（※ 從圖判讀）。作者據此說受體的需求不是發育造成的 |
| [[s-kaldun-2025-dop1r2-memory-phases]] | 把 Dop1R2 的條件式剔除（[[e-dopamine-receptor]]）推遲到羽化之後，只做全蕈狀體（[[e-ok107-gal4]]）這一組 | 嫌惡 STM 仍正常、嫌惡 LTM 仍顯著受損（Figure 4—figure supplement 3）。**該圖在本庫未取得的補充資料裡，來源頁只能轉述、標 ？待查** |

數值見 [[numbers]]。

## 已知的問題

- **庫內只有兩篇用它，而其中一篇的圖本庫看不到。** [[s-kaldun-2025-dop1r2-memory-phases]] 的 Gal80<sup>ts</sup> 結果只有正文的轉述，數值與統計都在未取得的補充圖裡（該頁標 ？待查）。本頁的門檻因此是「兩篇都做了這個實驗」，不是「兩篇都有可查的數字」。
- **這組對照的覆蓋面很窄。** [[s-kaldun-2025-dop1r2-memory-phases]] 只做了全蕈狀體、只做了嫌惡的 STM 與 LTM；三條葉與獎賞訓練都沒有做。
- **「限制在成蟲期」不等於「只在訓練時」。** 兩篇的誘發都長達 3–7 天，時間解析度是天，不是分鐘。要只在訓練那幾分鐘操弄，得換 [[e-shibire-ts]] 或 [[e-cschrimson]] 這類工具。
- **抑制是否完全、放開是否完全，兩篇都沒有直接驗證**（例如量操作後蛋白真的減少多少）：？待查。
- **溫度本身是一種干擾。** 32 °C 或 30 °C 既是開關，也改變果蠅的整體狀態；Pribbenow 2022 有全程低溫的溫度對照，Kaldun 2025 的來源頁沒有寫出對應的對照：？待查。

## 相關

- 品系與工具：[[e-split-gal4]]、[[e-vt1211]]、[[e-ok107-gal4]]、[[e-shibire-ts]]、[[e-cschrimson]]
- 受體與基因：[[e-dopamine-receptor]]
- 概念：[[c-appetitive-memory]]、[[c-memory-consolidation]]、[[c-performance-index]]
- 來源：[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-kaldun-2025-dop1r2-memory-phases]]；只用非溫度型 GAL80 者：[[s-burke-2012-octopamine-dopamine-reward]]、[[s-felsenberg-2017-re-evaluation]]、[[s-aso-2014-mb-architecture]]
- 待開頁面：`c-conditional-knockout`、`e-mb011b`、`e-nachr`、`e-dlg`
