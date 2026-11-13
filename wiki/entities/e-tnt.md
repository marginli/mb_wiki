---
title: 破傷風毒素輕鏈（TNT / TeNT / TnT / TNTe）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# 破傷風毒素輕鏈（TNT / TeNT / TnT / TNTe）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **驅動品系（driver line）**：讓外加基因只在選定神經元表現的果蠅品系。split-GAL4 把 GAL4 拆成兩半，兩半都在的細胞才有作用（[[e-split-gal4]]）；「empty-split」是不標任何細胞、但帶著同樣轉殖基因的對照品系。
- **蕈狀體、KC、MBON、DAN、PAM**：果蠅腦中把氣味和好壞經驗連起來的構造（[[e-mushroom-body]]）；代表氣味的 Kenyon 細胞（[[e-kenyon-cell]]）；讀出 KC 訊號的輸出神經元（[[e-mbon]]）；送出獎賞或懲罰訊號的多巴胺神經元，PAM 群多傳獎賞（[[e-dopaminergic-neuron]]）。
- **側角（lateral horn, LH）**：嗅覺的另一條下游，與天生的好惡有關。
- **UpWiN、SMP108**：[[s-aso-2023-upwind-neurons]] 的「迎風神經元」；[[s-yamada-2023-second-order-conditioning]] 在二階制約中居間的一型中間神經元。
- **一階／二階制約**：先讓氣味 S1 配糖；之後讓新氣味 S2 配已經有意義的 S1，果蠅就對 S2 也有偏好（[[c-second-order-conditioning]]）。
- **ΔF/F0、PI**：螢光相對基線的變化比例；行為分數（[[c-performance-index]]）。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值。

## 是什麼

**破傷風毒素輕鏈讓表現它的神經元放不出神經傳遞物質。** 它由驅動品系送進選定的細胞，而且**從發育期起一直作用**——這一點是它與 [[e-shibire-ts]] 的根本差別：shibire 可以只在某一段時間（訓練、測驗、再聞氣味）關掉細胞，TNT 不能。庫內四篇用它，寫法各不相同：TNT（Aso 2023、Yamada 2023，該篇也寫 TeNT）、TnT（Huang 2024）、TNTe（Eschbach 2021，幼蟲）。

**庫內有一篇寫下了「為什麼只能用它」**：[[s-yamada-2023-second-order-conditioning]] 想用 shibire<sup>ts1</sup> 只在二階制約期間關掉 SMP108，但在 32 °C 的限制溫度下，連對照基因型的果蠅都很快把一階記憶消退掉、做不成二階制約（正文寫 data not shown），所以阻斷只能用 TNT。

## 版本與規模（庫內各篇的用量）

| 來源 | 寫法 | 關掉哪些細胞（品系） | 對照 |
|---|---|---|---|
| Aso 2023 | TNT | UpWiN（SS33917） | SS33917/+ 與 empty-split/TNT 兩組 |
| Yamada 2023 | TNT、TeNT | SMP108（SS67221、SS45234）；PAM-α1（MB043C）；γ4、γ4<γ1γ2、γ5、β′2a 的 PAM（MB196B，約 27 顆／半腦） | 各品系的 /+ 對照與 empty-split＋TNT |
| Huang 2024 | TnT | MBON-α3（MB093C）；MBON-γ1pedc>α/β（MB085C） | 該頁未逐一列出：？待查 |
| Eschbach 2021（幼蟲） | TNTe | KC | 同篇另用 Kir2.1（慢性抑制）與 GtACR2（急性抑制） |

各篇用的 TNT 轉殖基因版本與插入位置，來源頁都沒有記錄：？待查。

## 庫內誰用了它

| 來源 | 用來做什麼 | 得到什麼 |
|---|---|---|
| [[s-aso-2023-upwind-neurons]] | 關掉 UpWiN，真糖訓練、一天後測迎風（圖 7A–B） | PA 為 CS+ 時迎風約：SS33917/+ 0.17、Empty/TNT 0.25、SS33917/TNT 0.12；EL 為 CS+ 時約 0.21、0.24、0.13；對 CS− 三組無差異（※ 從圖判讀）。記憶驅動的迎風被**削弱**而非消除（阻斷組對 CS+ 約 0.12 仍高於 CS− 約 0.05） |
| [[s-yamada-2023-second-order-conditioning]] | 關掉 SMP108，測二階記憶（圖 7） | 二階記憶由 SS67221/+ 約 0.53 降到約 0.35、由 SS45234/+ 約 0.60 降到約 0.33（empty-split＋TNT 約 0.51；N＝10–12）；**一階記憶完全不受影響**。拿論文的數字回推，阻斷後仍保有約 54–69% |
| [[s-yamada-2023-second-order-conditioning]] | 關掉 PAM-α1 或 MB196B 標的 PAM（圖 2D） | 關掉 PAM-α1：一天後 S1 偏好約 0.50（對照 0.81）、二階記憶約 0.19（對照 0.43）；關掉 MB196B：二階記憶降到約 0.25 但 S1 偏好不變 |
| [[s-huang-2024-dopamine-memory-dynamics]] | 關掉 MBON-α3 的輸出（MB093C） | 5 分鐘記憶正常、3 小時記憶消失（延伸圖 7d–e，每組 10 隻） |
| [[s-huang-2024-dopamine-memory-dynamics]] | 關掉 MBON-γ1pedc>α/β 的回饋（MB085C），量 PPL1-α3（圖 4i–j） | 阻斷組的 PPL1-α3 對兩種吸引氣味都只有輕微上升、訓練前後不變、bias 不顯著；對照組重現了「對 CS+ 由降轉升」 |
| [[s-eschbach-2021-learned-innate-valence-integration]] | 幼蟲中關掉 KC，看 MBON-m1 還剩多少氣味反應 | 對乙酸乙酯仍顯著上升，約 0.72 ΔF/F₀（n＝6，※）——MBON-m1 的氣味輸入不只來自蕈狀體，也來自側角（見 [[t-innate-learned-integration]]） |

數值見 [[numbers]]。

## 已知的問題

- **從發育期起就阻斷。** 四篇都寫了這一點。所以「關掉之後某個行為變差」不能排除發育異常或長期代償；也不能把效果歸給「訓練那一刻的傳遞」。
- **常常只是削弱，不是消除。** [[s-aso-2023-upwind-neurons]] 的迎風少了約三成到五成（看和哪個對照比）；[[s-yamada-2023-second-order-conditioning]] 的二階記憶少了三到四成半，摘要卻寫 essential、標題寫 a single key interneuron。引用時要看數字，不要只看形容詞。
- **對照之間本身就有差距。** Aso 2023 的兩個對照組差約 0.08（0.17 vs 0.25），阻斷組對前者只有 `*`、對後者 `****`；Yamada 2023 的兩個品系對照值 0.53 與 0.60 也不同，且都高於 empty-split＋TNT 的 0.51。**比較要看配對的那一條，不要跨組比絕對值。**
- **阻斷改變的不只是訓練後的那一段。** [[s-huang-2024-dopamine-memory-dynamics]] 圖 4i 的阻斷組，連訓練**前**對吸引氣味的下降都不見了（Pre 約 0，對照約 −5），所以「訓練後沒有上升」有一部分是起點就不同。
- **無法做時間控制，是被逼出來的選擇。** [[s-yamada-2023-second-order-conditioning]] 試過 shibire<sup>ts1</sup>，因為 32 °C 下對照組的一階記憶迅速消退而做不成（見「是什麼」）。[[s-aso-2023-upwind-neurons]] 的 shibire 實驗則有另一個問題：限制溫度下連對照組都不迎風，所以「測驗時需要 UpWiN 才能迎風」沒有被檢驗。
- **阻斷是否完全，四篇都沒有直接驗證**（例如量傳遞物質釋放減少多少）：？待查。

## 相關

- 工具：[[e-shibire-ts]]（可限時的阻斷）、[[e-cschrimson]]、[[e-split-gal4]]、[[e-gcamp]]
- 細胞：[[e-mbon-alpha3]]、[[e-mbon-gamma1pedc]]、[[e-pam-alpha1]]、[[e-kenyon-cell]]、[[e-mbon]]
- 概念：[[c-second-order-conditioning]]、[[c-appetitive-memory]]、[[c-valence-coding]]
- 主題：[[t-mbon-to-action]]、[[t-innate-learned-integration]]、[[t-mbon-dan-feedback]]
- 來源：[[s-aso-2023-upwind-neurons]]、[[s-yamada-2023-second-order-conditioning]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-eschbach-2021-learned-innate-valence-integration]]
- 待開頁面：`e-smp108`、`e-upwind-neurons`、`e-kir2-1`、`e-gtacr2`、`e-mb043c`、`e-mb196b`
