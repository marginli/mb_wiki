---
title: cAMP 訊號（cAMP signaling）
created: 2026-10-25
updated: 2026-10-25
tags: [concept, active, mb-learning]
confidence: medium
---

# cAMP 訊號（cAMP signaling）

**cAMP（環腺苷酸，cyclic AMP）是細胞內的第二傳訊者（second messenger）：細胞表面的受體接到外來訊號（例如多巴胺）後，由腺苷酸環化酶（adenylyl cyclase, AC）在細胞裡製造的小分子，再由它去啟動下游的蛋白。** 本庫關心的是 Kenyon 細胞（KC）軸突裡的 cAMP 如何被多巴胺與 KC 自身活動共同推高，以及它推動突觸往哪個方向改變。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **KC**：Kenyon 細胞（Kenyon cell），蘑菇體（mushroom body，果蠅腦中把氣味和好壞連起來的構造）裡代表氣味的神經元，每種氣味只活化一小群。
- **DAN**：多巴胺神經元（dopaminergic neuron），送出代表懲罰或獎賞的多巴胺。依 Handler 2019 的說法，PAM 群多報告獎賞、PPL（PPL1）群多報告懲罰。
- **MBON**：蘑菇體輸出神經元（MB output neuron），接收 KC 的訊號，推動果蠅靠近或走開。
- **葉、萼部**：KC 的軸突（送出訊號的長枝）成束排成 α、α′、γ 等「葉」（lobe）；KC 的樹突（接收端）聚在「萼部」（calyx）。
- **區室**：葉沿長度切成的一格，以 γ1pedc、γ2、γ4、α2 等編號命名；細胞也以所在區室命名，例如 MBON-γ1pedc、PPL1-γ1pedc。詳見 [[c-mb-compartment]]。
- **章魚胺**（octopamine）：昆蟲腦中類似腎上腺素的物質，Tomchik 2009 當時被認為傳遞獎賞，所以拿來和多巴胺對照。
- **forskolin**：直接活化製造 cAMP 的酵素的藥，用來人為拉高 cAMP。
- **ΔR/R、ΔF/F**：螢光感測器的訊號（兩色亮度比值，或亮度）相對刺激前基線的變化比例，例如 0.15＝高了 15%。只能在同一實驗內比大小。
- **rut¹、238Y、c739、MB320C 等**：*rut¹* 是 *rutabaga* 基因的一個突變版本；其餘是「驅動品系」代號，即決定外加基因只在哪些細胞表現的果蠅品系。
- **−/−**：該基因兩份都被剔除。
- **DopR1、DopR2、內質網鈣**：KC 上兩種多巴胺受體。DopR1 接上製造 cAMP 的路徑；DopR2 接上讓內質網（細胞內存鈣的小倉庫）放出鈣的路徑，所以量內質網鈣就是在看 DopR2 路徑有沒有啟動。

## 怎麼算 / 怎麼判定

兩篇都用遺傳編碼的 FRET 感測器（[[e-epac-camp-sensor]]）：感測器帶青、黃兩種螢光蛋白，cAMP 結合後兩色亮度比改變，讀「比值相對基線的變化」。

- Tomchik 2009：Epac1-camps，共軛焦成像，記為 ΔR/R0（R0＝刺激前的基線比值，與 ΔR/R 意思相同；CFP 為青色、YFP 為黃色螢光蛋白）；在葉部末端或萼部劃範圍量。
- Handler 2019：EPAC，雙光子 850 nm 激發，記為 ΔR/R；在 γ4/γ5 區室量，取多巴胺神經元活化後 4 s 的平均。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | 浴灌多巴胺／章魚胺的劑量反應；乙醯膽鹼＋多巴胺配對的協同；用 forskolin（直接活化 AC 的藥）拉高 cAMP | 浴灌多巴胺的最大 cAMP 反應約 11.9 ± 1.3% ΔR/R0（forskolin 可讓同一感測器讀到約 40%，表示 11.9% 不是感測器的上限）；配對比相加多約五成，*rut¹* 中消失；cAMP 拉高後 KC 對同樣刺激的鈣反應（神經元被激發時細胞內鈣上升，常用作活動的指標）變大（α 葉約 3.2 倍），作者視為 KC 變得更容易被激起 |
| [[s-handler-2019-dopamine-receptor-timing]] | 不同時間差下的 cAMP；剔除受體 DopR1、DopR2 | 六個時間差都有 cAMP，0 s 最高；DopR1−/− 降到野生型約 27%，DopR2−/− 不變 → cAMP 主要走 DopR1；cAMP 被歸為推動突觸**減弱**的一方 |

> 數值見 [[numbers]]。**Hige 2015 只提到**：討論中引 Boto et al. 2014（cAMP 上升侷限在被活化 DAN 支配的區室）與「遺傳證據顯示 cAMP 是蘑菇體可塑性誘發的核心」，本身沒有量或操作 cAMP。
>
> **2015–2018 新收的五篇都沒有量或操作 cAMP**（Cohn 2015 grep `cAMP|PKA|rutabaga` 無結果；Ichinose 2015 只在背景引 *rutabaga*；Felsenberg 2018 引言轉述 Schwaerzel et al. 2002 的「消退在 KC 內對抗 cAMP 訊號」，並主張自己的結果是細胞之間而非細胞內的拮抗）。cAMP 上游受體 DopR1 的用法見 [[e-dopamine-receptor]]。

## 引用時的陷阱

1. **兩篇的數字不能直接比大小。** 都是比值變化，但感測器版本、驅動品系、顯微鏡、讀法不同；連 Tomchik 2009 自己不同遺傳背景的圖之間，多巴胺的最大反應都不同（約 11.9% vs 約 8.5%）。
2. **cAMP 能否分辨先後，兩篇說法不同。** Tomchik 2009 看的是「協同」，只在順向出現；Handler 2019 看的是 cAMP 本身，兩種順序都有（在圖 5E 與圖 6B 野生型這兩批資料中，順向都比逆向高約 28–36%，論文未檢定，稱「相當」）。見 [[syn-contradictions]] 1.2，不在本頁裁決。
3. **cAMP 的「方向」量在不同位置。** Tomchik 2009：cAMP 上升讓 KC **內部**的鈣反應變大；Handler 2019：DopR1–cAMP 路徑讓 KC→MBON **突觸**變弱。兩者不是同一個量，方向看似相反不等於矛盾，見 [[c-kc-mbon-plasticity]]。
4. **殘留的 cAMP 來源不明。** Tomchik 2009 的 *rut¹* 突變果蠅單獨給多巴胺時，cAMP 照樣上升、與對照組無差異，所以 *rut* 之外還有來源（作者推測是其他 AC）；Handler 2019 的 DopR1−/− 仍有約 27%，論文未討論來源。

## 相關

- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]
- 概念：[[c-coincidence-detection]]、[[c-kc-mbon-plasticity]]、[[c-mb-compartment]]
- 實體：[[e-epac-camp-sensor]]、[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]、[[e-dopamine-receptor]]
- 綜述：[[syn-contradictions]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-hige-2015-heterosynaptic-plasticity]]
