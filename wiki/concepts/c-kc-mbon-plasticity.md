---
title: KC→MBON 突觸可塑性（KC-MBON synaptic plasticity）
created: 2026-10-25
updated: 2026-10-25
tags: [concept, active, mb-learning]
confidence: medium
---

# KC→MBON 突觸可塑性（KC-MBON synaptic plasticity）

**Kenyon 細胞（KC）把氣味訊號經突觸交給蘑菇體輸出神經元（MBON），MBON 再推動果蠅「靠近」或「走開」；這個突觸的強度被多巴胺改變，就是 KC→MBON 突觸可塑性。** 變弱並持續稱長期抑制（long-term depression, LTD），變強稱增強（potentiation）。由第三個神經元（這裡是多巴胺神經元 DAN）改變另外兩者之間突觸的現象，稱**異突觸可塑性（heterosynaptic plasticity）**；只由突觸兩端自身活動決定的，稱同突觸（homosynaptic）可塑性。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **KC**：Kenyon 細胞（Kenyon cell），蘑菇體（mushroom body，果蠅腦中把氣味和好壞連起來的構造）裡代表氣味的神經元，每種氣味只活化一小群。
- **DAN**：多巴胺神經元（dopaminergic neuron），送出代表懲罰或獎賞的多巴胺。依 Handler 2019 的說法，PAM 群多報告獎賞、PPL（PPL1）群多報告懲罰。
- **MBON**：蘑菇體輸出神經元（MB output neuron），接收 KC 的訊號，推動果蠅靠近或走開。
- **葉、萼部**：KC 的軸突（送出訊號的長枝）成束排成 α、α′、γ 等「葉」（lobe）；KC 的樹突（接收端）聚在「萼部」（calyx）。
- **區室**：葉沿長度切成的一格，以 γ1pedc、γ2、γ4、α2 等編號命名；細胞也以所在區室命名，例如 MBON-γ1pedc、PPL1-γ1pedc。詳見 [[c-mb-compartment]]。
- **光**：指光遺傳活化 DAN，即讓 DAN 帶上照紅光就放電的蛋白，用光代替真的懲罰或獎賞（見 [[c-us-substitution]]）。
- **forskolin**：直接活化製造 cAMP 的酵素的藥，用來人為拉高 cAMP。
- **ΔR/R、ΔF/F**：螢光感測器的訊號（兩色亮度比值，或亮度）相對刺激前基線的變化比例，例如 0.15＝高了 15%。只能在同一實驗內比大小。
- **離體、在體、閉迴路**：離體＝取出的腦泡在養液裡；在體＝活果蠅頭部固定、打開腦殼；閉迴路＝頭部固定的果蠅踩在球上走，送氣管隨牠的轉向轉動，可同時記錄行為與腦。
- **CS+／CS−**：訓練時配了糖或電擊的氣味／沒配的對照氣味。
- **−/−**：該基因兩份都被剔除。
- **DopR1、DopR2、內質網鈣**：KC 上兩種多巴胺受體。DopR1 接上製造 cAMP 的路徑；DopR2 接上讓內質網（細胞內存鈣的小倉庫）放出鈣的路徑，所以量內質網鈣就是在看 DopR2 路徑有沒有啟動。

## 怎麼算 / 怎麼判定

配對前後各量一次「同樣的 KC 輸入讓 MBON 反應多少」，相減或算比例：

- Hige 2015：活體全細胞記錄（把玻璃電極接上單一神經元、直接量它的電訊號）MBON，量氣味開始後 0–1.4 s 的放電次數，以及突觸電流的總電荷（電荷轉移，pC）。
- Handler 2019：離體腦以乙醯膽鹼刺激 KC，量 γ4 MBON 的鈣反應（用會隨鈣變亮的螢光蛋白 GCaMP6s 量，代表 MBON 被 KC 驅動的程度）的峰值 ΔF/F；在體則量 γ4 對氣味的反應。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-hige-2015-heterosynaptic-plasticity]] | 氣味配一顆 DAN 的光活化，直接量突觸 | **單向減弱**：MBON-γ1pedc 配對氣味放電降 80% ± 5.7%、電荷降 90% ± 3.7%，至少 40 分鐘；MBON 不放電也會發生（表示由 KC 與 DAN 決定，不需突觸後的活動）；逆向配對無效 |
| [[s-handler-2019-dopamine-receptor-timing]] | 不同時間差配對；剔除受體 | **雙向**：γ4 MBON 對 KC 刺激的峰值反應（ΔF/F）逆向（−1.2 s）配對前約 1.22 → 配對後 2.8，增強；順向（+0.5 s）配對前約 1.22 → 配對後 0.42，減弱；DopR1 剔除後不再減弱，DopR2 剔除後不再增強 |
| [[s-cohn-2015-coordinated-neuromodulation]] | 離體：P2X2＋ATP 活化 γ4/γ5 DAN，膜片鉗或鈣影像量 γ4 MBON；配對（＜ 500 ms）與不配對（＞ 45 s）輪流做 | **不配對也會改變，而且是變強**：γ4 MBON 的 EPSC 約 1.5 → 16 pA，ΔF/F0 約 0.7 → 2.5；配對讓已被增強的反應壓回（約 2.0 → 0.35）；活體雙氣味實驗中，配對氣味相對未配對氣味的比值約 1.35 → 0.6 |
| [[s-felsenberg-2017-re-evaluation]] | 糖獎賞訓練後 3 小時，活體量 γ2α′1 MBON 對 CS+、CS− 的鈣反應 | **沒配糖的 CS− 反應變大**（標準化 AUC 約 +14% 與 +24%），CS+ 不變；V2 群 MBON 不變 |
| [[s-felsenberg-2018-memory-extinction]] | 電擊訓練或訓練後再消退，活體量 MVP2、M4β′、M6 的樹突與軸突 | MVP2 樹突 CS+ ＜ CS−（嫌惡痕跡），消退後仍在；M6 樹突在消退後新出現 CS+ ＜ CS−；只訓練時 M6 軸突 CS+ 較大、樹突沒有 |
| [[s-tomchik-2009-camp-dynamics]] | **沒量 KC→MBON 突觸。** 量的是 KC 軸突本身的鈣反應在 cAMP 拉高後是否變大 | forskolin 使 α 葉鈣反應約 3.2 倍、多巴胺約 2 倍；作者稱「突觸前可塑性」，討論中稱其為異突觸 |

> 數值見 [[numbers]]；γ4 與 Tomchik 的倍數為從圖判讀。

## 引用時的陷阱

1. **Tomchik 2009 的「增強」不是突觸增強。** KC 軸突裡的鈣變大只是「可能送出較多訊號」的間接指標；洗掉藥物後似乎回落（單一範例）。它與 Hige 2015 的 LTD 方向看似相反，但量的不是同一個東西，不能當成矛盾，也不能當成 Handler 2019 增強的前驅證據。
2. **Hige 2015 的「九成」是電荷總量。** 電流一開始的峰值大致保留，少掉的是之後的持續段。
3. **Hige 2015 只活化可取代嫌惡電擊的 PPL1 型 DAN**，沒看到增強不代表不存在；逆向「無效」與 Handler 2019 逆向「增強」的不同，見 [[syn-contradictions]] 1.1。
4. **Handler 2019 的增強證據較薄**：離體只有 −1.2 s 一點顯著；在體實驗是順向、逆向交替訓練，逆向造成的增強只把前一次順向壓低的反應部分拉回。
5. **改變在突觸前還是突觸後未定**（Hige 2015 自陳）。Cohn 2015 直接量了 KC 突觸前末梢的鈣，看到它隨多巴胺逐格改變，但沒有量**配對後**的末梢鈣，所以仍沒回答配對造成的減弱在哪一側（見 [[c-presynaptic-calcium]]）。Felsenberg 2018 引言把突觸前減弱列為已知，合併引用的文獻包括 Tomchik 2009 與 Hige 2015；本庫對這兩篇的紀錄並不支持這個說法（Tomchik 量到的是 KC 鈣反應**變大**）。
6. **Cohn 2015 的「配對減弱」有兩個條件。** 離體實驗是從已被增強的狀態開始配對；活體實驗量的是配對氣味對未配對氣味的比值，比值下降也可能來自未配對氣味被增強。
7. **「不配對」的時間尺度兩篇對不上。** Cohn 2015 相隔 ＞ 45 s 讓 γ4 突觸變強；Handler 2019 相隔 6 s 幾乎不變。見 [[syn-contradictions]] 1.3，未裁決。
8. **現有規則只處理與 DAN 配對的氣味。** Felsenberg 2017 的 CS− 反應變大發生在沒有與糖配對的氣味上，本頁整理的規則無法直接解釋（[[syn-contradictions]] 3.7）。Ichinose 2015 的模型是 MBON-α1 回頭讓同格的 PAM-α1 更活躍、延長多巴胺釋放（見 [[t-mbon-dan-feedback]]）；這隱含配對後 CS+ 仍能驅動 MBON-α1，與「順向配對讓突觸變弱」有張力（[[syn-contradictions]] 3.6）；Ichinose 2015 本身沒有量突觸變強或變弱。
9. **樹突沒變不等於輸出沒變。** Felsenberg 2018：學習讓 M6 軸突的 CS+ 反應變大，樹突卻看不出差別；作者以鄰格 MVP2 的抑制性輸入作用在 M6 樹突根部附近解釋。只量樹突會漏掉這類網路造成的改變。

## 相關

- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]、[[t-memory-updating]]
- 概念：[[c-mb-compartment]]、[[c-camp-signaling]]、[[c-cs-us-timing]]、[[c-presynaptic-calcium]]、[[c-whole-cell-patch-clamp]]
- 實體：[[e-kenyon-cell]]、[[e-mbon]]、[[e-dopaminergic-neuron]]、[[e-gcamp]]、[[e-mbon-gamma4]]、[[e-mbon-gamma1pedc]]、[[e-mbon-gamma2alpha1]]、[[e-mbon-gamma5beta2a]]、[[e-dopamine-receptor]]
- 綜述：[[syn-contradictions]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
