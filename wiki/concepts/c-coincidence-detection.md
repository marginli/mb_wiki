---
title: 巧合偵測（coincidence detection）
created: 2026-10-25
updated: 2026-10-26
tags: [concept, active, mb-learning]
confidence: medium
---

# 巧合偵測（coincidence detection）

**一個分子或細胞，只在兩個輸入差不多同時到達時才給出特別大的反應，叫巧合偵測。** 本庫指的是 Kenyon 細胞（Kenyon cell, KC；蘑菇體裡代表氣味的神經元）的軸突同時收到「氣味讓 KC 活動」與「多巴胺」兩個訊號時，細胞內的 cAMP（環腺苷酸，受體被活化後在細胞內產生、再去啟動下游蛋白的訊號分子，見 [[c-camp-signaling]]）額外增加。這被視為「氣味＋懲罰才留下記憶」在分子層的開關。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **KC**：Kenyon 細胞（Kenyon cell），蘑菇體（mushroom body，果蠅腦中把氣味和好壞連起來的構造）裡代表氣味的神經元，每種氣味只活化一小群。
- **DAN**：多巴胺神經元（dopaminergic neuron），送出代表懲罰或獎賞的多巴胺。依 Handler 2019 的說法，PAM 群多報告獎賞、PPL（PPL1）群多報告懲罰。
- **葉、萼部**：KC 的軸突（送出訊號的長枝）成束排成 α、α′、γ 等「葉」（lobe）；KC 的樹突（接收端）聚在「萼部」（calyx）。
- **乙醯膽鹼**（acetylcholine）：嗅覺訊號傳給 KC 時用的化學物質；在取出的腦上噴它，等於「假裝聞到氣味」。
- **章魚胺**（octopamine）：昆蟲腦中類似腎上腺素的物質，Tomchik 2009 當時被認為傳遞獎賞，所以拿來和多巴胺對照。
- **ΔR/R、ΔF/F**：螢光感測器的訊號（兩色亮度比值，或亮度）相對刺激前基線的變化比例，例如 0.15＝高了 15%。只能在同一實驗內比大小。
- **rut¹、238Y、c739、MB320C 等**：*rut¹* 是 *rutabaga* 基因（[[e-rutabaga]]）的一個突變版本；其餘是「驅動品系」代號，即決定外加基因只在哪些細胞表現的果蠅品系。
- **DopR1、DopR2、內質網鈣**：KC 上兩種多巴胺受體。DopR1 接上製造 cAMP 的路徑；DopR2 接上讓內質網（細胞內存鈣的小倉庫）放出鈣的路徑，所以量內質網鈣就是在看 DopR2 路徑有沒有啟動。

## 怎麼算 / 怎麼判定

本庫有兩種操作型定義，**判準不同**：

- **Tomchik 2009：配對 vs 單獨相加。** 同一顆腦分別量「單獨乙醯膽鹼（代表氣味讓 KC 活動）」「單獨多巴胺」「兩者配對（乙醯膽鹼先 1 秒）」的 cAMP 上升。配對 ＞ 兩次單獨之和＝協同（synergy），算是巧合偵測；配對 ＜ 和＝次加成（sub-additive）。再看協同在 *rutabaga*（*rut*，製造 cAMP 的酵素腺苷酸環化酶的基因）突變果蠅是否消失。
- **Handler 2019：cAMP 在時間差 0 最大。** 改變多巴胺與 KC 刺激的時間差，看 cAMP 在哪個時間差最高；同時開始時最高，作者稱 DopR1（一種多巴胺受體）的 cAMP 路徑為巧合偵測器，同時強調它「不能單獨編碼先後」。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | 用「配對 vs 相加」檢驗 *rut* 是不是巧合偵測器 | 238Y α 葉配對約為相加的 1.53 倍；*rut¹* 中約 0.94，協同消失；章魚胺配對反而次加成 |
| [[s-handler-2019-dopamine-receptor-timing]] | 以六個時間差下的 cAMP 大小判定 | cAMP 在 0 s 最大（約 0.15 ΔR/R），其餘時間差都較小但都顯著大於零 |

> 數值為從圖判讀，見 [[numbers]]。Hige 2015 只提到：討論中說「KC 與 DAN 的共同活動是可塑性的唯一決定因素」，但沒有量任何分子訊號，所以不列入表。
>
> **2015–2018 新收的五篇都只提到、沒有量分子層的巧合偵測，所以不列入表**：Cohn 2015 在討論中推測方向可能取決於能偵測「KC 活動與多巴胺是否同時出現」的下游訊號，資料上只比較了配對（＜ 500 ms）與不配對（＞ 45 s）的突觸方向（見 [[c-cs-us-timing]]）；Ichinose 2015 引 Trannoy et al. 2011 稱 *rutabaga* 為巧合偵測者；Aso 2016、Felsenberg 2017、Felsenberg 2018 沒有操作 cAMP 或其上游酵素（Felsenberg 2018 只在引言轉述 Schwaerzel et al. 2002 的「細胞內拮抗」）。
>
> **[[s-tully-1985-classical-conditioning]] 依同一條規則也不列入表**：它沒有量任何分子訊號，只量整隻果蠅的行為。它在討論中轉述海兔（*Aplysia*）的生化模型（Kandel et al. 1983），該模型把受鈣／攜鈣素（calmodulin，與鈣結合後去啟動其他酵素的蛋白）刺激的腺苷酸環化酶當成 CS（制約刺激）與 US（非制約刺激，如電擊）交會的點（原文「point of convergence」，PDF 第 275 頁），再用突變株的行為分數指出三處對不上，其中一處是：*rut* 缺這種環化酶活性，照模型應該學不會，實際上仍學到 Λ ≈ 0.41（Λ 是該篇的行為學習分數，0＝沒學到、1＝全部躲開被電的氣味）。它用到的是「模型的預測」，不是巧合偵測的量測。

## 引用時的陷阱

1. **兩個定義不是同一件事。** Tomchik 2009 要求配對「超過相加」；Handler 2019 只比較不同時間差下的 cAMP 高低。Handler 正文與方法中找不到「配對 vs 單獨相加」的 cAMP 比較（已 grep `synerg`、`additive`、`sum of`、`alone`；補充圖未取得，是否在補充圖中：？待查）。所以「兩篇都證明 cAMP 是巧合偵測器」這句話不能直接寫。
2. **巧合偵測 ≠ 先後偵測。** Tomchik 2009 的協同只在順向出現；Handler 2019 的 cAMP 兩種順序都有，先後交給 DopR2 的內質網放鈣路徑去分辨。兩篇對「cAMP 能否分辨先後」說法不同，見 [[syn-contradictions]] 1.2，本頁不裁決。
3. **Tomchik 2009 的證據限制**：缺「基因型 × 條件」的交互作用檢定；刺激是離體腦上的藥物模擬；協同幅度是多約五成，不是倍增。
4. **Handler 2019 的「0 s 最大」沒有被檢定**：論文方法章節（STAR Methods）的統計段對圖 5E 只列了「對零」的檢定，沒有檢定 0 s 是否高於相鄰時間差；「最大」是六個點的形狀。
5. **「*rut* 是巧合偵測器」不等於「學習全靠它」。** Tully 1985 的 *rut* 突變果蠅仍學得到 Λ ≈ 0.41（同日野生型 0.87）；Tomchik 2009 自己的討論也寫，*rut* 突變株的表現「降低但沒有消失」，所以至少還有一條其他的可塑性路徑（全文 text.txt 第 654–656 行）。Tomchik 2009 的協同是在 *rut¹* 中消失；Tully 1985 用的則是 *rutabaga* 的另一個突變版本（等位基因）*rut*^PS511。兩者若不是同一種缺損，就不能把「*rut¹* 沒有協同」和「*rut*^PS511 仍學得到」拼成同一隻果蠅的結論；兩者是否為同一突變：？待查。

## 相關

- 主題：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]
- 概念：[[c-camp-signaling]]、[[c-cs-us-timing]]、[[c-us-substitution]]
- 實體：[[e-rutabaga]]、[[e-kenyon-cell]]、[[e-epac-camp-sensor]]
- 綜述：[[syn-contradictions]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-tully-1985-classical-conditioning]]（只提到）
